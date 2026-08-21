# Etapa 9: Dashboard del Cliente

## 9.1 Definir el valor para el cliente
Para el modelo de negocio de IKAL, el concepto de "cliente" abarca dos roles clave que interactúan en la plataforma. El valor para cada uno se define de la siguiente manera:
1. **Comprador Final (E-commerce):** Le permite consultar su historial de compras, controlar sus gastos (inversión total), revisar el progreso logístico de sus pedidos en tiempo real e identificar sus preferencias de consumo.
2. **Cliente-Artesano (B2B):** Le proporciona una herramienta de inteligencia operativa para conocer sus ingresos exactos, medir el alcance geográfico de sus piezas y revisar qué productos son sus "best-sellers" para enfocar su tiempo de producción.

## 9.2 Diseñar visualizaciones personalizadas

### A. Dashboard del Comprador (E-commerce)
Diseñado para ofrecer claridad y control sobre la cuenta personal del usuario:
* **KPIs (Métricas Clave):** Total invertido en la plataforma ($16,022.63 MXN), número de pedidos realizados (22) y fecha exacta de su última compra (viernes, 22 de mayo de 2026).
* **Evolución de mis compras:** Gráfica de líneas que muestra el comportamiento de su gasto a lo largo de los meses (con picos de compra en septiembre y noviembre).
* **Seguimiento de mis compras:** Gráfica de embudo que transparenta el estado logístico de sus 22 pedidos (18 entregados, 3 enviados y 1 cancelado).
* **Preferencias de compra:** Gráfico de anillo que le muestra su estilo personal de consumo (36.36% Blusas, 27.27% Playeras, 22.73% Bordados y 13.64% Accesorios).

![Dashboard Comprador](img/dashboard_comprador.png)

### B. Dashboard del Cliente-Artesano (B2B / Operativo)
Diseñado como un panel de control para empoderar al productor local:
* **KPIs (Métricas Clave):** Catálogo activo (5 productos publicados), ingresos totales generados por su trabajo ($258,579.98 MXN) y artículos vendidos (447).
* **Tendencia de Ventas Mensuales:** Gráfica de líneas que revela sus temporadas altas (mostrando un pico crítico de ventas entre mayo y junio).
* **Distribución de Clientes:** Mapa interactivo de México que le muestra en qué ciudades tiene más impacto su arte (fuerte concentración en Monterrey, Guadalajara, CDMX y Estado de México).
* **Top Productos:** Gráfica de barras horizontales para identificar rápidamente qué piezas le generan más ingresos (liderado por la "Playera nahua" y la "Blusa punto de cruz").

![Dashboard Artesano](img/dashboard_artesano.png)

## 9.3 Proteger la información
Para garantizar la privacidad y seguridad, estos dashboards operan bajo reglas estrictas:
* **Datos personales aislados:** El comprador final solo ve sus propios hábitos de consumo; en ningún momento se muestran métricas, nombres o datos de otros usuarios.
* **Privacidad financiera:** No se muestran números de tarjetas de crédito, cuentas bancarias ni credenciales de acceso, únicamente los totales de gasto/ingreso ya procesados.
* **Protección del comprador frente al artesano:** En el mapa de "Distribución de Clientes" del artesano, los datos están agregados a nivel macro (por ciudad). No se revelan nombres, direcciones exactas ni teléfonos de los compradores finales, protegiendo su anonimato.

## Pregunta principal
**¿Cómo puede el cliente comprender y aprovechar mejor su relación con el negocio?**
* **El Comprador:** Al tener visibilidad total de sus gastos y el estatus de sus envíos, genera mayor confianza en IKAL, reduciendo la ansiedad post-compra y permitiéndole administrar su presupuesto para futuras adquisiciones de moda artesanal.
* **El Artesano:** Aprovecha la plataforma no solo como un escaparate, sino como una guía de negocios. Al saber que sus mayores ventas ocurren en mayo-junio y que la "Playera nahua" es su producto estrella en grandes ciudades, puede anticipar la compra de insumos y enfocar su tiempo de bordado de manera estratégica para maximizar sus ganancias.
