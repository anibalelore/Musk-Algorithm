# Musk Algorithm — Auditoría de sistemas existentes (sin cambios automáticos)

## Alcance verificable

Cuando el usuario aporta repo, proyecto abierto, documentación o credenciales, examinar **solo lo que el host y el usuario autorizan**. Si un recurso no está disponible, pedir acceso específico o continuar por entrevista de funcionamiento. No declarar «auditado en producción» un sistema revisado solo a nivel de código.

### Triaje inicial de fuentes

| Fuente | Qué puede probar | Qué no prueba por sí sola |
|---|---|---|
| Repositorio | Componentes, rutas, reglas, dependencias y tests escritos | Que se usa así en producción |
| Pantallas y demos | Recorrido visible, textos y fricción UI | Cobertura y rendimiento real |
| SOP/documentación | Proceso previsto y obligaciones declaradas | Que se cumple fielmente |
| Logs/telemetría autorizados | Eventos y fallos de periodos observados | Experiencia completa del cliente |
| Base de datos/estadísticas | Patrones agregados y estados almacenados | Motivos de negocio sin entrevistas |
| Entrevistas | Intención, decisiones y prácticas actuales | Métricas exactas sin validación |

No obtener ni mostrar PII innecesaria; preferir agregados. No solicitar contraseñas, tokens o volcados de datos sensibles.

## Procedimiento de lectura

1. Identificar resultado comercial y flujo crítico: alta → operación → entrega de valor → pago (o el orden que aplique).
2. Inspeccionar inventario relevante: entry points, rutas, frontend, APIs, worker/colas, tablas/migraciones, integraciones, pagos, permisos, tests, despliegues. Evitar leer toda la base de código sin propósito.
3. Marcar los módulos como `evidencia: código`, `evidencia: comportamiento observado`, `declarado` o `hipótesis`. No inferir uso o ganancias de existencia de archivos.
4. Detectar duplicidad, transferencias manuales, aprobaciones no justificadas, pantallas sin uso probado, inconsistencias de estados, tareas repetitivas, llamadas API redundantes y costos no medidos.
5. Revisar seguridad, privacidad, cumplimiento, facturación, integridad de datos, rollback e impacto de terceros antes de proponer recortes.
6. Elaborar 3–5 hallazgos **priorizados**, cada uno con evidencia, beneficio esperado, incertidumbre y costo/riesgo. **Conversar una decisión por turno**: recomendar, confirmar, registrar.
7. Tras acordar qué mantener/eliminar, crear un plan por lotes reversibles con tests y posibles migraciones. Separar aprobación del plan de permiso para ejecutarlo.

## Preguntas técnicas contextuales (solo si hacen falta)

- «¿Este módulo está desplegado en producción o solo está en staging?»
- «¿Qué porcentaje de operaciones realmente pasa por este formulario?» (si no existe métrica, dejar pendiente)
- «¿Hay integraciones externas que dependan de esta ruta?»
- «¿Quién aprueba y audita estos pagos?»
- «¿Cuál fue la última incidencia relacionada con este paso?»

## Riesgos en servicios ya operativos

- **No eliminar** credenciales, registros legales, consentimientos, conciliaciones, auditoría, controles antifraude, backups, componentes de seguridad física o supervisión necesarios.
- **No tomar silencio como aprobación** de eliminar endpoints, tablas, jobs o módulos.
- Planear impacto en datos históricos, enlaces externos, clientes activos, integraciones, migraciones y trazabilidad.
- Preferir desactivar detrás de feature flag o mediante experimento gradual si conviene; con observabilidad y plan de reversión.
- Acciones externas (desplegar, enviar correos, cancelar proveedores, ejecutar cobros) necesitan permiso independiente.

## Resultado de la auditoría

Un mapa `estado actual → estado acordado` que distinga `observado`, `informado por el dueño` y `propuesto`, decisiones con estado y los experimentos que confirmarían los ahorros. Solo entregar diagnóstico final completo al concluir las decisiones o si el usuario lo pide.
