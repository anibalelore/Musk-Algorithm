# Ejemplos ilustrativos: no son auditorías de producción

Estos escenarios son ejemplos didácticos de cómo aplicar la metodología. No confirman estado real de software, proveedores, normas, ingresos ni cobertura.

## Escenario A · VOLTRIVA (red de asistencia EV)

**Resultado protegido:** conductor que necesita ayuda consigue asistencia real y confiable; el proveedor completa el servicio y recibe pago correctamente.

1. QUESTION: ¿Es obligatorio crear cuenta antes de buscar una grúa? ¿Existe disponibilidad real en la zona? ¿Quién certifica esa cobertura? ¿Por qué se quieren cinco dashboards?
2. DELETE: retirar registro previo a búsqueda si no es necesario y reemplazar pantallas redundantes de selección de asistencia por una entrada unificada.
3. SIMPLIFY: buscar → mostrar proveedores verificados/condiciones → confirmar → seguir → resolver. Mantener verificación, seguridad vial, consentimiento y pago donde corresponda.
4. ACCELERATE: medir tiempo hasta opción útil, tiempo hasta aceptación y tiempo de resolución; distinguir consulta de servicio completado.
5. AUTOMATE: evento de confirmación, notificaciones y matching condicionado por disponibilidad. Un LLM puede interpretar lenguaje libre, **no** inventar ETA ni reemplazar despacho autorizado.

**Clasificación:** buscador = KEEP; onboarding excesivo = SIMPLIFY/DELETE; expansión sin partners = DEFER; agente autónomo de rescate = AUTOMATE_LATER/VALIDATE.

## Escenario B · eQatu (marketplace boliviano)

**Resultado protegido:** compra pagada legítimamente, vendedor procesa, entrega comprobable y cierre confiable.

1. QUESTION: ¿Qué atributos necesita un vendedor para publicar? ¿Cuáles son obligaciones regulatorias? ¿Qué pagos y operadores logísticos están realmente habilitados?
2. DELETE: evitar doble digitación entre pedido y envío; retirar campos no necesarios en la primera publicación, preservando verificaciones exigidas.
3. SIMPLIFY: buscar → decidir → pagar → despacho → entrega. El comprador en el extranjero puede indicar destinatario en Bolivia si existe aceptación efectiva de pagos.
4. ACCELERATE: medir tiempo hasta primera publicación, tasa de pago confirmado, despacho y entrega.
5. AUTOMATE: crear solicitud de envío a partir del pedido y actualizar estados mediante eventos confirmados. IA para ayudar con fichas de producto si existe revisión de precisión.

**Clasificación:** checkout y pedido = KEEP; doble ingreso logístico = DELETE; logística propia de cobertura nacional no validada = DEFER; retargeting masivo por IA = AUTOMATE_LATER.

## Escenario C · Empresa con proceso manual

El usuario dice «quiero un agente para copiar datos de una aplicación a otra cada lunes».

- QUESTION: ¿Cuál es la fuente de verdad? ¿Por qué necesitan ambas copias?
- DELETE: proponer retirar el reporte duplicado si nadie lo usa.
- SIMPLIFY: una única consulta que calcule KPI de la misma fuente.
- ACCELERATE: generación después del cierre de datos y publicación sin transcribir.
- AUTOMATE: programar reporte **solamente** cuando la definición del KPI y la calidad de los datos estén verificadas.

Una respuesta correcta puede ser «no necesitas agente, necesitas eliminar un reporte».
