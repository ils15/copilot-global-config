---
applyTo: 'repos/ofertachina-social/**'
description: 'Social Media Agent Audit System - Standardized process for integration quality and content consistency'
---

# Social Media Agent Audit System Instructions

## Overview

Este documento define o processo padrão de auditoria para **ofertachina-social** (agente de redes sociais). O foco é garantir confiabilidade das integrações com APIs de redes sociais, qualidade de conteúdo postado, segurança de credenciais e sincronização de dados entre plataformas.

**Objetivo**: Identificar bugs em integrações (Instagram, Facebook, Twitter), falhas de cross-posting, issues de segurança de credenciais, e gaps de rastreamento ANTES que causem perda de dados ou bans de conta.

---

## 📅 Quando Executar Auditoria

| Situação | Escopo | Agent | Frequência |
|----------|--------|-------|-----------|
| **Quarterly Review** | Todas as integrações (Instagram, Facebook, Twitter) | @debug + @backend | A cada 3 meses |
| **Pós-API Update** | Quando rede social atualizar API | @backend | Dentro de 2 semanas |
| **Cross-Posting Failure** | Quando falhar post em plataforma X | @debug | Dentro de 24h |
| **Credential Rotation** | Quando rotacionar tokens/secrets | @planner | Trimestralmente |
| **Rate Limit Issue** | Quando atingir rate limit | @debug | Imediatamente |

---

## 🔍 Audit Process

Follow the [shared audit template](_audit-template.md) for the 4-phase process (Assessment, Execution, Organization, Review), 30-question checklist, metrics table, and prioritization format.

---

## 📱 Social-Specific Audit Sections

### Platform Integrations
- ✅ Each social platform has dedicated integration module?
- ✅ API versioning handled properly (v1/v2 migrations)?
- ✅ Error handling specific to each platform's API quirks?
- ✅ Rate limiting respects platform-specific limits?
- ⚠️ Token refresh logic implemented for each platform?

### Posting Flows
- ✅ Cross-posting logic handles partial failures gracefully?
- ✅ Post status tracked across all platforms?
- ✅ Content validation prevents spam/inappropriate posts?
- ✅ Duplicate detection prevents reposting same content?
- ⚠️ Scheduling respects platform posting guidelines?

---

## 🤖 Subagent Usage

### Decision Matrix
- Use @backend for integration architecture review
- Use @debug for API reliability and security audits

### Workflow
```
@backend: Integration structure
  ↓
@debug: API reliability & security
  ↓
@planner: Prioritize & document
```

---

## 📋 Output Format

```markdown
## 📋 SOCIAL AUDIT REPORT
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

- Save reports in `memory-bank-social/audit-YYYY-MM-DD.md`
- Update Memory Bank with findings
- Escalate API/security issues to @planner/@reviewer

Após completar as 4 fases, gerar relatório no Memory Bank:

```markdown
# Social Media Agent Audit Report - [Data]

## Métricas Coletadas
- Total de linhas: XXX
- Providers: XX (Instagram, Facebook, Twitter, etc)
- Handlers/Services: XX
- Cobertura de testes: XX%

## Achados Críticos
- [ ] Q3.1 (Segurança): Tokens de Instagram hardcoded em [arquivo:linha]
- [ ] Q2.1 (Confiabilidade): Post que falha em Instagram não tem retry logic

## Achados High Priority
- [ ] Q1.3: 40% de duplicação entre instagram_handler e facebook_handler
- [ ] Q5.1: Apenas 60% dos posts são rastreados (missing logging)

## Padrões Positivos
✅ Cada provider tem módulo separado
✅ Rate limit handling para Twitter API
✅ Audit log de posts implementado

## Ações Recomendadas
1. **Week 1**: Fixar Q3.1 (secrets em Vault) + Q2.1 (retry logic)
2. **Week 2**: Refatorar para extrair BaseProvider (reduzir Q1.3 duplicação)
3. **Week 3**: Adicionar logging completo (Q5.1 → 100%)
4. **Ongoing**: Aumentar cobertura de testes para >80%

