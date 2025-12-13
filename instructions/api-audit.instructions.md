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

## 🔍 Estrutura de Auditoria (4 Fases)

### Fase 1: Coleta de Métricas (10 min)

Use comandos no terminal para coletar dados básicos:

```bash
# Total de linhas de código (excluindo tests)
find repos/ofertachina-api/app -name "*.py" ! -path "*/tests/*" | xargs wc -l | tail -1

# Total de routers/endpoints
grep -r "^@router\." repos/ofertachina-api/app/routers --include="*.py" | wc -l

# Total de métodos em services
grep -r "^    async def " repos/ofertachina-api/app/services --include="*.py" | wc -l

# Total de modelos SQLAlchemy
grep -r "^class.*Base" repos/ofertachina-api/app/models --include="*.py" | wc -l

# Arquivo maior (target: <300 linhas)
find repos/ofertachina-api/app -name "*.py" -exec wc -l {} + | sort -n | tail -5

# Dependências não usadas
grep -r "^from \|^import " repos/ofertachina-api/app --include="*.py" | sed 's/from //; s/import //' | sort | uniq -c | sort -n

# Queries sem índices (grep por common patterns)
grep -r "select\|filter\|join" repos/ofertachina-api/app/repositories --include="*.py" | wc -l
```

### Fase 2: Análise de Estrutura (15 min)

1. **Separação de Concerns**
   - ✅ Existe `/routers` com endpoints separados por domínio?
   - ✅ Existe `/services` com lógica de negócio?
   - ✅ Existe `/repositories` com acesso a dados?
   - ✅ Existe `/models` com Pydantic + SQLAlchemy?
   - ⚠️ Se não, é uma RED FLAG

2. **God Routers/Services**
   - 🔴 Qual router tem mais endpoints? (Target: <10 por router)
   - 🔴 Qual service tem mais métodos? (Target: <15)
   - 🔴 Qual arquivo tem mais linhas? (Target: <300)
   - ⚠️ links.py > 500 linhas = REFACTOR NEEDED

3. **Lógica de Negócio Duplicada**
   - Grep por padrões: `affiliate commission`, `product validation`, `user authorization`
   - Compare entre serviços
   - Target: <15% duplicação

4. **Performance Red Flags**
   - ⚠️ Há N+1 queries? (Buscar loop + query dentro)
   - ⚠️ Há queries sem LIMIT em endpoints públicos?
   - ⚠️ Há .all() ou lazy loading desnecessário?

### Fase 3: Checklist de Qualidade (20 min)

Use o template padrão de **25 questões** em 5 categorias:

#### 1️⃣ ARQUITETURA (5 questões)

- Q1.1: Qual é o maior arquivo e quantas linhas tem?
- Q1.2: Qual service/router viola Single Responsibility Principle (SRP)?
- Q1.3: Existe separação clara entre routers/services/repositories?
- Q1.4: Quantos endpoints tem o maior router?
- Q1.5: Qual % da lógica está em services vs em routers?

#### 2️⃣ QUALIDADE DE CÓDIGO (5 questões)

- Q2.1: Cobertura de testes para routers/services? Qual %?
- Q2.2: Type hints estão presentes em todas as funções públicas?
- Q2.3: Docstrings existem para routers e services?
- Q2.4: Tratamento de erros é consistente (try/except/HTTPException)?
- Q2.5: Logging estruturado em pontos críticos (auth, payment, data changes)?

#### 3️⃣ SEGURANÇA (5 questões)

- Q3.1: Há validação de input em TODOS os endpoints POST/PUT/DELETE?
- Q3.2: Há autenticação/autorização em endpoints protegidos?
- Q3.3: Secrets (API keys, DB passwords) estão em Vault, não hardcoded?
- Q3.4: Há SQL injection protection? (SQLAlchemy ORM usado corretamente?)
- Q3.5: Há rate limiting em endpoints públicos?

#### 4️⃣ PERFORMANCE (5 questões)

- Q4.1: Há N+1 queries? Cite exemplos específicos.
- Q4.2: Há índices de banco de dados em colunas frequentemente filtradas?
- Q4.3: Há caching em endpoints que leem dados frequentemente (Redis)?
- Q4.4: Há paginação em endpoints que retornam coleções?
- Q4.5: Qual é o tempo médio de resposta dos 5 endpoints mais chamados?

#### 5️⃣ MANUTENIBILIDADE (5 questões)

- Q5.1: Há padrões consistentes entre routers/services/repositories?
- Q5.2: Qual é o ciclo de vida das conexões DB? (pooling, timeouts?)
- Q5.3: Há documentação clara sobre regras de negócio complexas?
- Q5.4: Qual é a cobertura de teste de integração vs unitários?
- Q5.5: Há dependências outdated em requirements.txt?

