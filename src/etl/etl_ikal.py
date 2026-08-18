"""
ETL — IKAL Alma Artesanal
Limpia los datasets de data/raw/ y guarda el resultado en data/processed/

Cómo ejecutarlo:
    python src/etl/etl_ikal.py
"""
import pandas as pd

RAW = 'data/raw'
PROCESSED = 'data/processed'
LOG = []  # aquí se va guardando todo lo que hace el script, para el reporte

def log(mensaje):
    print(mensaje)
    LOG.append(mensaje)

# ══════════════════════════════════════════════════════════════
# PASO 1: EXTRACCIÓN — abrir los archivos originales (con errores)
# ══════════════════════════════════════════════════════════════
log("=== 1. EXTRACCIÓN ===")
artesanos = pd.read_csv(f'{RAW}/artesanos.csv', encoding='utf-8-sig')
compradores = pd.read_csv(f'{RAW}/compradores.csv', encoding='utf-8-sig')
productos = pd.read_csv(f'{RAW}/productos.csv', encoding='utf-8-sig')
ventas = pd.read_csv(f'{RAW}/ventas.csv', encoding='utf-8-sig')
log(f"Se leyeron 4 archivos: {len(artesanos)} artesanos, {len(compradores)} compradores, "
    f"{len(productos)} productos, {len(ventas)} ventas")

# ══════════════════════════════════════════════════════════════
# PASO 2: PERFILADO — revisar QUÉ errores tiene, antes de tocar nada
# ══════════════════════════════════════════════════════════════
log("\n=== 2. PERFILADO INICIAL (revisar errores antes de corregir) ===")
log(f"Nulos en compradores.ubicacion: {compradores['ubicacion'].isna().sum()}")
log(f"Ventas duplicadas: {ventas.duplicated(subset='venta_id').sum()}")
log(f"Categorías mal escritas (mayúsculas): "
    f"{(productos['categoria'] != productos['categoria'].str.capitalize()).sum()}")
log(f"Fechas en formato raro (con '/' en vez de '-'): "
    f"{ventas['fecha_venta'].astype(str).str.contains('/').sum()}")
log(f"Nombres con espacios de más: "
    f"{(artesanos['nombre'] != artesanos['nombre'].str.strip()).sum()}")

# ══════════════════════════════════════════════════════════════
# PASO 3: TRANSFORMACIÓN — aquí se corrige cada error, uno por uno
# ══════════════════════════════════════════════════════════════
log("\n=== 3. TRANSFORMACIÓN (aquí se arregla todo) ===")

# 3.1 — Rellenar los nulos en ubicación con un texto por defecto
antes = compradores['ubicacion'].isna().sum()
compradores['ubicacion'] = compradores['ubicacion'].fillna('No especificado')
log(f"✓ Nulos en ubicación corregidos: {antes} filas")

# 3.2 — Quitar las ventas que están repetidas
antes = len(ventas)
ventas = ventas.drop_duplicates(subset='venta_id', keep='first')
log(f"✓ Ventas duplicadas eliminadas: {antes - len(ventas)}")

# 3.3 — Arreglar categorías (ej. "BOLSA" -> "Bolsa")
productos['categoria'] = productos['categoria'].str.strip().str.capitalize()
log("✓ Categorías normalizadas")

# 3.4 — Arreglar fechas que estaban en formato DD/MM/YYYY
ventas['fecha_venta'] = pd.to_datetime(ventas['fecha_venta'], format='mixed', dayfirst=True)
ventas['fecha_venta'] = ventas['fecha_venta'].dt.strftime('%Y-%m-%d')
log("✓ Fechas convertidas todas al mismo formato (YYYY-MM-DD)")

# 3.5 — Quitar espacios de más en los nombres
artesanos['nombre'] = artesanos['nombre'].str.strip()
log("✓ Espacios extra eliminados en nombres")

# 3.6 — Verificar que no haya ventas de compradores que no existen
ids_validos = set(compradores['comprador_id'])
huerfanas = (~ventas['comprador_id'].isin(ids_validos)).sum()
ventas = ventas[ventas['comprador_id'].isin(ids_validos)]
log(f"✓ Ventas sin comprador válido eliminadas: {huerfanas}")

# ══════════════════════════════════════════════════════════════
# PASO 4: CARGA — guardar la versión ya limpia
# ══════════════════════════════════════════════════════════════
log("\n=== 4. CARGA (guardar archivos limpios) ===")
import os
os.makedirs(PROCESSED, exist_ok=True)
artesanos.to_csv(f'{PROCESSED}/artesanos.csv', index=False, encoding='utf-8-sig')
compradores.to_csv(f'{PROCESSED}/compradores.csv', index=False, encoding='utf-8-sig')
productos.to_csv(f'{PROCESSED}/productos.csv', index=False, encoding='utf-8-sig')
ventas.to_csv(f'{PROCESSED}/ventas.csv', index=False, encoding='utf-8-sig')
log(f"✓ 4 archivos limpios guardados en {PROCESSED}/")

# ══════════════════════════════════════════════════════════════
# PASO 5: VALIDACIÓN FINAL — confirmar que ya quedó todo bien
# ══════════════════════════════════════════════════════════════
log("\n=== 5. VALIDACIÓN FINAL ===")
log(f"Nulos que quedan: {compradores['ubicacion'].isna().sum()} (debe ser 0)")
log(f"Duplicados que quedan: {ventas.duplicated(subset='venta_id').sum()} (debe ser 0)")
log(f"Filas finales: {len(artesanos)} artesanos, {len(compradores)} compradores, "
    f"{len(productos)} productos, {len(ventas)} ventas")

# Guardar el reporte para poder mostrarlo como evidencia
with open('docs/etl-report.md', 'w', encoding='utf-8') as f:
    f.write("# Reporte del proceso ETL — IKAL\n\n```\n" + "\n".join(LOG) + "\n```\n")

print("\n✅ Terminado. Revisa docs/etl-report.md para ver el reporte completo.")
