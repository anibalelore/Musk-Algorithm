# Guía de auditoría técnica y repositorios

## Inspección inicial (solo si hay acceso)

- Comprender README, estructura, scripts, tests, esquema de datos, endpoints, colas, workers y proveedores externos.
- Identificar rutas duplicadas, capas de abstracción sin consumidores, configuraciones obsoletas, múltiples fuentes de verdad y trabajo manual innecesario.
- Relacionar archivos y módulos con un resultado del usuario; no llamar «código muerto» sin comprobar usos dinámicos, jobs, flags, clientes externos y migraciones.

## Aplicación del algoritmo

1. **QUESTION:** para cada arquitectura/requisito, documentar constraint, amenaza, consumidor y propietario.
2. **DELETE:** comparar eliminar función, reutilizar componente, desacoplar dependencia o fusionar servicios. Buscar pruebas de uso y referencias.
3. **SIMPLIFY:** preferir interfaces y datos suficientes a abstracciones excesivas; disminuir estados, esquemas y rutas duplicadas.
4. **ACCELERATE:** perfilar latencia, pipelines, build, test, despliegue y feedback; optimizar cuello de botella real.
5. **AUTOMATE:** automatizar checks, pruebas, formateo, migraciones seguras y tareas repetibles cuando el flujo esté estabilizado.

## Protocolo de cambios

- Antes de modificar, presentar diffs/alcance cuando el usuario pidió solo auditoría.
- Para cambios autorizados, trabajar con pasos pequeños, tests y compatibilidad hacia atrás.
- No eliminar una tabla/campo/evento de producción solo por falta de referencias en el código; verificar datos históricos, consumidores externos, políticas de retención y obligaciones.
- Usar patrón expand/contract cuando se necesiten migraciones incompatibles.
- Verificar backups, rollbacks, auditoría y monitoreo antes de retiros irreversibles.
- Distinguir «no encontré uso» de «no se utiliza».

## Entregable técnico sugerido

| Componente | Evidencia (ruta/uso) | Estado | Cambio | Riesgo | Tests | Reversión |
|---|---|---|---|---|---|---|

**Sin acceso a repositorio:** entregar auditoría conceptual, marcar toda suposición y solicitar rutas solo si son imprescindibles para implementar.
