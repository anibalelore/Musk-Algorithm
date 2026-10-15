# Guía para automatizaciones y agentes IA

La etapa 5 no es sinónimo de usar LLM. El criterio es costo total, confiabilidad, auditabilidad y valor marginal.

## Puertas previas obligatorias

1. ¿Este paso realmente debe seguir existiendo tras las etapas 1–2?
2. ¿La entrada/salida y las excepciones están definidas?
3. ¿Hay proceso manual estable y un propietario que pueda validar decisiones?
4. ¿Se puede usar un evento/regla/SQL/API convencional en lugar de agentes?
5. ¿Qué fallos esperables existen? ¿Hay intervención humana, trazabilidad y rollback?

## Elegir tecnología

| Problema | Primero probar | Escalar a IA solo cuando... |
|---|---|---|
| Cambiar estado de pedido | Máquina de estados + eventos | Hay ambigüedad real a interpretar |
| Enviar confirmación | Event bus + plantillas | Se requiere comprensión contextual |
| Conciliar pagos | PSP/webhooks/ledger y reglas | Se necesita investigar excepciones con revisión |
| Extraer información semiestructurada | Parser/OCR + validación | Variabilidad supera reglas y hay evaluaciones |
| Clasificar tickets | Taxonomía + reglas | Calidad de clasificación con IA supera baseline |
| Recomendar proveedores | Matching por cobertura/capacidad/datos | Hay datos confiables y mejora demostrada |

## Especificación mínima de automatización

- Trigger y garantías (at-least-once / deduplicación).
- Entradas, esquema, permisos, validaciones, salidas, side effects.
- Estados, reintentos, timeouts, circuit breaker y cola de excepciones.
- Auditoría, métricas, costos por transacción y privacidad.
- Guardrails: acciones de alto impacto requieren autorización, revisión y límites.
- Pruebas: casos normales, ambigüedades, duplicados, fallos, recuperación.

## Riesgos

Para pagos, seguridad vial, medicina, cumplimiento y decisiones que afecten derechos, no delegar aprobación irrevocable a un agente de IA sin controles expertos y autorización. Evitar prometer que un workflow es «autónomo» si requiere APIs, cuentas o aprobaciones aún no disponibles.

## Regla de decisión

`AUTOMATE_NOW` únicamente si flujo necesario + estable + entradas confiables + beneficio medible + fallas gestionables. En cualquier otro caso, recomendar `SIMPLIFY`, `VALIDATE` o `AUTOMATE_LATER`.
