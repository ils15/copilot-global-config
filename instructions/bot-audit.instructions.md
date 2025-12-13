---
applyTo: 'bots/**'
description: 'Bot Audit System - Standardized process for quality and security assessment'
---

# Bot Audit System Instructions

## Overview

Este documento define o processo padrão de auditoria para bots Telegram no ecossistema **ofertachina-bots**. Cada bot segue a mesma estrutura modular e deve ser auditado regularmente para garantir qualidade, segurança e manutenibilidade.

**Objetivo**: Identificar bugs críticos, duplicação de código, issues de segurança, e gaps de arquitetura ANTES que causem problemas em produção.

---

## 📅 Quando Executar Auditoria

| Situação | Escopo | Agent | Frequência |
|----------|--------|-------|-----------|
| **Quarterly Review** | ALL 4 bots (username, alertas, ofertas, affiliate) | @planner + subagents | A cada 3 meses |
| **Pré-Refactoring** | Target bot específico | @bot-auditor | Antes de major changes |
| **Pós-Deploy** | Bot modificado | @reviewer | Após deploy crítico |
| **Nova Feature** | Bot impactado | @backend | Quando adiciona >200 lines |
| **Before Adding Bot** | Novo bot template | @planner | Antes de criar novo bot |

---

## 🔍 Estrutura de Auditoria (4 Fases)

### Fase 1: Coleta de Métricas (5 min)

Use comandos no terminal para coletar dados básicos:

```bash
# Total de linhas de código
find bots/{bot_name} -name "*.py" | xargs wc -l | tail -1

# Total de funções/métodos
grep -r "^def " bots/{bot_name} | wc -l

# Total de classes
grep -r "^class " bots/{bot_name} | wc -l

# Arquivo maior
find bots/{bot_name} -name "*.py" -exec wc -l {} + | sort -n | tail -5

# Duplicação de imports
grep -r "^from " bots/{bot_name} | sort | uniq -d
```

### Fase 2: Análise de Estrutura (10 min)

1. **Separação de Concerns**
   - ✅ Existe `/handlers` separado?
   - ✅ Existe `/services` separado?
   - ✅ Existe `/models` ou `/repositories`?
   - ⚠️ Se não, é uma RED FLAG

2. **God Objects**
   - 🔴 Qual classe tem mais métodos? (Target: <10)
   - 🔴 Qual arquivo tem mais linhas? (Target: <300)
   - ⚠️ CommandHandler > 15 métodos = REFACTOR NEEDED

3. **Código Duplicado**
   - Grep por padrões comuns (admin_menu, help_formatter, seed_groups)
   - Compare com outros bots
   - Target: <20% duplicação

### Fase 3: Checklist de Qualidade (15 min)

Use o template padrão de **25 questões** em 5 categorias:

#### 1️⃣ ESTRUTURA (5 questões)

- Q1.1: Qual é o maior arquivo e quantas linhas tem?
- Q1.2: Qual classe/módulo viola Single Responsibility Principle (SRP)?
- Q1.3: Existe separação clara entre `handlers/`, `services/`, `models/`?
- Q1.4: Quantos métodos tem a maior classe?
- Q1.5: Qual % do código é duplicado de outros bots?

#### 2️⃣ QUALIDADE (5 questões)

- Q2.1: Existe cobertura de testes? Qual %?
- Q2.2: Type hints estão presentes em funções públicas?
- Q2.3: Docstrings existem para classes/métodos públicos?
- Q2.4: Tratamento de erros é consistente (try/except/finally)?
- Q2.5: Logging é estruturado com níveis apropriados?

#### 3️⃣ SEGURANÇA (5 questões)

- Q3.1: Admin IDs estão hardcoded ou em config/Vault?
- Q3.2: Tokens/secrets são carregados via Vault AppRole?
- Q3.3: Há validação de input em todos os comandos?
- Q3.4: Conexões DB são fechadas corretamente (context managers)?
- Q3.5: Há rate limiting implementado?

#### 4️⃣ PERFORMANCE (5 questões)

