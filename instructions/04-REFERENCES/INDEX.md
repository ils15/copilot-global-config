# Instructions Index - Programmatic Cross-Reference

## File Inventory

### Core Rules & Structure
- **core.rules.md**
  - Purpose: All must-follow rules
  - Keywords: planning, rules, documentation, tasks
  - Cross-references: copilot-instructions.md, memory-bank.instructions.md, no-unnecessary-files.instructions.md

- **memory-bank-structure.md**
  - Purpose: Memory bank organization guide
  - Keywords: memory-bank, structure, generic, ofertasdachina
  - Cross-references: memory-bank.instructions.md, project-context.instructions.md

### Workflows & Agents
- **context-isolated-subagents.instructions.md**
  - Purpose: Subagent routing and usage
  - Keywords: subagents, routing, context-isolation
  - Cross-references: agents.md

- **copilot-execution.md**
  - Purpose: Code quality and review guidelines
  - Keywords: code-quality, review, security, docker, git
  - Cross-references: core.rules.md

### Audits
- **_audit-template.md**
  - Purpose: Shared audit structure
  - Keywords: audit, template, metrics, phases
  - Cross-references: api-audit.md, bot-audit.md, socialpost-audit.md, impressao3d-audit.md

- **api-audit.md**
  - Purpose: API audit process
  - Keywords: api, audit, endpoints, services, async
  - Cross-references: _audit-template.md

- **bot-audit.md**
  - Purpose: Bot audit process
  - Keywords: bot, audit, handlers, webhooks, telegram
  - Cross-references: _audit-template.md

- **socialpost-audit.md**
  - Purpose: Social media audit process
  - Keywords: social, audit, integrations, posting
  - Cross-references: _audit-template.md

- **impressao3d-audit.md**
  - Purpose: 3D printing marketplace audit
  - Keywords: impressao3d, audit, marketplace, stl, obj
  - Cross-references: _audit-template.md

### Domain Guides
- **telegram-bot-ui-design.instructions.md**
  - Purpose: Telegram bot UI/UX patterns
  - Keywords: telegram, ui, ux, keyboards, messages

- **web-ui-ux-analysis.instructions.md**
  - Purpose: Web UI/UX analysis framework
  - Keywords: web, ui, ux, frontend, analysis

- **code-simplification.instructions.md**
  - Purpose: Code simplification techniques
  - Keywords: simplification, refactoring, complexity

### Project Context
- **project-context.instructions.md**
  - Purpose: Ofertasdachina project overview
  - Keywords: project, context, ofertasdachina, architecture
  - Cross-references: memory-bank-structure.md

- **memory-bank.instructions.md**
  - Purpose: Memory bank workflows
  - Keywords: memory-bank, workflows, tasks
  - Cross-references: memory-bank-structure.md, core.rules.md

- **no-unnecessary-files.instructions.md**
  - Purpose: Documentation file rules
  - Keywords: documentation, files, memory-bank
  - Cross-references: core.rules.md

## Search Tags

### By Topic
- **Planning**: core.rules.md
- **Documentation**: core.rules.md, memory-bank-structure.md, no-unnecessary-files.instructions.md
- **Tasks**: core.rules.md, memory-bank.instructions.md
- **Audits**: _audit-template.md, *-audit.md
- **Code Quality**: copilot-execution.md
- **Security**: copilot-execution.md
- **Subagents**: context-isolated-subagents.instructions.md

### By Component
- **API**: api-audit.md, project-context.instructions.md
- **Bots**: bot-audit.md, telegram-bot-ui-design.instructions.md
- **Social**: socialpost-audit.md
- **Frontend**: web-ui-ux-analysis.instructions.md
- **3D Printing**: impressao3d-audit.md

## Maintenance

- Update this index when adding/removing instruction files
- Keep cross-references accurate
- Review quarterly for consolidation opportunities