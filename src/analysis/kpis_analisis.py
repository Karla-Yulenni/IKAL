"""
Etapa 7 - Definicion y calculo de KPI
Proyecto IKAL - Catalogo de indicadores clave de desempeno
Autor: Rous (Maria del Rosario Maldonado Hilario)
"""
import csv
from collections import defaultdict
from datetime import date
import statistics as st
import json

def load(fn):
    with open(fn, encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

ventas = load('ventas_corregido.csv')
productos = load('productos_corregido.csv')
artesanos = load('artesanos_corregido.csv')

prod_by_id = {p['producto_id']: p for p in productos}
ventas_validas = [v for v in ventas if v['estatus'] != 'Cancelado']

kpis = {}

# KPI 1: Margen promedio del artesano
art_prods = [p for p in productos if p['tipo']=='Artesano']
margenes = [(float(p['precio_venta'])-float(p['costo']))/float(p['precio_venta'])*100 for p in art_prods]
kpis['margen_artesano'] = round(st.mean(margenes),1)

# KPI 2: % artesanos activos
ing_neto_art = defaultdict(float)
for v in ventas_validas:
    p = prod_by_id.get(v['producto_id'])
    if p: ing_neto_art[p['artesano_id']] += float(v['total'])
activos = sum(1 for a in artesanos if ing_neto_art.get(a['artesano_id'],0) > 0)
kpis['pct_artesanos_activos'] = round(activos/len(artesanos)*100,1)
kpis['artesanos_activos_n'] = activos
kpis['artesanos_total_n'] = len(artesanos)

# KPI 3: % ventas fuera de region
region = {'Xicotepec de Juárez','Pantepec'}
fuera = sum(1 for v in ventas_validas if v['ubicacion_comprador'] not in region)
kpis['pct_fuera_region'] = round(fuera/len(ventas_validas)*100,1)

# KPI 4: tasa de cancelacion
kpis['tasa_cancelacion'] = round((len(ventas)-len(ventas_validas))/len(ventas)*100,1)

# KPI 5: ticket promedio - tendencia trimestral
def quarter(fecha_str):
    d = date.fromisoformat(fecha_str)
    q = (d.month-1)//3+1
    return f"{d.year}-Q{q}"

q_ing = defaultdict(float)
q_n = defaultdict(int)
for v in ventas_validas:
    q = quarter(v['fecha_venta'])
    q_ing[q]+=float(v['total'])
    q_n[q]+=1

quarters_sorted = sorted(q_ing.keys())
ticket_by_q = {q: round(q_ing[q]/q_n[q],2) for q in quarters_sorted}
kpis['ticket_promedio_global'] = round(sum(float(v['total']) for v in ventas_validas)/len(ventas_validas),2)
kpis['ticket_por_trimestre'] = ticket_by_q

qs = quarters_sorted
last4 = qs[-5:-1]
prev4 = qs[-9:-5]
avg_last4 = st.mean(ticket_by_q[q] for q in last4)
avg_prev4 = st.mean(ticket_by_q[q] for q in prev4)
kpis['ticket_avg_ultimos4_completos'] = round(avg_last4,2)
kpis['ticket_avg_4_anteriores'] = round(avg_prev4,2)
kpis['ticket_tendencia_pct'] = round((avg_last4-avg_prev4)/avg_prev4*100,1)

# KPI 6: margen por categoria
cat_margen = defaultdict(list)
for p in productos:
    m = (float(p['precio_venta'])-float(p['costo']))/float(p['precio_venta'])*100
    cat_margen[p['categoria']].append(m)
kpis['margen_por_categoria'] = {c: round(st.mean(v),1) for c,v in cat_margen.items()}

with open('kpis_resultados.json','w',encoding='utf-8') as f:
    json.dump(kpis, f, ensure_ascii=False, indent=2)

print(json.dumps(kpis, indent=2, ensure_ascii=False))