- Q4.1: Há caching implementado? Onde?
- Q4.2: Queries DB são otimizadas (índices, paginação)?
- Q4.3: Conexões externas usam timeout/retry?
- Q4.4: Há memory leaks conhecidos?
- Q4.5: Pool de conexões está configurado corretamente?

#### 5️⃣ MANUTENIBILIDADE (5 questões)

- Q5.1: Memory Bank está atualizado e completo?
- Q5.2: README ou documentação existe no bot?
- Q5.3: Configuração é via env vars ou hardcoded?
- Q5.4: Existe versionamento de schema/migrations?
- Q5.5: Comandos estão documentados em `/help`?

### Fase 4: Priorização e Relatório (10 min)

Classificar todos os issues encontrados:

- 🔴 **CRITICAL**: Fix today (runtime errors, security breaches)
  - Exemplo: Pool exhaustion, hardcoded secrets, SQL injection
  
- 🟠 **HIGH**: Fix this sprint (major refactoring)
  - Exemplo: God objects, major code duplication, missing error handling
  
- 🟡 **MEDIUM**: Fix next sprint (improvements)
  - Exemplo: Missing type hints, low test coverage, optimization opportunities
  
- 🟢 **LOW**: Backlog (nice-to-have)
  - Exemplo: Docstring improvements, logging verbosity, code style

---

## 🤖 Uso de Subagents para Auditorias

### Decision Matrix: Quando Usar Subagent?

```
EXECUTAR AUDITORIA DE BOT:

1. É o bot > 500 linhas?
   ├─ SIM → USE SUBAGENT (@debug ou @bot-auditor)
   └─ NÃO → INLINE ANALYSIS OK

2. Precisa analisar > 5 arquivos diferentes?
   ├─ SIM → USE SUBAGENT
   └─ NÃO → INLINE ANALYSIS OK

3. Output esperado > 50 linhas?
   ├─ SIM → USE SUBAGENT
   └─ NÃO → INLINE ANALYSIS OK

4. Auditar MÚLTIPLOS bots em paralelo?
   ├─ SIM → USE MÚLTIPLOS SUBAGENTS (paralelizar)
   └─ NÃO → USE 1 SUBAGENT sequencial
```

### Subagent Selection por Bot Type

| Bot Type | Primary Subagent | Secondary Subagent |
|----------|-----------------|-------------------|
| **Verification Bot** | @debug (security focus) | @reviewer (validation) |
| **Alert Bot** | @debug (performance focus) | @backend (optimization) |
| **Commerce Bot** | @debug (API integration focus) | @reviewer (conversion) |
| **Helper Bot** | @debug (UX flow focus) | @backend (AI integration) |

### Subagent Prompt Template

```
Você é especialista em auditoria de bots Telegram. Analise o {bot_name} bot localizando em:

{bot_path}

**PROCURE POR:**
1. BUGS CRÍTICOS - runtime errors, crashes, security holes
2. CODE DUPLICATION - padrões repetidos de outros bots
3. IMPORTS QUEBRADOS - paths relativos incorretos
4. EXCEPTION HANDLING - except: pass silenciando erros
5. CONNECTION LEAKS - cursores/sockets não fechados
6. RACE CONDITIONS - estado compartilhado sem locks
7. HARDCODED CONFIG - secrets, admin IDs, API keys

**RETORNE APENAS:**

## 📋 BOT AUDIT REPORT: {bot_name}

### SUMMARY
- Total lines: X
- Largest class/file: Y
- Estimated health: Z%

### 🔴 CRITICAL ISSUES (max 3)
1. [Issue] - [File:Line] - [Impact] - [Fix]
2. ...

### 🟠 HIGH PRIORITY ISSUES (max 3)
1. [Issue] - [File:Line] - [Impact] - [Fix]

### 🟡 MEDIUM PRIORITY ISSUES (max 3)
1. [Issue] - [File:Line] - [Impact] - [Fix]

### ✅ STRENGTHS
- [What's working well]

### 📊 METRICS
- Code duplication: X%
- Test coverage: Y%
- Type hints presence: Z%

NÃO crie arquivo .md. Retorne apenas no chat.
```

---

## 📋 Formato de Saída Padrão

Todos os relatórios de auditoria devem seguir este formato:

