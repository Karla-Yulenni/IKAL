# IKAL
---
## Plataforma digital para la comercialización de artesanías regionales
---
IKAL es una plataforma web regional enfocada en la comercialización de artesanías elaboradas por artesanos de Xicotepec y Pantepec.

El proyecto busca conectar directamente a los artesanos con compradores interesados en adquirir productos regionales a un precio justo, reduciendo la participación de intermediarios que pueden comprar las artesanías a precios bajos para posteriormente revenderlas a turistas a precios considerablemente mayores.

---

# Propósito del proyecto

El propósito de IKAL es desarrollar una plataforma web regional que permita a artesanos de Xicotepec y Pantepec comercializar sus productos de manera directa, reduciendo la participación de intermediarios y facilitando el acceso a compradores interesados en adquirir artesanías a un precio justo.

La plataforma busca ampliar el mercado de los artesanos mediante herramientas digitales que permitan publicar y administrar productos, establecer comunicación directa con los compradores, realizar pagos en línea y consultar información sobre sus ventas.

Además, IKAL busca promover las artesanías de la región y dar mayor visibilidad a los productos locales, incluyendo propuestas innovadoras como artesanías con realidad aumentada en sus bordados.

---

# Objetivo general del proyecto

Procesar, analizar e interpretar información del negocio mediante herramientas y metodologías de analítica de datos, con la finalidad de identificar tendencias, patrones, métricas e indicadores clave que apoyen la toma de decisiones.

---

# Flujo general de trabajo

El proyecto seguirá un flujo de trabajo basado en las siguientes etapas:

**Contexto del negocio**  
↓  
**Problema y preguntas de negocio**  
↓  
**Entidades, atributos y fuentes de datos**  
↓  
**Simulación estratégica del dataset**  
↓  
**Proceso ETL**  
↓  
**Análisis exploratorio de datos**  
↓  
**Mecanismo analítico**  
↓  
**Definición de KPI**  
↓  
**Dashboard del dueño**  
↓  
**Dashboard del cliente**  
↓  
**Diagnóstico y recomendaciones**  
↓  
**Documentación, GitHub y defensa**

---

# Etapas del proyecto

## Etapa 1. Contexto, problemática y objetivos analíticos

### 1.1 Descripción del negocio

IKAL es una plataforma web regional enfocada en la comercialización de artesanías elaboradas por artesanos de Xicotepec y Pantepec.

La plataforma permite que los artesanos se registren, administren su perfil y publiquen, editen o eliminen sus productos.

Los compradores pueden consultar y filtrar las artesanías de acuerdo con diferentes características, como tipo de bordado, color, categoría del producto, ropa o accesorio.

IKAL también permite la comunicación directa entre compradores y artesanos mediante un chatbot y ofrece la posibilidad de realizar pagos con tarjeta.

Los artesanos pueden consultar información relacionada con sus ventas, productos más y menos vendidos, ingresos y número de pedidos.

La plataforma cuenta además con un perfil administrativo desde el cual se puede supervisar la información de los artesanos, consultar su procedencia y gestionar usuarios que no cumplan con los requisitos establecidos.

Como parte de su propuesta, las creadoras de IKAL también participan como artesanas dentro de la plataforma, ofreciendo productos que incorporan realidad aumentada en sus bordados.

El modelo de negocio contempla diferentes fuentes de ingresos, entre ellas la venta de productos, anuncios y colaboraciones.

---

### 1.2 Problema

Los artesanos de Xicotepec y Pantepec pueden tener dificultades para comercializar sus productos directamente con consumidores interesados en adquirir artesanías a un precio justo.

La participación de intermediarios puede provocar que los productos sean adquiridos a precios bajos y posteriormente revendidos a turistas a precios considerablemente mayores.

Esta situación puede limitar el alcance comercial de los artesanos y reducir los beneficios económicos obtenidos por su trabajo. Además, la falta de canales digitales especializados puede dificultar que sus productos lleguen a compradores fuera de su entorno local.

Por ello, IKAL busca proporcionar un espacio digital que permita conectar directamente a artesanos y compradores, ampliar el mercado de las artesanías regionales y facilitar que los productores tengan mayor control sobre la comercialización de sus productos.

---

### 1.3 Stakeholders

| Stakeholder | Interés o participación |
|---|---|
| Artesanos | Publicar y vender sus productos, administrar su perfil y consultar sus ventas. |
| Compradores | Buscar, filtrar y comprar artesanías directamente a los productores. |
| Administradores de IKAL | Supervisar usuarios, productos y funcionamiento de la plataforma. |
| Turistas | Encontrar y adquirir artesanías regionales directamente de los artesanos. |
| Colaboradores y anunciantes | Promocionar productos o servicios dentro de la plataforma. |
| IKAL | Facilitar la comercialización y obtener ingresos mediante ventas, anuncios y colaboraciones. |

