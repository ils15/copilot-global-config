# 🏛️ Plano Estratégico - Copilot Agents com Mitologia Grega

## Visão Geral

Refatoração completa do sistema de agentes seguindo **padrões oficiais do VSCode** (Custom Instructions, Prompt Files, Agent Skills) com **nomes mitológicos gregos** que refletem papéis especializados.

**Status**: Estratégia em Desenvolvimento  
**Base**: VSCode 1.108+ | Agent Skills Standard | Github-Copilot-Atlas v2

---

## 📊 Mapeamento de Agentes Mitológicos

| Posição | Agente Atual | Nome Mitológico | Mitologia | Função | Status |
|---------|-------------|---|------|--------|--------|
| **1** | orchestrator | **Zeus** | Grega | Coordenador central - autoridade, orquestração | 🔄 Renomear |
| **2** | planner | **Atena** | Grega | Sabedoria estratégica, decisões arquiteturais | 🔄 Renomear |
| **3** | explorer | **Hermes** | Grega | Scout rápido, exploração paralela, mensageiro | 🔄 Renomear |
| **4** | backend | **Hefesto** | Grega | Forja/construção, implementação sólida | ✅ Feito (hermes) |
| **5** | frontend | **Afrodite** | Grega | Beleza, estética, experiência visual | 🔄 Renomear |
| **6** | database | **Maat** | Egípcia | Ordem, justiça, integridade de dados | 🔄 Renomear |
| **7** | infra | **Rá** | Egípcia | Energia, ciclos constantes (CI/CD) | 🔄 Renomear |
| **8** | code-reviewer | **Têmis** | Grega | Leis, conformidade, qualidade | 🔄 Renomear |
| **9** | memory | **Mnemósine** | Grega | Deusa da memória, documentação | ✅ Feito |

---

## 🏗️ Estrutura de Arquivos (VSCode Padrão)

```
.github/
├── AGENTS.md                           # Orquestrador central (Zeus)
├── agents/
│   ├── zeus.agent.md                   # Orchestrator
│   ├── atena-subagent.agent.md         # Planner
│   ├── hermes-subagent.agent.md        # Scout/Explorer
│   ├── hefesto-subagent.agent.md       # Backend
│   ├── afrodite-subagent.agent.md      # Frontend
│   ├── maat-subagent.agent.md          # Database
│   ├── ra-subagent.agent.md            # Infrastructure
│   ├── temis-subagent.agent.md         # Code Reviewer
│   └── mnemosyne-subagent.agent.md     # Memory
│
├── instructions/                        # Custom Instructions (.instructions.md)
│   ├── backend-standards.instructions.md
│   ├── frontend-standards.instructions.md
│   ├── database-standards.instructions.md
│   ├── infra-standards.instructions.md
│   └── code-review-standards.instructions.md
│
├── prompts/                             # Reusable Prompts (.prompt.md)
│   ├── implement-feature.prompt.md
│   ├── review-code.prompt.md
│   ├── plan-architecture.prompt.md
│   ├── optimize-database.prompt.md
│   └── debug-issue.prompt.md
│
└── skills/                              # Specialized Skills (SKILL.md)
    ├── tdd-testing/SKILL.md
    ├── api-design/SKILL.md
    ├── performance-optimization/SKILL.md
    ├── security-audit/SKILL.md
    ├── database-migration/SKILL.md
    └── docker-deployment/SKILL.md
```

---

## 🎯 Fase 1: Refatoração de Agentes

### Nomes Atuais vs Novos

```bash
# Renomear existentes
backend.agent.md → hefesto-subagent.agent.md      ✅ FEITO
frontend.agent.md → afrodite-subagent.agent.md    ⏳ TODO
database.agent.md → maat-subagent.agent.md        ⏳ TODO
infra.agent.md → ra-subagent.agent.md             ⏳ TODO
code-reviewer.agent.md → temis-subagent.agent.md  ⏳ TODO
planner-architect.agent.md → atena-subagent.agent.md ⏳ TODO
orchestrator.agent.md → zeus.agent.md             ⏳ TODO

# Renomear (já feitos antes)
explorer.agent.md → hermes-subagent.agent.md      ✅ FEITO
memory.agent.md → mnemosyne-subagent.agent.md     ✅ FEITO
```

### YAML Frontmatter Padrão (Todos os Agentes)

