"""
Etapa 6 - Mecanismo analitico de diagnostico
Proyecto IKAL - Analisis de rentabilidad y equidad por artesano, comunidad y categoria
Autor: Rous (Maria del Rosario Maldonado Hilario)
"""
import csv
from collections import defaultdict, Counter
from datetime import date
import statistics as st
import json

def load(fn):
    with open(fn, encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

ventas = load('ventas_corregido.csv')
productos = load('productos_corregido.csv')
compradores = load('compradores_corregido.csv')
artesanos = load('artesanos_corregido.csv')

prod_by_id = {p['producto_id']: p for p in productos}
art_by_id = {a['artesano_id']: a for a in artesanos}

# Solo ventas NO canceladas para todo calculo de ingreso/rentabilidad real
ventas_validas = [v for v in ventas if v['estatus'] != 'Cancelado']

resultados = {}

# ---- 1. Resumen general ----
resultados['resumen'] = {
    'total_ventas': len(ventas),
    'ventas_validas': len(ventas_validas),
    'ventas_canceladas': len(ventas) - len(ventas_validas),
    'tasa_cancelacion_pct': round((len(ventas)-len(ventas_validas))/len(ventas)*100, 1),
    'ingreso_bruto': round(sum(float(v['total']) for v in ventas), 2),
    'ingreso_neto': round(sum(float(v['total']) for v in ventas_validas), 2),
    'total_artesanos': len(artesanos),
    'total_productos': len(productos),
    'total_compradores': len(compradores),
    'periodo': f"{min(v['fecha_venta'] for v in ventas)} a {max(v['fecha_venta'] for v in ventas)}",
}

# ---- 2. Rentabilidad neta por artesano ----
ing_neto_art = defaultdict(float)
unid_neto_art = defaultdict(int)
for v in ventas_validas:
    p = prod_by_id.get(v['producto_id'])
    if p:
        ing_neto_art[p['artesano_id']] += float(v['total'])
        unid_neto_art[p['artesano_id']] += int(v['cantidad'])

art_rows = []
for a in artesanos:
    aid = a['artesano_id']
    art_rows.append({
        'nombre': a['nombre'], 'ubicacion': a['ubicacion'],
        'fecha_registro': a['fecha_registro'],
        'productos_publicados': int(a['productos_publicados']),
        'ingreso_neto': round(ing_neto_art.get(aid,0),2),
        'unidades_vendidas_neto': unid_neto_art.get(aid,0),
    })
art_rows.sort(key=lambda r: -r['ingreso_neto'])
resultados['top10_artesanos'] = art_rows[:10]
resultados['bottom10_artesanos'] = art_rows[-10:]
ingresos_art = [r['ingreso_neto'] for r in art_rows]
resultados['stats_ingreso_artesano'] = {
    'media': round(st.mean(ingresos_art),2),
    'mediana': round(st.median(ingresos_art),2),
    'min': round(min(ingresos_art),2),
    'max': round(max(ingresos_art),2),
}
inactivos = [r for r in art_rows if r['productos_publicados']==0]
resultados['artesanos_inactivos'] = inactivos
resultados['pct_inactivos'] = round(len(inactivos)/len(artesanos)*100,1)

# ---- 3. Rentabilidad por comunidad ----
com_ing = defaultdict(float)
com_n = defaultdict(int)
for a in artesanos:
    com_ing[a['ubicacion']] += ing_neto_art.get(a['artesano_id'],0)
    com_n[a['ubicacion']] += 1
resultados['por_comunidad'] = {u: {'ingreso_neto': round(v,2), 'n_artesanos': com_n[u], 'promedio_por_artesano': round(v/com_n[u],2)} for u,v in com_ing.items()}

# ---- 4. Rentabilidad por categoria/tecnica ----
cat_ing = defaultdict(float)
cat_margen = defaultdict(list)
cat_n_ventas = defaultdict(int)
for v in ventas_validas:
    p = prod_by_id.get(v['producto_id'])
    if p:
        cat = p['categoria']
        cat_ing[cat] += float(v['total'])
        cat_n_ventas[cat] += 1
for p in productos:
    margen = (float(p['precio_venta'])-float(p['costo']))/float(p['precio_venta'])*100
    cat_margen[p['categoria']].append(margen)

resultados['por_categoria'] = {
    cat: {
        'ingreso_neto': round(cat_ing[cat],2),
        'n_ventas': cat_n_ventas[cat],
        'margen_promedio_pct': round(st.mean(cat_margen[cat]),1)
    } for cat in cat_ing
}

# ---- 5. Marca IKAL vs artesanos (benchmark por producto) ----
marca_prods = [p for p in productos if p['tipo']=='Marca IKAL']
art_prods = [p for p in productos if p['tipo']=='Artesano']

ing_neto_prod = defaultdict(float)
for v in ventas_validas:
    ing_neto_prod[v['producto_id']] += float(v['total'])

ing_marca = sum(ing_neto_prod.get(p['producto_id'],0) for p in marca_prods)
ing_art_total = sum(ing_neto_prod.get(p['producto_id'],0) for p in art_prods)

resultados['benchmark_marca_ikal'] = {
    'ingreso_neto_marca_ikal': round(ing_marca,2),
    'ingreso_neto_artesanos_total': round(ing_art_total,2),
    'pct_ingreso_marca_ikal': round(ing_marca/(ing_marca+ing_art_total)*100,1),
    'ingreso_promedio_por_producto_marca': round(ing_marca/len(marca_prods),2),
    'ingreso_promedio_por_producto_artesano': round(ing_art_total/len(art_prods),2),
    'ratio_por_producto': round((ing_marca/len(marca_prods))/(ing_art_total/len(art_prods)),2),
    'margen_promedio_marca_pct': round(st.mean([(float(p['precio_venta'])-float(p['costo']))/float(p['precio_venta'])*100 for p in marca_prods]),1),
    'margen_promedio_artesano_pct': round(st.mean([(float(p['precio_venta'])-float(p['costo']))/float(p['precio_venta'])*100 for p in art_prods]),1),
}

# ---- 6. Alcance geografico ----
region = {'Xicotepec de Juárez','Pantepec'}
ubic_counts = Counter(v['ubicacion_comprador'] for v in ventas_validas)
total_v = len(ventas_validas)
fuera = sum(c for u,c in ubic_counts.items() if u not in region)
resultados['alcance_geografico'] = {
    'pct_fuera_region': round(fuera/total_v*100,1),
    'pct_dentro_region': round((total_v-fuera)/total_v*100,1),
    'top_ubicaciones': ubic_counts.most_common(8),
}

# ---- 7. Cancelaciones por canal ----
canal_stats = defaultdict(lambda: [0,0])
for v in ventas:
    canal_stats[v['canal']][0]+=1
    if v['estatus']=='Cancelado':
        canal_stats[v['canal']][1]+=1
resultados['cancelacion_por_canal'] = {c: {'total':t,'canceladas':cc,'tasa_pct':round(cc/t*100,1)} for c,(t,cc) in canal_stats.items()}

with open('resultados.json','w',encoding='utf-8') as f:
    json.dump(resultados, f, ensure_ascii=False, indent=2)

print(json.dumps(resultados, ensure_ascii=False, indent=2))
