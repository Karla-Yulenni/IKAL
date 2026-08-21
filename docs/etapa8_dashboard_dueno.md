# Etapa 8: Dashboard del Dueño del Negocio

## 8.1 Definición del Usuario (Administración)
* **Qué decisiones toma:** Optimización de inventarios por categoría de producto, estrategias de expansión geográfica y campañas de apoyo directo para equilibrar las ventas entre los artesanos locales (zona de Xicotepec) y la Marca IKAL.
* **Qué información necesita:** Ingresos totales acumulados, volumen de ventas, distribución geográfica de la oferta y la demanda, desempeño por categoría de producto y preferencias de método de pago.
* **Con qué frecuencia consulta los datos:** Revisión operativa semanal y análisis financiero estratégico de forma mensual.
* **Qué nivel de detalle requiere:** Una vista general (macronivel) con capacidad de analizar tendencias históricas (2024-2026) y segmentar por tipo de vendedor (Artesano vs. Marca IKAL).
* **Qué alertas son importantes:** Caídas repentinas en el registro de compradores o una disminución crítica en la participación de los artesanos en las ventas globales.

## 8.2 Elaboración del Diseño (Wireframes, Mockups y Prototipo)
* **Sketch y Wireframe:** Se diseñó un panel estructurado en bloques para facilitar la lectura en un solo vistazo:
  1. *Extremo Izquierdo:* Indicadores clave de rendimiento (KPIs) numéricos y tendencias históricas en gráficas de líneas.
  2. *Centro:* Distribución geográfica de los productores (mapa local) y análisis detallado de categorías mediante un gráfico de barras horizontales.
  3. *Extremo Derecho:* Alcance geográfico de clientes (mapa nacional) y gráficos de proporción en formato anillo.
* **Mockup y Prototipo:** Se implementó utilizando una paleta de colores acorde a la identidad institucional de IKAL, usando un fondo con textura artesanal, contrastado con tonos verde oscuro, gris y blanco para mantener la legibilidad y evitar la saturación visual.

## 8.3 Organización de la Información
El panel integra los siguientes componentes analíticos:
* **KPI Principales:** Ingresos totales ($2,588,255.55 MXN) y Total de Ventas (3614).
* **Ventas e Ingresos (Categorías):** Gráfica comparativa de los productos más demandados (Bordados, Blusas, Playeras, Bolsas, Accesorios y Aretes), separando el rendimiento por tipo de productor.
* **Tendencia Temporal:** Evolución del registro histórico tanto de compradores como de artesanos en el periodo 2024-2026.
* **Clientes y Proveedores (Geografía):** Mapas independientes que contrastan el origen de manufactura (San Ambrosio / Xicotepec de Juárez) contra el destino de compra (concentración en el centro de México y dispersión nacional).
* **Ventas (Proporciones):** Gráficas de anillo que muestran las Preferencias de Pago (51% Débito vs 49% Crédito) y la Distribución global por ventas (68% Marca IKAL vs 32% Artesano).

## 8.4 Incorporación de Interacción (Filtros)

El dashboard está preparado para interactuar mediante los siguientes filtros dinámicos:
* **Fecha:** Selector de rango temporal para aislar meses o años específicos.
* **Categoría:** Opción para aislar el comportamiento de un solo producto (ej. solo "Bordado").
* **Región:** Capacidad de hacer zoom en los mapas para analizar zonas geográficas particulares.

## 8.5 Integración de Alertas de Negocio
Reglas de negocio configuradas para notificar al administrador:
* **Disminución de ventas:** Alerta si el registro de compradores en la gráfica de líneas presenta una tendencia a la baja durante semanas consecutivas.
* **Desbalance de inventario/ventas:** Aviso preventivo si la proporción de ventas de la "Marca IKAL" opaca drásticamente las ventas de la categoría "Artesano", para no perder el enfoque social del modelo de negocio.

## Pregunta Principal de Negocio
* **¿Qué está ocurriendo?** El negocio presenta ingresos superiores a los 2.5 millones de pesos con una fuerte tracción. La "Marca IKAL" domina el volumen de distribución global (68%), aunque en categorías específicas como "Playeras" y "Blusas", el "Artesano" tiene un impacto superior.
* **¿Por qué está ocurriendo?** La plataforma ha conectado la producción hiperlocal (concentrada en Veracruz/Puebla) con un mercado de compradores expandido a nivel nacional, manteniendo una confianza de pago equilibrada entre crédito y débito.
* **¿Qué decisión debería tomar el negocio?** Implementar estrategias de marketing dirigidas a impulsar las ventas directas de la categoría "Artesano" (para equilibrar el 32% actual) y asegurar el stock de los productos líderes (Bordados y Playeras) en las temporadas de mayor registro de compradores.

  
![Dashboard del administrador](img/dashboard_dueño.png)
