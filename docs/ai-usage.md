# Uso Responsable de IA Generativa

Este documento registra el uso de IA generativa (Claude, Anthropic) en el desarrollo del proyecto IKAL, conforme a lo solicitado en la Etapa 14 de la guía.

## Herramienta utilizada
Claude (Anthropic), a través de la interfaz de conversación con capacidad de análisis de código y generación de archivos.

## Actividades apoyadas por IA

| Etapa | Actividad | Tipo de apoyo |
|---|---|---|
| 6 | Selección y justificación del método analítico | Propuesta de opciones, discusión de trade-offs, decisión final tomada por la integrante |
| 6 | Verificación de integridad de 3 versiones distintas del dataset compartido por el equipo | Código de validación (duplicados, referencias, consistencia matemática) ejecutado y revisado por la IA, resultados verificados manualmente por la integrante contra los archivos CSV originales |
| 6 | Cálculo de rentabilidad por artesano, comunidad y categoría | Código Python generado por la IA, ejecutado y con salidas revisadas antes de aceptarse |
| 7 | Definición del catálogo de KPI | Propuesta inicial de 6 KPI generada por IA; la integrante confirmó cuáles usar antes de calcular |
| 7 | Cálculo de valores de KPI y semáforos | Código Python generado por la IA |
| 11 | Redacción de README y documentación técnica | Estructura y redacción generadas por IA a partir de la información confirmada por la integrante; secciones dependientes de otras etapas se dejaron marcadas como pendientes en vez de inventarse |
| — | Guía paso a paso para subir archivos a GitHub vía interfaz web (sin terminal) | Instrucciones de uso de la herramienta, sin generar contenido del proyecto |

## Decisiones tomadas por el equipo (no por la IA)

- La elección del método analítico de la Etapa 6 (rentabilidad y equidad, en vez de RFM o pronóstico) fue decisión de la integrante, con la IA presentando opciones.
- La corrección del dataset (agregar columnas de costo/canal/estatus, corregir columnas de artesanos) fue solicitada y validada por el equipo tras detectar el problema en conjunto con la IA.
- El tratamiento de "Marca IKAL" como referencia comparativa y no como un artesano más fue una decisión discutida explícitamente con la integrante antes de aplicarse en el análisis.
- Los umbrales de meta/alerta del catálogo de KPI fueron propuestos por la IA con base en los objetivos de negocio declarados por el equipo, sujetos a revisión del equipo completo.

## Errores detectados y corregidos durante el proceso

- Una primera versión del dataset extendido a 3 años (compartida por una integrante) resultó tener solo redistribución de fechas sin aumento real de volumen — se detectó por conteo directo de registros por año y se solicitó una nueva versión.
- Una segunda versión reportada como "0 errores, 3,614 ventas reales" fue verificada de forma independiente con código antes de aceptarse como base de trabajo, en vez de confiar en el reporte de otra sesión de IA.

## Validaciones aplicadas

Todo resultado numérico presentado en las Etapas 6 y 7 fue calculado directamente sobre los archivos CSV finales del equipo (no inventado ni estimado), con verificación de integridad referencial y consistencia matemática antes de su uso.