---

### Fase 4: Matriz de Priorização (5 min)

Para cada achado, classificar:

| Severidade | Descrição | Ação | Prazo |
|-----------|-----------|------|-------|
| 🔴 CRITICAL | Bug em auth, N+1 query em endpoint popular, hardcoded secrets | Deploy hotfix | < 24h |
| 🟠 HIGH | Missing validation, performance <2s, missing tests | Próximo sprint | < 1 semana |
| 🟡 MEDIUM | Code duplication, inconsistent patterns, minor perf issues | Backlog | < 2 semanas |
| 🟢 LOW | Documentation gaps, code style, minor refactoring | Nice-to-have | Próximo quarter |

---

## 📊 Relatório de Auditoria

Após completar as 4 fases, gerar relatório no Memory Bank com:

```markdown
# API Audit Report - [Data]

## Métricas Coletadas
- Total de linhas: XXX
- Total de endpoints: XX
- Maior arquivo: routers/links.py (XXX linhas)
- Cobertura de testes: XX%

## Achados Críticos
- [ ] Q3.1 (Segurança): Secrets hardcoded em [arquivo]
- [ ] Q4.1 (Performance): N+1 query em GET /offers (descrito em linhas XXX-YYY)

## Achados High Priority
- [ ] Q1.2: affiliate_service.py viola SRP (commission + validation + caching)
- [ ] Q4.3: Cache não implementado em GET /categories (15k requisições/dia)

## Padrões Positivos
✅ Separação clara entre routers/services/repositories
✅ Type hints presentes em 95% das funções
✅ Autenticação consistente em endpoints protegidos

## Ações Recomendadas
1. **Week 1**: Fixar Q3.1 (secrets) + Q4.1 (N+1)
2. **Week 2-3**: Refatorar affiliate_service.py
3. **Week 4**: Implementar cache para GET /categories
4. **Ongoing**: Aumentar cobertura de testes para >80%

## Próxima Auditoria
[Data prevista]
```

---

## 🔧 Verificação Prática (Optional)

Se quiser validar achados com código:

```bash
# Verificar N+1 queries em um endpoint
# (Ativa logging SQL verboso, faz request, conta quantas queries)
LOG_LEVEL=DEBUG curl -s http://localhost:3001/api/offers | grep "SELECT"

# Verificar cobertura de testes
cd repos/ofertachina-api
pytest --cov=app --cov-report=term-missing | grep -E "TOTAL|Missing"

# Verificar type hints
mypy app/routers/*.py --strict 2>&1 | head -20

# Verificar secrets hardcoded
grep -r "password\|token\|secret\|key" repos/ofertachina-api/app \
  --include="*.py" \
  | grep -v "\.env\|config\|import\|parameter" \
  | head -10
```

---

## 🎯 Integração com Agents

**Quem executa cada fase:**

| Fase | Agent | Tempo | Saída |
|------|-------|-------|-------|
| 1 (Métricas) | @backend | 10 min | Tabela de métricas |
| 2 (Estrutura) | @backend + @database | 15 min | Lista de red flags |
| 3 (Checklist) | @debug | 20 min | Respostas para 25 questões |
| 4 (Priorização) | @planner | 5 min | Matriz de ações |

**Workflow recomendado:**

```
@backend: Fase 1 + 2
  ↓
@debug: Fase 3 (com subagent para análise detalhada)
  ↓
@planner: Fase 4 + documentar em Memory Bank
  ↓
@backend: Implementar fixes (CRITICAL + HIGH)
  ↓
@reviewer: Validar mudanças
  ↓
@planner: Atualizar Memory Bank com status final
```

---

## 📅 Ciclo Trimestral

**Padrão recomendado:**

- **Semana 1**: Planejar auditoria, coletar métricas
- **Semana 2**: Executar análise detalhada (estrutura + segurança)
- **Semana 3**: Implementar fixes CRITICAL + HIGH
- **Semana 4**: Validar e documentar resultados

---

## 🔗 Referências

- **Memory Bank API**: `/home/admin/ofertasdachina/repos/ofertachina-api/docs/memory-bank-api/`
- **Vault Secrets**: `/home/admin/ofertasdachina/docs/memory-bank-infrastructure/VAULT-SECRETS-STRUCTURE.md`
- **Performance Tips**: `memory-bank-api/01-architecture.md` (seção Performance)
- **Testing Strategy**: `memory-bank-api/04-testing-strategy.md`

---

**Última Atualização**: 2025-12-12
