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

## 🔍 Audit Process

Follow the [shared audit template](_audit-template.md) for the 4-phase process (Assessment, Execution, Organization, Review), 30-question checklist, metrics table, and prioritization format.

---

## 🤖 Bot-Specific Audit Sections

### Handler Structure
- ✅ Command handlers follow `/command` pattern?
- ✅ Callback handlers use proper data format?
- ✅ Error handlers catch Telegram-specific exceptions?
- ✅ Message handlers validate input types?
- ⚠️ Inline handlers implemented correctly?

### Webhook Configuration
- ✅ Webhook URL properly configured in Telegram API?
- ✅ SSL certificate valid and current?
- ✅ Timeout settings appropriate for bot usage?
- ✅ Fallback to polling if webhook fails?
- ⚠️ Webhook secret token matches bot token?

### Telegram Patterns
- ✅ Bot uses `aiogram` or `python-telegram-bot` consistently?
- ✅ State management for conversations implemented?
- ✅ Keyboard markup follows UX guidelines?
- ✅ Media handling (photos, documents) works correctly?
- ⚠️ Rate limiting respects Telegram API limits (30 msg/sec)?

---

## 🤖 Subagent Usage

### Decision Matrix
- Use subagent for bots >500 lines or >5 files
- Use @debug for security/performance focus
- Use @backend for refactoring/complexity

### Subagent Prompt Template
```
Analise o {bot_name} bot em {bot_path}

PROCURE POR: bugs críticos, duplicação, imports quebrados, exception handling, connection leaks, race conditions, hardcoded config

RETORNE APENAS o relatório no formato padrão.
```

---

## 📋 Output Format

```markdown
## 📋 BOT AUDIT REPORT: {bot_name}
**Date**: {YYYY-MM-DD}  
**Auditor**: {agent_name}  
**Status**: [CRITICAL/HIGH/MEDIUM/LOW PRIORITY]

### 📊 SUMMARY METRICS
[Metrics table from template]

### 🔴 CRITICAL ISSUES
[List critical issues]

### 🟠 HIGH PRIORITY ISSUES
[List high priority]

### 🟡 MEDIUM PRIORITY ISSUES
[List medium priority]

### ✅ STRENGTHS
[Positive observations]

### 📝 RECOMMENDATIONS
[Priority items with estimates]
```

---

## 🔗 Integration

- Save reports in `memory-bank-{bot_name}/audit-YYYY-MM-DD.md`
- Update Memory Bank with findings
- Escalate architecture/security issues to @planner/@reviewer
