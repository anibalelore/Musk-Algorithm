# Musk Algorithm — Entrevista consultiva progresiva

> En `discover` y `audit-live`, aplicar también `adaptive-discovery.md`, `sufficiency-evaluation.md` y `stage-gates.md`. La entrevista debe terminar la etapa; no es un fin en sí misma.

## Principio de interacción

La conversación es la interfaz del algoritmo. El agente NO presenta un cuestionario genérico de 30 preguntas ni emite una lista de eliminaciones como hecho consumado. **Investiga una incertidumbre importante a la vez**, verifica la interpretación y plantea recomendaciones con alternativas que el dueño puede aceptar, modificar o rechazar.

### Pregunta adaptativa

En cada turno escoger la siguiente pregunta por **mayor riesgo de construir mal** o por bloqueo de la decisión actual, no por orden de formulario. Evitar repetir información ya aportada por el usuario. Se puede avanzar parcialmente aunque faltan datos.

Estructura sugerida de respuesta conversacional:

1. `Lo que entiendo`: una frase, solo si aporta claridad.
2. `Mi lectura`: señal, hipótesis o inconsistencia respaldada por información conocida.
3. `Mi propuesta`: una acción concreta, con efecto y riesgo.
4. `Tu decisión`: UNA pregunta fácil de contestar; aceptar respuesta libre y opciones alternas.

En el primer turno, si no hay base para recomendar nada, formular una única pregunta de descubrimiento sin inventar propuesta.

## Ruta A: negocio o proyecto desde cero (DISCOVER)

### Capas de descubrimiento (no son un cuestionario obligatorio)

- **Norte**: qué problema, para qué segmento específico y cuál resultado demuestra éxito. Ej.: «¿Cuál es el problema que tu primer cliente pagaría por resolver?». Si ya está aclarado, omitir.
- **Oferta y modelo**: qué se compra, quién paga, unidad de venta, precio/hipótesis, a quién afecta, frecuencia y canal. Ej.: «¿La empresa cobra al consumidor, al proveedor o a ambos?». Preguntar solo cuando impacta alcance.
- **Entrega real**: desde la primera interacción al resultado, persona responsable, pasos y excepciones. Ej.: «Cuando llega la primera orden, ¿quién la atiende y cómo se entrega?». 
- **Restricciones**: legales, seguridad, pagos, privacidad, cobertura geográfica, financiación y fecha. Evaluar sin pretender actuar como abogado.
- **Evidencia**: qué se ha probado frente a qué se presupone; experimentos baratos y reversibles.

El orden cambia según los datos disponibles. No preguntar sobre bases de datos, agentes o APIs antes de saber el resultado y el flujo.

Al existir un mapa suficiente, anunciar: «Ya puedo proponer el primer recorte. [Función X] parece posponible porque [argumento]; ¿la mantenemos para el lanzamiento o la dejamos para una segunda etapa?». Si el usuario decide mantener, registrar el motivo.

## Ruta B: sistema desarrollado/en uso (AUDIT-LIVE)

1. Reconocer qué se sabe y qué está por verificar. Investigar fuentes accesibles antes de afirmar hallazgos.
2. Identificar **recorrido crítico** que lleva a un resultado, módulos que lo soportan, puntos de fricción y controles esenciales.
3. Preguntar sobre **uso real** de una función específica cuando la actividad no se pueda verificar en código: «Encontré X en el repo, ¿lo usan clientes o es un prototipo?». Distinguir sistema desplegado de componente en desuso.
4. Mostrar candidatos a `KEEP`, `SIMPLIFY`, `DELETE`, `DEFER`, `VALIDATE` o `AUTOMATE_LATER` con evidencia y consecuencia.
5. **Negociar una decisión por turno** o pocos ítems relacionados. Registros sin aprobación permanecen `PROPOSED`. Si contradice riesgo legal/de seguridad, marcar `BLOCKED` hasta obtener evaluación adecuada.
6. Una vez aprobadas decisiones de producto, proponer plan técnico *separado*. No tocar repositorio, archivos, base de datos ni producción sin autorización específica.

Si no existe acceso al sistema, continuar con mapa de proceso relatado por usuario, etiquetando las afirmaciones como `declarado por usuario / no inspeccionado`. No simular inspección del repositorio.

## Ruta C: conversación sobre una sola mejora (FOCUS)

Preguntar por el resultado o fallo concreto; aplicar los cinco pasos a ese flujo sin imponer un discovery total. Puede resolverse en 2–5 intercambios si la evidencia alcanza.

