# Etapa 2. Entidades, atributos, fuentes y diccionario de datos

## 2.1 Entidades principales

> **Nota de diseño:** el modelo original consideraba 7 entidades (Artesano, Producto,
> Cliente, Pedido, Detalle del pedido, Pago, Categoría). Durante la fase de simulación
> del dataset se consolidaron Pedido, Detalle del pedido y Pago en una sola tabla
> `ventas`, ya que en IKAL cada registro de venta corresponde a un producto, un
> comprador y un pago en una sola transacción. Esta simplificación reduce la
> complejidad del modelo sin perder información analítica relevante.

| Entidad | Descripción |
|---|---|
| Artesano | Persona que se registra y comercializa sus productos en IKAL. |
| Producto | Artesanía publicada dentro de la plataforma (propia o de artesano). |
| Comprador | Persona que consulta y adquiere productos. |
| Venta | Transacción que registra producto, comprador, pago y estado en un solo evento. |

## 2.2 Clasificación de los datos

Conforme a la guía del proyecto, los datos utilizados en IKAL se clasifican de la
siguiente manera:

| Categoría | Clasificación | Justificación |
|---|---|---|
| Estructura | **Estructurados** | Los 4 datasets están organizados en tablas (filas y columnas) en formato CSV, con tipos de dato definidos por campo. |
| Temporalidad | **Históricos / almacenados** | Representan un periodo cerrado de 3 años (agosto 2023 – agosto 2026), no un flujo de datos en tiempo real. |
| Origen | **Simulados** | Generados con un script propio (Python + Faker + NumPy) con reglas de negocio explícitas, no provienen de una fuente externa real. |
| Acceso | **Privados de uso interno del proyecto** | No contienen datos personales reales; los nombres y correos son ficticios generados para fines académicos. |
| Estado de procesamiento | Dos versiones: **crudos** (`data/raw/`, con errores intencionales) y **procesados** (`data/processed/`, ya limpios tras el ETL) | Permite demostrar el proceso completo de calidad de datos (Etapa 4). |

**Nota:** no se utilizan datos semiestructurados (JSON, XML) ni no estructurados
(texto libre, imágenes) en esta fase, ya que el modelo de datos de IKAL se resuelve
completamente en formato tabular.

## 2.3 Atributos principales (columnas reales del dataset)

### Artesano — `artesanos.csv`

| Campo | Tipo | Descripción |
|---|---|---|
| artesano_id | Entero | Identificador único del artesano |
| nombre | Texto | Nombre completo |
| ubicacion | Texto | Xicotepec de Juárez o Pantepec |
| fecha_registro | Fecha | Fecha de alta en la plataforma |
| productos_publicados | Entero | Cantidad de productos activos del artesano |
| unidades_vendidas | Entero | Total de piezas vendidas de sus productos |
| ingresos_generados | Decimal | Suma de ingresos de sus productos |
| utilidad_generada | Decimal | Ingresos menos costo de producción |

### Producto — `productos.csv`

| Campo | Tipo | Descripción |
|---|---|---|
| producto_id | Entero | Identificador único del producto |
| nombre | Texto | Nombre del producto |
| tipo | Texto | "Marca IKAL" o "Artesano" |
| categoria | Texto | Playera, Bolsa, Aretes, Accesorio, Bordado, Blusa |
| artesano_id | Entero | Referencia al artesano (0 = Marca IKAL) |
| precio_venta | Decimal | Precio al público |
| costo | Decimal | Costo de producción |
| unidades_vendidas | Entero | Total vendido (calculado desde ventas) |
| ingreso_total | Decimal | Ingreso generado por el producto |
| utilidad_total | Decimal | ingreso_total − (costo × unidades_vendidas) |

### Comprador — `compradores.csv`

| Campo | Tipo | Descripción |
|---|---|---|
| comprador_id | Entero | Identificador único del comprador |
| nombre | Texto | Nombre completo |
| ubicacion | Texto | Ciudad de residencia |
| fecha_registro | Fecha | Fecha de alta en la plataforma |
| num_compras | Entero | Total de compras realizadas (calculado desde ventas) |
| total_gastado | Decimal | Suma gastada en la plataforma (calculado desde ventas) |

### Venta — `ventas.csv`

| Campo | Tipo | Descripción |
|---|---|---|
| venta_id | Entero | Identificador único de la venta |
| producto_id | Entero | Referencia al producto vendido |
| comprador_id | Entero | Referencia al comprador |
| ubicacion_comprador | Texto | Ubicación del comprador al momento de la venta |
| fecha_venta | Fecha | Fecha de la transacción |
| cantidad | Entero | Piezas compradas |
| metodo_pago | Texto | Crédito o Débito |
| total | Decimal | precio_venta × cantidad |
| tipo_producto | Texto | "Marca IKAL" o "Artesano" |
| canal | Texto | Web, Instagram, Facebook o WhatsApp |
| estatus | Texto | Entregado, Enviado, En preparación o Cancelado |



## 2.5 Diccionario de datos — reglas de validez

| Campo | Regla |
|---|---|
| *_id (todos) | Único, obligatorio, sin duplicados |
| fecha_registro (comprador) | Debe ser anterior a cualquier fecha_venta de ese comprador |
| costo | Siempre menor que precio_venta |
| total (ventas) | Debe ser igual a precio_venta × cantidad |
| artesano_id = 0 | Reservado exclusivamente para productos de Marca IKAL |
| metodo_pago | Solo "Crédito" o "Débito" |
| estatus | Solo "Entregado", "Enviado", "En preparación" o "Cancelado" |