```markdown
## 📋 BOT AUDIT REPORT: {bot_name}
**Date**: {YYYY-MM-DD}  
**Auditor**: {agent_name}  
**Status**: [CRITICAL/HIGH/MEDIUM/LOW PRIORITY]

### 📊 SUMMARY METRICS

| Metric | Value | Status | Target |
|--------|-------|--------|--------|
| Total Lines | X | 🟢/🟡/🔴 | <5000 |
| Largest Class | Y methods | 🟢/🟡/🔴 | <10 |
| Largest File | Z lines | 🟢/🟡/🔴 | <300 |
| Test Coverage | W% | 🟢/🟡/🔴 | >70% |
| Code Duplication | V% | 🟢/🟡/🔴 | <20% |
| Vault Integration | OK/FAIL | ✅/❌ | All secrets |
| Security Score | S/10 | 🟢/🟡/🔴 | >8 |
| Architecture Score | R/10 | 🟢/🟡/🔴 | >7 |

### 🔴 CRITICAL ISSUES
1. **[Issue Title]**
   - Location: File:Line
   - Impact: Description of impact
   - Fix: Recommended fix (1-2 lines)
   - Effort: X hours

2. ...

### 🟠 HIGH PRIORITY ISSUES
1. **[Issue Title]**
   - Location: File:Line
   - Impact: Description
   - Fix: Recommendation
   - Effort: X hours

### 🟡 MEDIUM PRIORITY ISSUES
1. **[Issue Title]**
   - Location: File:Line
   - Impact: Description
   - Fix: Recommendation
   - Effort: X hours

### ✅ STRENGTHS (Positive observations)
- [What's working well]
- [Good patterns]
- [Best practices followed]

### 📝 RECOMMENDATIONS
1. **[Priority Item]** - Estimated: [X hours]
2. **[Priority Item]** - Estimated: [X hours]
3. **[Priority Item]** - Estimated: [X hours]

### 📁 FILES AUDITED
- handlers/[...].py
- services/[...].py
- models/[...].py
- [...]
```

---

## 🔗 Integração com Memory Bank

### Workflow Pós-Audit

1. **Save Audit Report**
   ```
   memory-bank-{bot_name}/
   └── audit-2025-12-12.md  ← Salvar resultado aqui
   ```

2. **Create Action Items**
   ```
   memory-bank-{bot_name}/tasks/
   └── _index.md  ← Adicionar tarefas encontradas
   ```

3. **Update Architecture Doc**
   ```
   memory-bank-{bot_name}/01-architecture.md
   └── Documentar quaisquer mudanças estruturais descobertas
   ```

4. **Track Progress**
   ```
   memory-bank-{bot_name}/05-progress-log.md
   └── Entry: "Audit completed - X critical issues, Y refactoring items"
   ```

---

## 🔄 Cross-Bot Patterns

### ✅ Shared Components (Reutilizar em Todos)

- **HelpFormatter**: `bots/shared/helpers/help_command.py`
- **Admin Commands** (TO BE CREATED): `bots/shared/handlers/admin_command_handler.py`
- **Group Discovery**: `bots/shared/services/group_discovery_service.py`

### ❌ Anti-Patterns (Nunca Fazer)

| Pattern | Why Bad | Example |
|---------|---------|---------|
| **Hardcoded Admin IDs** | Security risk, not configurable | `ADMIN_IDS = [141386101]` |
| **Callbacks in setup()** | Not testable, hard to debug | Registering handlers no main |
| **CommandHandler >10 methods** | God object, hard to test | 17+ métodos em 1 classe |
| **DB connections not closed** | Connection pool exhaustion | `cursor = conn.cursor()` (no finally) |
| **Silent exception handlers** | Impossible to debug | `except Exception: pass` |
| **Duplicated admin logic** | Maintenance nightmare | Same admin menu em 4 bots |

---

## 📊 Métricas de Saúde Target