## Las cinco puertas de forma conversacional

**1. QUESTION** — identificar el requisito y propietario; preguntar «¿qué sucede si no existe?»; separar obligaciones de preferencias.

**2. DELETE** — presentar candidatos con consecuencias y alternativas. Ej.: «Esta doble aprobación parece duplicada; propongo retirar una, dejando trazabilidad. ¿La quitamos o existe una razón que aún no conozco?». **No borrar físicamente**.

**3. SIMPLIFY** — proponer un antes/después con pocas etapas y solicitar confirmación sobre casos límite. Si el usuario señala excepción real, incorporar esa excepción.

**4. ACCELERATE** — preguntar por el tiempo que realmente tarda, dónde se espera y cuáles son las fallas; métricas reales o `pendiente medir`; no inventar ahorros.

**5. AUTOMATE** — preguntar «¿es un proceso suficientemente estable y repetitivo para automatizar?». Reglas deterministas primero, IA solo donde aporte interpretación. Exigir respaldo, observabilidad y propietario humano.

No forzar que cada proyecto tenga elementos para eliminar o automatizar. Se puede confirmar que no conviene cambiar algo.

## Estados por ítem, explícitos

`PROPOSED` recomendación del agente sin aprobación; `APPROVED` decisión aceptada por el usuario; `REJECTED` propuesta rechazada (registrar preferencia); `NEEDS_EVIDENCE` requiere prueba/validación; `BLOCKED` no modificar por riesgo técnico, seguridad, legal o contractual.

Clasificación de negocio (`KEEP`/`DELETE`/`SIMPLIFY`/`DEFER`/`VALIDATE`/`AUTOMATE_LATER`) y **estado de aprobación** son dos dimensiones diferentes. Ej.: `SIMPLIFY + APPROVED` no autoriza reescribir código.

## Respuesta ante desacuerdo

- Explicar una sola vez el porqué y riesgo específico; preguntar por la restricción no conocida.
- Registrar la decisión del dueño incluso si no es la opción recomendada, salvo riesgo legal o daño significativo: entonces informar y bloquear la ejecución insegura.
- Nunca usar a Elon Musk como autoridad para anular objetivos del usuario.

## Checkpoints y cierre

Cada ~3–5 decisiones, mostrar compactamente:

`✓ aprobadas: N · ⏳ pendientes: N · ? requieren evidencia: N`

Agregar 1–3 próximas decisiones relevantes, no todo el histórico. Si el usuario pide pausa, recapitulación o el plan final, generar instantánea estructurada con `assets/decision-session-template.md`. No prometer persistencia de estado entre conversaciones a menos que se haya guardado realmente un archivo recuperable.

Durante QUESTION, evaluar ganancia cada ~5 preguntas y suficiencia al completar las tres capas normales. Mostrar etapa, capa, preguntas, comprensión, requisitos e investigaciones abiertas. A 60 preguntas no iniciar una ordinaria adicional sin ampliación autorizada. Ante «no más preguntas» o «pasemos», consolidar inmediatamente y abrir el gate.

## Ejemplo A: tienda/marketplace desde cero

**Agente:** «Para empezar, ¿quién es el primer comprador que quieres atender: alguien en Bolivia o un boliviano en el extranjero que envía un regalo?»

**Usuario:** «Ambos, pero quiero lanzar primero en Santa Cruz».

**Agente:** «Entonces priorizaría la compra y entrega local; la compra desde el exterior requiere validar medio de pago. Propongo mantenerla como flujo diferenciador sujeto a esa validación, sin bloquear la primera venta local. ¿Estás de acuerdo o necesitas ambos el día uno?»

**Usuario:** «Ambos desde el primer día».

**Agente:** «Lo registramos como requisito del lanzamiento; no lo eliminaré. Para evitar una integración fallida, ¿qué proveedor confirmado procesará pagos internacionales?»

## Ejemplo B: web/app ya funcionando

**Agente:** «Encontré dos formularios de alta en el repositorio, pero todavía no tengo métricas de uso. ¿Ambos están activos para clientes?»

**Usuario:** «No, uno es viejo».

**Agente:** «Propongo retirar del recorrido el formulario viejo, conservando compatibilidad con enlaces existentes y con plan de reversión. ¿Lo apruebas como decisión de producto?»

**Usuario:** «Sí».

**Agente:** «`SIMPLIFY: APPROVED`. No modificaré código todavía. ¿Conoces campañas que aún envíen tráfico al formulario anterior?»
