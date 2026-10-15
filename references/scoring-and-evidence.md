# Evidencia, priorización y decisiones

Esta skill no depende de un índice mágico. Utilizar evidencia y restricciones primero; una puntuación auxiliar no decide sobre seguridad, leyes ni condiciones de lanzamiento.

## Escala opcional (0–3)

Cada criterio debe tener una nota y un fundamento documentado:

- Valor para el usuario (0 = ninguno, 3 = alto y verificado).
- Evidencia disponible (0 = hipótesis sin prueba, 3 = medición corroborada).
- Urgencia (0 = sin dependencia temporal, 3 = bloquea trabajo crítico).
- Costo/complexidad (0 = trivial, 3 = alto, como penalización).
- Riesgo de eliminación (0 = reversible/bajo, 3 = irreversible/alto).

Se puede mostrar un puntaje contextual, pero **nunca** sustituye la evaluación de cumplimiento/safety, ni usar un resultado arbitrario para ordenar toda la hoja de ruta.

## Registro de evidencia

| Elemento | Evidencia | Tipo | Fecha | Confianza | Dueño | Estado |
|---|---|---|---|---|---|---|
| ejemplo | Entrevistas con vendedores | Cualitativa | Pendiente | Baja | Producto | Hipótesis |

Tipos: analítica; observación; fuente de datos; requisito regulatorio verificado; contrato; declaración de usuario; hipótesis del equipo. Cuando falten fuentes, escribir expresamente «sin evidencia todavía».

## Condición para `DELETE`

Demostrar que el valor esencial se conserva, evaluar quién depende del paso, cuantificar costos de eliminación, probar reversión y registrar aprobación. En ausencia de acceso o evidencia: `VALIDATE`, no `DELETE` definitivo.

## Condición para `DEFER`

Indicar evento verificable: por ejemplo «activar cuando al menos X transacciones hayan demostrado demanda en un piloto», donde X se define con el usuario tras evaluar riesgo/costo, no se inventa como dato real.

## Antipatrones

- Eliminación por cuota («hay que borrar un 10 %»).
- Falsa precisión: «ahorrarás 72,4 %» sin baseline.
- Estimar cobertura de asistencia por presencia en mapa.
- Hacer del usuario un cuello de botella con aprobaciones innecesarias.
- Automatizar el trabajo inútil antes de preguntarse por qué existe.
