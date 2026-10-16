# Paso 5 — Diseño, construcción y verificación de automatizaciones

> **Regla:** primero decidir si el trabajo debe existir. La skill es portátil e independiente: no instala servicios, no incorpora runtime propio ni ejecuta acciones en sistemas externos por arte de magia. El agente anfitrión utiliza únicamente herramientas a las que efectivamente tenga acceso.

## 0. Activación y continuidad

- Entrar solo después de QUESTION, DELETE, SIMPLIFY y ACCELERATE, o documentar que el usuario trae evidencia previa suficiente de esas puertas.
- Obtener del registro de decisiones el proceso sobreviviente, la métrica objetivo, los riesgos y el dueño. Si el proceso todavía es incierto, volver a VALIDATE.
- Mostrar en pocas líneas un candidato concreto y el **mínimo** de preguntas críticas pendientes. La entrevista sigue siendo interactiva: una pregunta prioritaria por turno.
- No imponer automatización cuando el flujo manual es suficientemente simple o barato.

## 1. Elegibilidad `AUTOMATE_NOW`

Comprobar y registrar en `assets/automation-blueprint.md`:

1. ¿El proceso sobrevivió a la eliminación y simplificación?
2. ¿Disparador, entradas, outputs y casos excepcionales están claros?
3. ¿Existe propietario del proceso, métricas de línea base y beneficio medible o experimento de validación?
4. ¿Existen datos fiables, permisos legítimos y vía técnica factible (API, webhook, BD o UI permitida)?
5. ¿El sistema acepta reintentos, duplicados, fallos y reversión sin generar daño?
6. ¿Se definieron revisión humana y controles aplicables a pagos, identidad, seguridad y datos sensibles?

Resultado: `AUTOMATE_NOW`, `VALIDATE_FIRST`, `KEEP_MANUAL` o `SIMPLIFY_AGAIN`, con motivo. Estimaciones se etiquetan como tales.

## 2. Escalera tecnológica (elige la menor complejidad suficiente)

1. **Eliminar trabajo por diseño**: precarga o reutilización de datos, cambio de procedimiento, mejor UX.
2. **Configuración existente**: opciones nativas en ERP, CRM, PSP o plataforma.
3. **Reglas/eventos**: trigger, máquina de estados, plantillas, SQL, colas.
4. **Integración API/webhook**: autenticación, firma, idempotencia y reconciliación.
5. **Script o job**: batch para reglas estables; cron solo si evento no está disponible.
6. **RPA/control UI**: únicamente cuando esté permitido y no haya API razonable; prever fragilidad de interfaz.
7. **IA/LLM/agentes**: cuando se requiera interpretación no determinista, con pruebas de evaluación, umbrales, revisión humana y audit trail.

**No invocar agentes para mover campos de A a B si un webhook resuelve el problema.** No afirmar disponibilidad de un servicio externo sin verificarla.

## 3. Diseño obligatorio (BLUEPRINT)

Completar `assets/automation-blueprint.md` con:

- objetivo / alcance / proceso manual anterior y nuevo / condición de activación;
- disparador, esquema de entrada, validación, esquema de salida y efectos externos;
- sistemas, permisos, secretos, llamadas o integraciones realmente disponibles y faltantes;
- estados, deduplicación, idempotencia, timeout, reintentos, backoff, cola de excepciones;
- fallos, quién los resuelve, reversión, privacidad, logs y alarmas;
- pruebas felices, duplicados, fuera de orden, maliciosos o inválidos, reanudación y manual fallback;
- métricas antes/después, umbrales de aceptación y costo operativo aproximado con supuestos claros;
- decisión humana explícita y nivel de ejecución permitido.

Si existe una alternativa simple sin IA, recomendarla incluso cuando el usuario diga “quiero un agente”, explicando el trade-off.

## 4. Implementación real (BUILD)

**Solo con acceso al proyecto y aprobación de edición.** Conservar arquitectura, stack, convenciones, esquema de datos y tests existentes. No introducir frameworks por preferencia propia.

Secuencia:

1. Inventariar archivos y interfaces implicadas; verificar rama y cambios pendientes del usuario; no sobrescribir trabajo ajeno.
2. Escribir un plan corto de cambios: rutas, tablas o migrations, servicios, eventos, permisos, pruebas.
3. Implementar el camino feliz *y* protección contra duplicados, reintentos y acciones repetidas. Usar transacciones y callbacks verificables cuando corresponda.
4. Crear pruebas unitarias, integración con dobles cuando API externa no está conectada, y casos de fallo. Los mocks no demuestran disponibilidad real.
5. Ejecutar comprobaciones disponibles y reportar resultados exactos, rutas modificadas y límites. Si el host no tiene ejecución de comandos, reportar `código propuesto sin pruebas ejecutadas`.
6. Pedir permiso separado antes de aplicar migraciones irreversibles, tocar producción, conectar cuentas, activar notificaciones reales o generar cargos. Cambios sensibles requieren preflight, backup y reversión probados cuando sean posibles.

Nunca escribir sin permiso ni afirmar «automatización funcionando» si solo se redactó código. La skill no crea autorizaciones ni credenciales.

## 5. Prueba controlada (PILOT) y despliegue

- Preparar entorno de prueba/staging, sandbox de proveedor o datos de prueba. No usar pagos reales para pruebas salvo autorización formal y controles apropiados.
- Validar casos: normal, duplicado, repetido, retrasado, evento fuera de orden, fallo de proveedor, caída de red, datos incompletos, rollback.
- Ejecutar piloto acotado solo con permiso. Medir éxito/tiempo/errores/costo y comparar con línea base; si no hay muestras suficientes, declarar provisional.
- Activación en vivo separada; definir propietario, alertas, runbook, botón de pausa y procedimiento manual si falla.
- Después, revisión del ciclo: ¿la automatización añadió complejidad o un paso inútil? Si sí, volver a etapas 1–3.

## 6. Sin acceso, capacidades o autorizaciones (HANDOFF)

Completar `assets/automation-handoff.md`: flujo en lenguaje simple, arquitectura recomendada, pseudocódigo o código listo para integración cuando sea viable, contratos, tests y criterios de aceptación, lista explícita de conectores/credenciales faltantes y preguntas puntuales para un responsable. Puede entregarse a Claude Code, Codex, un desarrollador o equipo interno. No requiere ORE Skill ni ningún otro sistema especializado.

## 7. Ejemplos de política de implementación

**Marketplace:** `pago_confirmado` debe provenir de evento **verificado** del proveedor de pagos o conciliación autorizada, no del texto de un email. A partir de confirmación durable, publicar un único evento de preparación/solicitud de despacho. Reintentos no duplican guías ni cargos. Si operador externo no tiene API, dejar tarea manual y estados auditables.

**Roadside EV:** solicitar proveedores candidatos verificados por cobertura/capacidad; solo asignar una unidad cuando el proveedor confirme aceptación; no publicar ETAs inventadas. Si existe peligro vial, ofrecer contacto humano/emergencia según el caso, no depender exclusivamente de IA.

## 8. Formato final según avance

```
Modo seleccionado: BLUEPRINT | BUILD | PILOT | HANDOFF
Decisión de automatización: AUTOMATE_NOW | VALIDATE_FIRST | KEEP_MANUAL | SIMPLIFY_AGAIN
Aprobación documentada: [alcance y sí/no]
Hecho y verificado: [evidencia de archivos/pruebas/ejecución]
Pendiente: [accesos, pruebas, aprobación, despliegue]
Métrica y condición de éxito: [baseline / objetivo / experimentos]
Próxima decisión del usuario: [una sola]
```
