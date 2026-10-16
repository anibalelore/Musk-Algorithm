# Musk Algorithm

> **Skill independiente** para cuestionar requisitos, eliminar complejidad, simplificar procesos, acelerar ciclos y automatizar únicamente cuando tiene sentido.

**Identificador instalable:** `musk-algorithm`  
**Versión:** 1.3.0

**Idioma:** español por defecto, responde en el idioma del usuario  
**Formato:** [Agent Skills](https://agentskills.io/specification) (`SKILL.md`)  
**Licencia:** Apache License 2.0

**Dependencias:** ninguna para ejecutar la skill; Python 3.9+ solo para el instalador/validador opcional.

Esta implementación es **no oficial**; no está afiliada a Elon Musk, Tesla, SpaceX ni Everyday Astronaut. Su metodología toma como referencia la explicación de los cinco pasos durante el [recorrido de Starbase de 2021](https://everydayastronaut.com/starbase-tour-and-interview-with-elon-musk/).

## Qué hace

1. **QUESTION:** cuestiona requisitos y supuestos sin excepción.
2. **DELETE:** detecta partes, pasos o funciones prescindibles.
3. **SIMPLIFY:** minimiza la complejidad del proceso sobreviviente.
4. **ACCELERATE:** mide tiempos y elimina cuellos de botella.
5. **AUTOMATE:** automatiza solo cuando el proceso es útil, estable y verificable.

Primero conversa contigo para entender el negocio. Si ya hay un sistema, inspecciona las fuentes disponibles antes de emitir recomendaciones, luego **te pregunta qué mantener, simplificar, eliminar o posponer**. Solo después produce un diagnóstico con decisiones `KEEP`, `DELETE`, `SIMPLIFY`, `DEFER`, `VALIDATE` y `AUTOMATE_LATER`, flujos antes/después, riesgos y plan de ejecución. **En la fase 5**, puede diseñar un plano (`DESIGN`), implementar código con acceso y permiso (`BUILD`), validar un piloto (`PILOT`) o preparar un traspaso (`HANDOFF`). No modifica sistemas sin autorización. No depende de ORE Skill ni debe instalarse dentro de su repositorio.

## Estructura

```text
musk-algorithm/
├── SKILL.md                      # Instrucciones principales que lee el agente
├── agents/openai.yaml            # Metadatos opcionales para Codex
├── assets/audit-template.md      # Formato de auditoría
├── assets/decision-session-template.md  # Registro de decisiones y estado de conversación
├── assets/automation-blueprint.md      # Plano técnico verificable
├── assets/automation-handoff.md        # Traspaso sin acceso técnico
├── references/
│   ├── interactive-interview.md  # Entrevista guiada y aprobaciones
│   ├── adaptive-discovery.md     # Capas, suficiencia y límite de 60
│   ├── stage-gates.md            # Transiciones con confirmación
│   ├── automation-coordinator.md # DESIGN/BUILD/PILOT/HANDOFF
│   ├── chief-engineer-persona.md # Voz y conducta de revisión técnica
│   ├── live-system-audit.md     # Revisión basada en evidencia
│   ├── product-playbook.md
│   ├── operations-playbook.md
│   ├── engineering-playbook.md
│   ├── automation-playbook.md
│   ├── automation-execution.md  # Construir, probar y entregar
│   ├── scoring-and-evidence.md
│   └── examples.md
├── scripts/
│   ├── install.py                # Instalador opcional (Claude Code/Codex)
│   └── validate.py               # Validador básico
├── tests/                        # Pruebas de formato y simulación
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## Instalación rápida (local)

**1.** Descomprime el ZIP. Abre una terminal dentro de la carpeta `musk-algorithm`.

**2.** Instala en uno o ambos agentes, a nivel de usuario (disponible para todos tus proyectos):

```bash
python scripts/install.py --agent both --scope user
```

Para solo Claude Code:

```bash
python scripts/install.py --agent claude --scope user
```

Para solo Codex:

```bash
python scripts/install.py --agent codex --scope user
```

> En Windows, si `python` no existe, prueba `py`. La instalación no borra ni modifica otros paquetes de skills. Si `musk-algorithm` ya existe, se detiene: solo `--replace` permite respaldar la versión anterior y reemplazarla.

**3.** Abre una sesión nueva de Claude Code/Codex y pide: «Usa `musk-algorithm` para auditar el flujo de registro». En Claude Code, normalmente también puedes escribir `/musk-algorithm`.

### Instalación en un repositorio específico

```bash
python scripts/install.py --agent claude --scope project --project /ruta/a/mi-repo
python scripts/install.py --agent codex --scope project --project /ruta/a/mi-repo
```

Se instala en `.claude/skills/musk-algorithm/` (Claude) o `.agents/skills/musk-algorithm/` (Codex) de **ese repositorio**. Esto permite usar la skill independientemente de cualquier proyecto que contenga otros agentes.

### Instalación manual

Copia **toda** la carpeta `musk-algorithm/` a:

| Plataforma | Carpeta personal | Carpeta del proyecto |
|---|---|---|
| Claude Code | `~/.claude/skills/musk-algorithm/` | `.claude/skills/musk-algorithm/` |
| Codex | `~/.agents/skills/musk-algorithm/` | `.agents/skills/musk-algorithm/` |

En `claude.ai`, donde esté disponible la carga de skills personalizadas, importa el ZIP desde las opciones de personalización/Skills. La compatibilidad de carga de ZIP depende de las funciones habilitadas en la cuenta; no se instala desde este chat automáticamente.

## Qué incluye la versión 1.3

- **Chief Engineer Challenger:** personalidad original, directa y técnica que somete el proyecto a una revisión de primeros principios como si se defendiera ante un jefe de ingeniería excepcionalmente exigente. No suplanta ni imita literalmente a Elon Musk.
- **Adaptive Discovery Engine:** entrevista progresiva en tres capas normales —negocio, operación y arquitectura/reglas— y tres capas avanzadas opcionales.
- **Evaluación de suficiencia:** matriz de ocho dimensiones con escala 0–4 para decidir si conviene preguntar, investigar un bloqueo o avanzar.
- **Preguntas con límites inteligentes:** no impone una cuota mínima, revisa el rendimiento marginal y establece 60 preguntas como límite ordinario de QUESTION.
- **Smart Stage Gate Manager:** cada etapa termina con resumen, resultados, decisiones, riesgos, recomendación y confirmación para continuar.
- **Continuidad de sesiones:** conserva etapa, contador, evidencia y estados `APPROVED`, `REJECTED` y `NEEDS_EVIDENCE`, incluso en auditorías extensas.
- **Automation Architect & Implementer:** convierte oportunidades estables en `DESIGN`, `BUILD`, `PILOT` o `HANDOFF`, eligiendo la tecnología más sencilla adecuada.
- **Separación de permisos:** avanzar metodológicamente nunca concede permiso para editar, pilotear o desplegar.
- **Motor verificable sin dependencias:** `scripts/session_engine.py` permite comprobar suficiencia, transiciones, recuperación y elegibilidad de automatizaciones.
- **Pruebas conductuales:** simulan negocios pequeños y complejos, límite de preguntas, sesiones históricas y automatizaciones con o sin acceso técnico.
- **Demostraciones completas:** ejemplos desde QUESTION hasta AUTOMATE, auditoría de un sistema existente y recuperación de una sesión extensa.

### Cómo avanza el descubrimiento

QUESTION usa tres capas normales —negocio, operación, arquitectura/reglas— y hasta tres capas avanzadas solo con justificación y permiso. Una matriz 0–4 evalúa ocho dimensiones esenciales. No hay cuota mínima; a 60 preguntas se consolida el diagnóstico y cualquier ampliación requiere alcance y presupuesto nuevos.

Cada etapa termina con resultados, decisiones, riesgos y una recomendación. En modo interactivo se confirma una vez antes de avanzar; `auto_advance_enabled=true` automatiza transiciones metodológicas, nunca permisos técnicos. Una sesión guardada conserva contadores y estados históricos.

## Cómo funciona la conversación

La skill tiene dos entradas **sin dependencia de ORE**:

**A. Idea nueva:** escucha qué negocio quieres construir → descubre cliente, propuesta y operación a través de preguntas adaptadas → cuestiona requisitos → te propone qué conservar/eliminar/simplificar → **espera tus decisiones** → mide y propone automatización después.

**B. Sistema construido:** inspecciona el repositorio/documentación que pueda leer → traza el recorrido de usuarios y arquitectura → detecta procesos candidatos a simplificación → valida contigo cuáles están realmente en uso → **tú decides** cuáles mantener y cuáles cambiar → solo con un permiso diferente puede implementar cambios.

No interroga con 30 preguntas: **una pregunta prioritaria por turno**. Nunca asume que su recomendación ya fue aprobada; tampoco modifica servicios o datos sin autorización específica. Puede registrar la conversación en `assets/decision-session-template.md` para compartirla o continuarla en otra sesión si guardas ese archivo.

### Ejemplo realista de diálogo

> **Usuario:** «Quiero que audites mi e-commerce, ya está funcionando».  
> **Agente:** «¿Puedo revisar el repositorio o prefieres que primero mapeemos cómo recibe y entrega pedidos?»  
> **Usuario:** «Revisa el código».  
> **Agente:** «Encontré dos flujos de registro; aún no sé si ambos están activos. ¿Cuáles usan hoy?»  
> **Usuario:** «Solo el segundo».  
> **Agente:** «Propongo retirar el primero del recorrido (sin borrar nada todavía), comprobando enlaces que lo usan. ¿Lo eliminamos, lo simplificamos o prefieres mantenerlo?»

## Comandos de ejemplo

- «Activa `musk-algorithm` y hazme preguntas para conocer mi negocio antes de recomendar cambios.»
- «El sistema ya funciona; audita lo que existe y conversemos qué quitar y qué mantener, uno por uno.»
- «Usa `musk-algorithm` en modo `audit-live` para revisar nuestro marketplace antes de lanzarlo.»
- «Aplica los cinco pasos al proceso de despacho. ¿Qué eliminarías antes de automatizar?»
- «Audita mi repositorio en modo `implementation`, pero no cambies archivos sin mi confirmación.»
- «Quiero un agente IA para generar reportes. Demuéstrame primero si realmente hace falta.»
- «Revisa el onboarding: dame una matriz KEEP / DELETE / SIMPLIFY / DEFER / VALIDATE.»
- «Modo `quick`: cuestiona esta función antes de que la construyamos.»

## Paso 5: automatización guiada o ejecutada

- `DESIGN`: blueprint con evento, datos, reglas, APIs, errores, pruebas, costo y métrica.
- `BUILD`: si el agente tiene acceso a tu código y permiso, modifica **solo el alcance autorizado**, crea tests y documenta evidencias. Requiere entorno que permita leer/escribir/ejecutar; instalar una skill no concede esos accesos.
- `PILOT`: ejecuta pruebas controladas (no confundir mocks con una integración real); producción requiere permiso separado.
- `HANDOFF`: si falta acceso o conocimiento especializado, crea un paquete para otro agente o desarrollador, sin dependencia de ORE Skill.

**Ejemplo para marketplace:** confirmar pago mediante evento validado → crear una sola solicitud de despacho → notificar → registrar errores/reintentos. Primero reglas y webhooks; IA solo para excepciones ambiguas donde exista evaluación y revisión humana.

**Ejemplo de activación:** «Musk, terminamos de optimizar el despacho. Ahora evalúa si automatizarlo conviene. Muéstrame el flujo propuesto y, si apruebo, impleméntalo en este repositorio sin desplegar todavía».

## Flujo recomendado

```text
Negocio nuevo O sistema existente
      ↓
Descubrimiento conversacional / auditoría de evidencias
      ↓
QUESTION → DELETE → SIMPLIFY → ACCELERATE → AUTOMATE
      ↕
Consultoría + decisiones aprobadas por el usuario
      ↓
Matriz de decisiones + pruebas + plan de implementación (sin cambios no autorizados)
```

Los requisitos de seguridad, cumplimiento, consentimiento, pagos y protección de datos **no se eliminan** por una cuota arbitraria de simplificación. Se exige evaluación y autorización para cualquier cambio destructivo.

## Validar instalación y contenido

```bash
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/install.py --agent both --scope user --dry-run
```

Validador de formato de referencia opcional: `skills-ref validate ./musk-algorithm` si tienes instalado `skills-ref`.

## Arquitectura portable

El núcleo es `SKILL.md`: no requiere GitHub, API keys, ejecutables ni otro framework. Las referencias se cargan bajo demanda. `agents/openai.yaml` solo agrega metadatos de interfaz y no afecta el uso en otros agentes compatibles.

## Créditos y alcance

Metodología inspirada en la explicación pública de Elon Musk durante el tour Starbase/Everyday Astronaut de 2021. Esta skill no reproduce material de terceros extensamente ni pretende ser una herramienta oficial. Se publica como implementación independiente de ingeniería de procesos.
