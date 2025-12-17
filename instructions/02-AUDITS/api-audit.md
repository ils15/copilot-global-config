---
applyTo: 'repos/ofertachina-api/**'
description: 'API Audit System - Standardized process for backend quality and performance assessment'
---

# API Audit System Instructions

## Overview

Este documento define o processo padrão de auditoria para a **ofertachina-api** (FastAPI backend). O foco é garantir qualidade de código, performance de endpoints, segurança de dados e robustez da arquitetura de serviços.

**Objetivo**: Identificar bottlenecks de performance, bugs em lógica de negócio, gaps de segurança, e problemas de escalabilidade ANTES que causem degradação em produção.

---

## 📅 Quando Executar Auditoria

| Situação | Escopo | Agent | Frequência |
|----------|--------|-------|-----------|
| **Quarterly Review** | Todos os routers, services, repositories | @debug + @database | A cada 3 meses |
| **Pré-Release Major** | APIs críticas (auth, products, affiliates) | @backend + @database | Antes de deploy major |
| **Pós-Deploy** | Endpoint que sofreu mudança | @reviewer | Após deploy em produção |
| **Nova Feature** | Router novo que adiciona >5 endpoints | @backend | Quando implementa feature |
| **Performance Regression** | Endpoint específico lento | @debug + @database | Quando detectar slowness |

---

## 🔍 Audit Process

Follow the [shared audit template](_audit-template.md) for the 4-phase process (Assessment, Execution, Organization, Review), 30-question checklist, metrics table, and prioritization format.

---

## 🔧 API-Specific Audit Sections

### API Endpoints
- ✅ Endpoints follow REST conventions (GET/POST/PUT/DELETE appropriate)?
- ✅ Response schemas use Pydantic models consistently?
- ✅ Error responses use proper HTTP status codes?
- ✅ Pagination implemented for collection endpoints?
- ⚠️ Rate limiting configured per endpoint?

### Services
- ✅ Business logic separated from routers?
- ✅ Services use dependency injection properly?
- ✅ Database transactions handled correctly?
- ✅ External API calls have timeout/retry logic?
- ⚠️ Service methods are unit testable?

### Async Patterns
- ✅ All I/O operations use async/await?
- ✅ No blocking calls in async functions?
- ✅ Concurrent requests handled properly?
- ✅ Background tasks implemented for long operations?
- ⚠️ Async context managers used for DB connections?

---

## 🤖 Subagent Usage

### Decision Matrix
- Use @backend for structure analysis
- Use @database for query optimization review
- Use @debug for security/performance audits

### Workflow
```
@backend: Structure analysis
  ↓
@database: Query optimization
  ↓
@debug: Security & performance
  ↓
@planner: Prioritize & document
```

---

## 📋 Output Format

```markdown
## 📋 API AUDIT REPORT
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

- Save reports in `memory-bank-api/audit-YYYY-MM-DD.md`
- Update Memory Bank with findings
- Escalate performance/security issues to @planner/@reviewer
