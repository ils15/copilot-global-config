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

## 🔍 Estrutura de Auditoria (4 Fases)

### Fase 1: Coleta de Métricas (10 min)

Use comandos no terminal para coletar dados básicos:

```bash
# Total de linhas de código
find repos/ofertachina-social -name "*.py" | xargs wc -l | tail -1

# Total de integrações (Instagram, Facebook, Twitter, etc)
ls -la repos/ofertachina-social/app/integrations/

# Total de handlers/processadores
grep -r "class.*Handler\|def.*process" repos/ofertachina-social/app --include="*.py" | wc -l

# Maior arquivo
find repos/ofertachina-social -name "*.py" -exec wc -l {} + | sort -n | tail -5

# Testes existentes
find repos/ofertachina-social/tests -name "*.py" | wc -l

# Verificar logging de posts
grep -r "post_id\|post_status\|failed_post" repos/ofertachina-social --include="*.py" | wc -l

# Verificar rate limit handling
grep -r "rate_limit\|429\|retry" repos/ofertachina-social --include="*.py" | wc -l
```

### Fase 2: Análise de Estrutura (15 min)

1. **Separação de Concerns**
   - ✅ Existe `/integrations` com provider separados (instagram/, facebook/, twitter/)?
   - ✅ Existe `/services` com lógica de sync/cross-posting?
   - ✅ Existe `/models` com Post, Schedule, Analytics?
   - ✅ Existe `/handlers` com event processing?
   - ⚠️ Se tudo misto, é RED FLAG

2. **God Integrations**
   - 🔴 Qual provider tem mais linhas? (Target: <400)
   - 🔴 Qual service tem mais métodos? (Target: <15)
   - 🔴 Existe muita duplicação entre providers?
   - ⚠️ Se > 500 linhas em um provider = REFACTOR NEEDED

3. **Integrações Críticas**
   - ⚠️ Instagram Graph API é robusta? (Error handling, retry logic)
   - ⚠️ Facebook SDK é atualizado?
   - ⚠️ Twitter API v2 é completamente implementada?
   - ⚠️ Há suporte a variações de API (different account types)?

4. **Data Consistency**
   - ⚠️ Como é sincronizado post_id entre plataformas?
   - ⚠️ Como é rastreado status de post (pending, published, failed)?
   - ⚠️ Como é tratado post que falha em 1 plataforma mas sucede em outra?

### Fase 3: Checklist de Qualidade (20 min)

Use o template padrão de **30 questões** em 6 categorias:

#### 1️⃣ ARQUITETURA - INTEGRAÇÕES (5 questões)

- Q1.1: Cada provider tem sua própria classe/módulo?
- Q1.2: Existe interface/abstração comum (ex: BaseProvider)?
- Q1.3: Qual % do código é duplicado entre providers?
- Q1.4: Como é tratado versionamento de API (novo endpoint)?
- Q1.5: Há suporte a múltiplas contas por rede social?

#### 2️⃣ CONFIABILIDADE - CROSS-POSTING (5 questões)

- Q2.1: Como é tratado quando post falha em 1 plataforma (mas sucede em outras)?
- Q2.2: Existe fila de retry para posts falhados?
- Q2.3: Há webhooks para sincronizar status em tempo real?
- Q2.4: Como é sincronizado post_id entre plataformas?
- Q2.5: Há verificação de duplicação antes de postar?

#### 3️⃣ SEGURANÇA - CREDENCIAIS (5 questões)

- Q3.1: Tokens de acesso estão em Vault (não hardcoded)?
- Q3.2: Há refresh logic para tokens que expiram?
- Q3.3: Há rotação de secrets implementada?
- Q3.4: Há audit log de quem acessou qual credencial?
- Q3.5: Há proteção contra token leakage em logs?

#### 4️⃣ SEGURANÇA - CONTEÚDO (5 questões)

- Q4.1: Há validação de conteúdo antes de postar? (spam, sensitive content)
- Q4.2: Há sanitização de HTML/links no conteúdo?
- Q4.3: Há proteção contra injection de código?
- Q4.4: Há rate limiting por plataforma?
- Q4.5: Há logging de todos os posts (para auditoria)?

#### 5️⃣ OBSERVABILIDADE (5 questões)

- Q5.1: Qual % de posts são rastreados (logging de inicio/fim)?
- Q5.2: Há alertas para falhas de cross-posting?
- Q5.3: Há dashboard de status por plataforma?
- Q5.4: Há métricas de latência por provider?
- Q5.5: Há traces de post inteiro (origem → post em X plataformas)?

#### 6️⃣ TESTES (5 questões)

- Q6.1: Há testes unitários para cada provider? Cobertura %?
- Q6.2: Há testes de integração (fake API)?
- Q6.3: Há testes para failure scenarios (API down, rate limit)?
- Q6.4: Há testes de cross-posting inteiro?
- Q6.5: Há testes de credential rotation?

---

### Fase 4: Matriz de Priorização (5 min)

Para cada achado, classificar:

| Severidade | Descrição | Ação | Prazo |
|-----------|-----------|------|-------|
| 🔴 CRITICAL | Post perdido, credencial exposta, API quebrada | Hotfix imediato | < 4h |
| 🟠 HIGH | Cross-posting falha em 1 plataforma, rate limit | Próximo sprint | < 1 semana |
| 🟡 MEDIUM | Duplicação de código, logging incompleto | Backlog | < 2 semanas |
| 🟢 LOW | Documentação, code style, refactoring | Nice-to-have | Próximo quarter |

---

## 📊 Relatório de Auditoria

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
