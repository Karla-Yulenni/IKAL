# Reporte del proceso ETL — IKAL

```
=== 1. EXTRACCIÓN ===
Se leyeron 4 archivos: 60 artesanos, 900 compradores, 150 productos, 3629 ventas

=== 2. PERFILADO INICIAL (revisar errores antes de corregir) ===
Nulos en compradores.ubicacion: 10
Ventas duplicadas: 15
Categorías mal escritas (mayúsculas): 20
Fechas en formato raro (con '/' en vez de '-'): 181
Nombres con espacios de más: 15

=== 3. TRANSFORMACIÓN (aquí se arregla todo) ===
✓ Nulos en ubicación corregidos: 10 filas
✓ Ventas duplicadas eliminadas: 15
✓ Categorías normalizadas
✓ Fechas convertidas todas al mismo formato (YYYY-MM-DD)
✓ Espacios extra eliminados en nombres
✓ Ventas sin comprador válido eliminadas: 0

=== 4. CARGA (guardar archivos limpios) ===
✓ 4 archivos limpios guardados en data/processed/

=== 5. VALIDACIÓN FINAL ===
Nulos que quedan: 0 (debe ser 0)
Duplicados que quedan: 0 (debe ser 0)
Filas finales: 60 artesanos, 900 compradores, 150 productos, 3614 ventas
```