| Métrica | 🟢 Good | 🟡 Warning | 🔴 Critical | Fix Priority |
|---------|---------|------------|------------|-------------|
| **Lines per file** | <300 | 300-500 | >500 | HIGH |
| **Methods per class** | <10 | 10-15 | >15 | CRITICAL |
| **Code duplication** | <20% | 20-40% | >40% | HIGH |
| **Test coverage** | >70% | 40-70% | <40% | MEDIUM |
| **Type hints** | >90% | 70-90% | <70% | MEDIUM |
| **Hardcoded config** | 0 | 1-3 | >3 | CRITICAL |
| **Connection leaks** | 0 | 1-2 | >2 | CRITICAL |
| **Silent exceptions** | 0 | 1-2 | >2 | CRITICAL |

---

## ✅ Checklist Pré-Auditoria

Antes de começar qualquer auditoria, validar:

- [ ] Memory Bank do bot existe e está atualizado?
- [ ] Bot está em /home/admin/ofertasdachina/repos/ofertachina-bots/bots/{bot_name}?
- [ ] Memory Bank estrutura padrão (00-07 files)?
- [ ] Últimos logs do bot mostram erros críticos?
- [ ] Docker image existe para o bot?
- [ ] Bot está documentado em agents.md?
- [ ] .gitignore está configurado corretamente?

---

## 📈 Exemplo: Auditoria de username_verification_bot

### Exec Summary
- **Status**: ✅ SAUDÁVEL (após correções)
- **Audit Date**: 2025-12-12
- **Critical Issues Found**: 8 (FIXADOS HOJE)
- **Health Score**: 85/100

### Corrected Issues
```
✅ Duplicação de is_admin() - FIXADO
✅ Duplicação de handle_status() - FIXADO
✅ Try/except aninhados - SIMPLIFICADO
✅ Imports quebrados - CORRIGIDOS
✅ log_action() signature - CORRIGIDA
✅ GroupConfigSystem injection - CORRIGIDA
✅ UserService import - CORRIGIDA
✅ Overall structure - VALIDADA
```

### Resultado: BOT READY FOR PRODUCTION ✅

---

## 🚀 Quarterly Audit Workflow

```
┌─ Q1 START ─┐
│            │
├─ PLAN AUDITS (Week 1)
│  └─ Schedule 4 bots
│  └─ Assign subagents
│  └─ Prepare templates
│
├─ EXECUTE AUDITS (Week 2-3)
│  ├─ @debug audit username_verification_bot
│  ├─ @debug audit alertas_bot
│  ├─ @debug audit ofertas_bot
│  └─ @debug audit affiliate_helper_bot
│
├─ CONSOLIDATE (Week 4)
│  ├─ @planner consolidate findings
│  ├─ Create cross-bot analysis
│  ├─ Prioritize shared refactoring
│  └─ Update agents.md with lessons
│
├─ EXECUTE FIXES (Week 5-12)
│  ├─ CRITICAL items (now)
│  ├─ HIGH items (sprint 1)
│  ├─ MEDIUM items (sprint 2)
│  └─ LOW items (backlog)
│
└─ Q2 VALIDATION ─┘
   └─ Re-audit to verify fixes
```

---

## 📞 Support & Escalation

**Issues During Audit?**
- Import errors → Check .github/instructions/project-context.md
- DB schema questions → Check memory-bank-infrastructure/
- Vault secrets → Check VAULT-SECRETS-STRUCTURE.md
- Port allocation → Check QUICK-REFERENCE-PORTS.md

**Escalate if:**
- Finding suggests architecture redesign (→ @planner)
- Finding suggests security vulnerability (→ @reviewer)
- Finding affects multiple bots (→ @planner + subagents)
- Finding requires major refactoring (→ project lead)

---

## 📚 Related Documentation

- **Project Context**: `.github/instructions/project-context.md`
- **Memory Bank Guide**: `.github/instructions/memory-bank.instructions.md`
- **Copilot Guidelines**: `.github/instructions/copilot-instructions.md`
- **Agent Definitions**: `agents.md`
- **Bot Architecture**: `ofertasdachina/docs/memory-bank/01-architecture.md`
- **Infrastructure**: `ofertasdachina/docs/memory-bank-infrastructure/`

---

**Version**: 1.0  
**Last Updated**: 2025-12-12  
**Maintained By**: Platform Team  
**Next Review**: 2026-03-12 (Q2 Quarterly Audit)
