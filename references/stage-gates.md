# Smart Stage Gate Manager

Cerrar cada etapa con seis bloques: **resumen, resultados, decisiones aprobadas/propuestas, riesgos/evidencia faltante, recomendación y confirmación**.

Por defecto, recomendar la siguiente etapa y pedir una confirmación: avanzar, profundizar o revisar. Mientras se espera, no continuar preguntas ordinarias. Tras «avancemos», comenzar el análisis siguiente sin otra autorización metodológica.

`auto_advance_enabled=true` permite producir entregables sin pausas, pero jamás concede lectura, edición, eliminación, piloto o producción.

| Etapa | Gate mínimo | Siguiente |
|---|---|---|
| QUESTION | Tres informes, suficiencia e incertidumbres | DELETE |
| DELETE | Matriz de candidatos, controles protegidos, pendientes | SIMPLIFY |
| SIMPLIFY | Antes/después y arquitectura mínima | ACCELERATE |
| ACCELERATE | Baseline/plan, experimento y candidatos estables | AUTOMATE |
| AUTOMATE | Decisión y DESIGN/BUILD/PILOT/HANDOFF con evidencia | Cierre/iteración |

Una transición no cambia aprobaciones ni permisos técnicos.