```yaml
---
name: [lowercase-name]
description: [Role específico do deus na mitologia]
argument-hint: "[Como invocar este agente]"
tools: ['search', 'usages', 'edit', 'runCommands', 'runTasks', 'runSubagent']
model: Claude Sonnet 4.5 (copilot)
---
```

---

## 📋 Fase 2: Custom Instructions (.instructions.md)

### Padrão YAML

```yaml
---
description: "[Descrição breve]"
name: "[Nome da instrução]"
applyTo: "[Glob pattern - ex: **/*.py]"
---
```

### Arquivos a Criar

#### 1. **backend-standards.instructions.md**
```yaml
applyTo: "**/*.py"
---
# Backend Development Standards (Hefesto)

- Use async/await para todas operações I/O
- Implementar TDD: RED → GREEN → REFACTOR
- Type hints em todos os parâmetros
- Docstrings em funções públicas
- Máximo 300 linhas por arquivo
```

#### 2. **frontend-standards.instructions.md**
```yaml
applyTo: "**/*.{tsx,jsx}"
---
# Frontend Development Standards (Afrodite)

- TypeScript strict mode
- Props interfaces em todos componentes
- ARIA labels para acessibilidade
- Mobile-first responsive design
- >80% test coverage com React Testing Library
```

#### 3. **database-standards.instructions.md**
```yaml
applyTo: "**/*migration*.py"
---
# Database Standards (Maat)

- Forward migration + rollback sempre
- Testar em dados production-like
- Documentar breaking changes
- Nunca editar migrations antigas
- Usar transações para consistência
```

#### 4. **code-review-standards.instructions.md**
```yaml
applyTo: "**"
---
# Code Review Standards (Têmis)

- Verificar OWASP Top 10
- Validar cobertura >80%
- Revisar apenas arquivos alterados
- Categorizar: CRITICAL | HIGH | MEDIUM | LOW
- Sem fallbacks síncronos quando async disponível
```

#### 5. **infra-standards.instructions.md**
```yaml
applyTo: "**/{Dockerfile,docker-compose.yml,*.tf}"
---
# Infrastructure Standards (Rá)

- Multi-stage builds em Dockerfiles
- Health checks em todos serviços
- Variáveis de ambiente não hardcoded
- CI/CD pipeline definido em código
- Suportar dev/staging/prod
```

---

## 💬 Fase 3: Prompt Files (.prompt.md)

### Padrão YAML

```yaml
---
name: "[Nome visible com /]"
description: "[O que o prompt faz]"
argument-hint: "[Dica para usuário]"
agent: [zeus|atena|hermes|hefesto|afrodite|maat|ra|temis]
tools: ['search', 'usages', 'edit', 'runCommands']
model: Claude Sonnet 4.5 (copilot)
---
```

### Prompts a Criar

#### 1. **implement-feature.prompt.md**
```yaml
agent: zeus
---
# Implementar Feature com TDD

Use @atena para planejar. Use @hefesto + @afrodite + @maat em paralelo.
Depois @temis revisa. Finalmente @ra faz deploy.

Foco: TDD primeiro, código mínimo, testes >80%
```

#### 2. **plan-architecture.prompt.md**
```yaml
agent: atena
---
# Planejar Arquitetura

Pesquise com @hermes. Analise padrões existentes.
Crie plano 3-10 fases com TDD.
Ofereça handoff automático para @zeus.
```

#### 3. **review-code.prompt.md**
```yaml
agent: temis
---
# Revisar Código com Segurança

Verifique: OWASP Top 10, testes, cobertura >80%.
Revise APENAS arquivos alterados.
Retorne: APPROVED | NEEDS_REVISION | FAILED
Categorize: CRITICAL | HIGH | MEDIUM | LOW
```

#### 4. **optimize-database.prompt.md**
```yaml
agent: maat
---
# Otimizar Database

- Identifique queries N+1
- Adicione índices estratégicos
- Analise execution plans
- Sugira denormalização se necessário
```

#### 5. **debug-issue.prompt.md**
```yaml
agent: hermes
---
# Debug Rápido (Exploração Paralela)

Lance 5-10 buscas paralelas simultâneas.
Retorne apenas arquivos relevantes.
Sugira próximos passos com @zeus.
```

---

## 🛠️ Fase 4: Agent Skills (SKILL.md)

### Padrão YAML

```yaml
---
name: [skill-name]
description: [Quando usar + o que faz]
---
```

### Skills a Criar

