# Etapa 3. Diseño y simulación estratégica del dataset

## 3.1 Reglas de negocio incorporadas

El dataset simula **3 años de operación** de IKAL (agosto 2023 – agosto 2026), con
reglas de negocio explícitas para que el comportamiento sea lógico y no aleatorio.

### Crecimiento de la plataforma
Como IKAL es un proyecto nuevo, la simulación refleja una **plataforma en crecimiento**:

| Elemento | Comportamiento simulado |
|---|---|
| Artesanos | Crecen de forma gradual, de pocos registros en 2023 a 60 en 2026 |
| Compradores | Crecen de forma más acelerada (típico de e-commerce), llegando a 900 |
| Productos | El catálogo aumenta con el tiempo: 30 Marca IKAL + 120 de artesanos |
| Ventas | Aumentan año con año: de apenas 67 en 2023 (arranque) a más de 1,600 en 2025 |

### Estacionalidad
Las ventas no son iguales todos los meses; se aplicó un factor de demanda según la
temporada, consistente con el contexto cultural mexicano:

| Periodo | Factor de demanda | Motivo |
|---|---|---|
| Noviembre–Diciembre | ×2.4 | Día de Muertos y temporada navideña |
| Mayo | ×1.8 | Día de las Madres |
| Enero–Febrero | ×0.6 | Temporada baja post-navideña |
| Resto del año | ×1.0 | Demanda base |

### Catálogo y precios
6 categorías (Playera, Bolsa, Aretes, Accesorio, Bordado, Blusa), cada una con un
rango de precio propio y un costo de producción entre 35% y 42% del precio de venta,
según la categoría — así se puede calcular utilidad real por producto.

### Canales y método de pago
Las ventas se distribuyen en 4 canales (Web, Instagram, Facebook, WhatsApp) y 2
métodos de pago (Crédito, Débito), con Web como canal principal.

## 3.2 Relaciones coherentes garantizadas

Estas reglas se validan matemáticamente en el propio script de generación:

- Ningún producto puede venderse antes de que su artesano se haya registrado.
- Ningún producto artesanal puede existir antes de la fecha de registro de su artesano.
- Ninguna venta puede ocurrir antes de que el comprador se haya registrado.
- El campo `total` de cada venta siempre es igual a `precio_venta × cantidad`.
- El costo de un producto siempre es menor que su precio de venta.
- Los totales de `num_compras`/`total_gastado` de cada comprador, y de
  `ingresos_generados` de cada artesano, se calculan **a partir de las ventas reales**,
  no se inventan por separado.

## 3.3 Problemas de calidad introducidos intencionalmente

Para poder demostrar el proceso de ETL (Etapa 4), se generó también una versión
"cruda" (`data/raw/`) con defectos de calidad controlados y documentados:

| Defecto | Tabla afectada | Cantidad |
|---|---|---|
| Valores nulos en ubicación | compradores | 2 registros |
| Registros duplicados | ventas | 3 registros |
| Categorías con mayúsculas inconsistentes | productos | 4 registros |
| Fechas en formato mixto (DD/MM/YYYY) | ventas | 5% de los registros |
| Nombres con espacios extra | artesanos | 3 registros |

Estos defectos se corrigen en el proceso ETL (ver Etapa 4), y la versión limpia se
guarda en `data/processed/`.

## 3.4 Reproducibilidad

El script usa semillas fijas (`np.random.seed(2026)` y `Faker.seed(2026)`), por lo que
ejecutarlo de nuevo produce exactamente el mismo dataset.

```bash
python src/simulation/generar_dataset.py
```

**Resultado de la última ejecución:**
- Artesanos: 60 (40 Xicotepec + 20 Pantepec)
- Compradores: 900
- Productos: 150 (30 Marca IKAL + 120 Artesano)
- Ventas: 3,614 (2023: 67 · 2024: 874 · 2025: 1,658 · 2026: 1,015)
- Ingreso total generado: $2,588,255.55 MXN
- Utilidad total generada: $1,566,814.17 MXN