## Próxima Auditoria
[Data prevista]
```

---

## 🔧 Verificação Prática

Validar achados com código:

```bash
# Verificar tokens/secrets hardcoded
grep -r "instagram_token\|facebook_token\|twitter_key" repos/ofertachina-social --include="*.py" | grep -v "Vault\|environ\|config"

# Verificar retry logic
grep -r "retry\|backoff\|max_retries" repos/ofertachina-social --include="*.py" | head -10

# Verificar rate limit handling
grep -r "429\|rate_limit\|too_many_requests" repos/ofertachina-social --include="*.py"

# Verificar logging de posts
grep -r "logger\|logging\|print.*post" repos/ofertachina-social --include="*.py" | wc -l

# Verificar cross-posting implementation
grep -r "post_to_all\|cross_post\|multicast" repos/ofertachina-social --include="*.py"

# Contar providers
ls repos/ofertachina-social/app/integrations/
```

---

## 🔐 Social Media API Specifics

### Instagram (Meta)

```
API Version: Graph API v18.0+
Rate Limit: 200 requests/day per token
Auth: Long-lived access token (refresh every 60 days)
Retry Strategy: Exponential backoff 1s, 2s, 4s
Monitoring: Check token expiry weekly
```

### Facebook

```
API Version: Graph API v18.0+
Rate Limit: 200 requests/day per token
Auth: Long-lived access token (refresh every 60 days)
Retry Strategy: Exponential backoff
Monitoring: Check Business Account permissions monthly
```

### Twitter/X

```
API Version: Twitter API v2
Rate Limit: 300 posts/15min (essential tier)
Auth: Bearer token (no expiry, but may be revoked)
Retry Strategy: Backoff on 429 responses (seconds_until_reset)
Monitoring: Track rate limit headers
```

---

## 🎯 Integração com Agents

**Quem executa cada fase:**

| Fase | Agent | Tempo | Saída |
|------|-------|-------|-------|
| 1 (Métricas) | @backend | 10 min | Tabela de métricas |
| 2 (Estrutura) | @backend + @database | 15 min | Lista de red flags |
| 3 (Checklist) | @debug | 20 min | Respostas para 30 questões |
| 4 (Priorização) | @planner | 5 min | Matriz de ações |

**Workflow recomendado:**

```
@backend: Fase 1 + 2
  ↓
@debug: Fase 3 (com subagent para análise de providers)
  ↓
@planner: Fase 4 + documentar em Memory Bank
  ↓
@backend: Implementar fixes (CRITICAL + HIGH)
  ↓
@reviewer: Validar com testes (incluir failure scenarios)
  ↓
@planner: Atualizar Memory Bank com status final
```

---

## 📅 Ciclo Trimestral

**Padrão recomendado:**

- **Semana 1**: Planejar auditoria, coletar métricas
- **Semana 2**: Executar análise detalhada (integrações + segurança + confiabilidade)
- **Semana 3**: Implementar fixes CRITICAL + HIGH
- **Semana 4**: Validar com testes + documentar resultados

---

## 🔗 Referências

- **Memory Bank Social**: `/home/admin/ofertasdachina/repos/ofertachina-social/memory-bank/`
- **Vault Secrets**: `/home/admin/ofertasdachina/docs/memory-bank-infrastructure/VAULT-SECRETS-STRUCTURE.md`
- **Social Media APIs**:
  - Instagram Graph API: https://developers.facebook.com/docs/instagram-api
  - Facebook Graph API: https://developers.facebook.com/docs/graph-api
  - Twitter API v2: https://developer.twitter.com/en/docs/twitter-api
- **Testing**: `memory-bank/03-process.md` (seção Testing)

---

**Última Atualização**: 2025-12-12