#### 1. **.github/skills/tdd-testing/SKILL.md**
- RED: Teste que falha
- GREEN: Código mínimo
- REFACTOR: Melhorar sem quebrar

#### 2. **.github/skills/api-design/SKILL.md**
- REST API standards
- HTTP methods corretos
- Pagination/filtering
- Error responses

#### 3. **.github/skills/security-audit/SKILL.md**
- OWASP Top 10
- Input validation
- SQL injection
- XSS, CSRF prevention

#### 4. **.github/skills/database-migration/SKILL.md**
- Migration scripting
- Backward compatibility
- Rollback procedures

#### 5. **.github/skills/docker-deployment/SKILL.md**
- Multi-stage builds
- Health checks
- Layer optimization
- Secrets management

#### 6. **.github/skills/performance-optimization/SKILL.md**
- Query optimization
- N+1 detection
- Index recommendations
- Caching strategies

---

## 🎛️ Fase 5: Orquestrador Central (AGENTS.md)

```yaml
---
description: "Orchestrator central usando todos agentes mitológicos"
---

# Zeus - Central Orchestrator

You are **ZEUS** - the orchestrating force coordinating all agents.

## Available Subagents

1. **Atena** (Planner) - Strategic planning, TDD-driven
2. **Hermes** (Scout) - Rapid file discovery
3. **Hefesto** (Backend) - API & services
4. **Afrodite** (Frontend) - UI/UX components
5. **Maat** (Database) - Schema & migrations
6. **Rá** (Infrastructure) - Docker & deployment
7. **Têmis** (Reviewer) - Code quality & security
8. **Mnemósine** (Memory) - Documentation

## Orchestration Workflow

Phase 1: Planning (@Atena)
Phase 2: Parallel Implementation (@Hefesto + @Afrodite + @Maat)
Phase 3: Quality Gate (@Têmis)
Phase 4: Deployment (@Rá)
```

---

## ⚙️ Fase 6: VSCode Settings

```json
{
  "chat.useAgentsMdFile": true,
  "chat.useAgentSkills": true,
  "chat.instructionsFilesLocations": [".github/instructions"],
  "chat.promptFilesLocations": [".github/prompts"],
  "chat.codeGeneration.useInstructionFiles": true,
  "github.copilot.chat.responsesApiReasoningEffort": "high"
}
```

---

## 📅 Cronograma

| Fase | Descrição | Timeline | Status |
|------|-----------|----------|--------|
| 1 | Renomear agentes para nomes mitológicos | Hoje | 🔄 Em Progresso |
| 2 | Criar .instructions.md files | Amanhã | ⏳ TODO |
| 3 | Criar .prompt.md files | Amanhã | ⏳ TODO |
| 4 | Criar SKILL.md files | Semana que vem | ⏳ TODO |
| 5 | Criar AGENTS.md orquestrador | Semana que vem | ⏳ TODO |
| 6 | Configurar VSCode settings | Semana que vem | ⏳ TODO |
| 7 | Testes e documentation | Semana que vem | ⏳ TODO |

---

## 🚀 Próximos Passos

1. ✅ **Refatorar agentes com nomes mitológicos** (5/9 completos)
2. 📋 **Criar Custom Instructions** organizadas por domínio
3. 💬 **Criar Prompts reutilizáveis** para tarefas comuns
4. 🛠️ **Criar Skills especializadas** para workflows
5. 🎛️ **Montar AGENTS.md orquestrador** central
6. ⚙️ **Configurar VSCode** com settings otimizadas

---

## 📐 Benefícios desta Arquitetura

✅ **Context Conservation**: 10-15% contexto vs 80-90%  
✅ **Parallel Execution**: 3-10 agentes simultâneos  
✅ **Portability**: Skills funcionam em VSCode, CLI, Coding Agent  
✅ **Reutilização**: Instructions + Prompts + Skills compartilháveis  
✅ **Escalabilidade**: Adicione skills sem saturation de contexto  
✅ **Mitologia**: Nomes memoráveis e domain-specific  

---

## 📚 Referências

- [VSCode Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [VSCode Prompt Files](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [VSCode Custom Instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Agent Skills Specification](https://agentskills.io/)
- [Github-Copilot-Atlas](https://github.com/bigguy345/Github-Copilot-Atlas)

---

**Filosofia**: Coordenar expertise. Conservar contexto. Entregar qualidade. Mover rápido.