---

### 1.4 Preguntas de negocio

1. ¿Cuáles son los productos más vendidos en IKAL?
2. ¿Cuáles son los productos menos vendidos?
3. ¿Qué artesanos generan mayores ingresos?
4. ¿Cómo varían las ventas a lo largo del tiempo?
5. ¿Qué categorías de productos tienen mayor demanda?
6. ¿De qué localidades provienen los artesanos registrados?
7. ¿Cuántos pedidos y cuánto ingreso genera la plataforma?
8. ¿Qué características de los productos tienen mayor relación con su nivel de ventas?

---

### 1.5 Objetivo analítico

Analizar los datos de IKAL relacionados con artesanos, productos, pedidos y ventas para identificar tendencias, patrones y características asociadas al comportamiento comercial de la plataforma, con el fin de generar indicadores y hallazgos que permitan evaluar su desempeño y apoyar la toma de decisiones.

---

## Antecedentes de diseño — Preguntas HMW

Como parte del proceso previo de diseño de IKAL se plantearon preguntas HMW (How Might We) para orientar la ideación de la plataforma:

- ¿Cómo podríamos hacer que las artesanas publiquen sus bordados sin necesidad de conocimientos técnicos avanzados?
- ¿Cómo podríamos generar confianza entre compradores que no conocen a la artesana en persona?
- ¿Cómo podríamos hacer que cada compra se sienta como una conexión cultural, no solo una transacción?
- ¿Cómo podríamos facilitar los pagos en línea para compradores y artesanas en zonas con acceso limitado a bancos?
- ¿Cómo podríamos ayudar a las artesanas a contar la historia detrás de cada pieza?

Estas preguntas sirvieron como antecedentes para definir algunas de las funcionalidades y características de IKAL.

---

# Etapa 2. Entidades, atributos, fuentes y diccionario de datos

## 2.1 Entidades principales

| Entidad | Descripción |
|---|---|
| Artesano | Persona que se registra y comercializa sus productos en IKAL. |
| Producto | Artesanía publicada dentro de la plataforma. |
| Cliente/Comprador | Persona que consulta y adquiere productos. |
| Pedido | Compra realizada por un cliente. |
| Detalle del pedido | Productos y cantidades incluidos en cada pedido. |
| Categoría | Clasificación de los productos, como ropa o accesorio. |
| Pago | Información relacionada con el pago de un pedido. |

---

## 2.2 Atributos principales

### Artesano

- `id_artesano`
- `nombre`
- `localidad`
- `fecha_registro`
- `estado_usuario`

### Producto

- `id_producto`
- `id_artesano`
- `nombre_producto`
- `categoria`
- `tipo_bordado`
- `color`
- `tipo_producto`
- `precio`
- `stock`

### Cliente

- `id_cliente`
- `nombre`
- `fecha_registro`

### Pedido

- `id_pedido`
- `id_cliente`
- `fecha_pedido`
- `total`
- `estado_pedido`

### Detalle del pedido

- `id_detalle`
- `id_pedido`
- `id_producto`
- `cantidad`
- `precio_unitario`
- `subtotal`

### Pago

- `id_pago`
- `id_pedido`
- `fecha_pago`
- `metodo_pago`
- `monto`
- `estado_pago`

---

## 2.3 Fuentes de datos

Debido a que IKAL es un proyecto de reciente creación y actualmente no cuenta con un historial amplio de operaciones, se utilizarán datos simulados para representar de manera lógica el funcionamiento del negocio.

| Fuente | Tipo | Uso |
|---|---|---|
| Dataset de artesanos | Simulado | Información de artesanos y localidades. |
| Dataset de productos | Simulado | Productos, categorías, características y precios. |
| Dataset de clientes | Simulado | Información básica de compradores. |
| Dataset de pedidos | Simulado | Pedidos, fechas e importes. |
| Dataset de detalle de pedidos | Simulado | Productos y cantidades de cada pedido. |
| Dataset de pagos | Simulado | Información de pagos y métodos utilizados. |
| Sitio web de IKAL | Sistema local | Representación de las operaciones y funcionalidades de la plataforma. |

---

## 2.4 Diccionario de datos

Esta sección se completará con base en las columnas definitivas de los datasets utilizados en el proyecto.

---

# Organización del repositorio

El proyecto se organizará de acuerdo con el tipo de recurso:

```text
IKAL/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── simulation/
│   └── etl/
│
├── dashboards/
│
├── docs/
│
├── tests/
│
├── README.md
└── requirements.txt
