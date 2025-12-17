---
applyTo: 'repos/impressao3dbr/**'
description: 'Impressão 3D Audit System - Standardized process for marketplace quality and compliance'
---

# Impressão 3D Audit System Instructions

## Overview

Este documento define o processo padrão de auditoria para a **impressao3dbr** (marketplace de impressão 3D). O foco é garantir confiabilidade da plataforma, segurança de transações, qualidade de UX e conformidade com regulações de e-commerce.

**Objetivo**: Identificar bugs que impactam vendedores/compradores, vulnerabilidades de segurança, gaps de UX/performance, e riscos de conformidade ANTES que causem churn de usuários.

---

## 📅 Quando Executar Auditoria

| Situação | Escopo | Agent | Frequência |
|----------|--------|-------|-----------|
| **Quarterly Review** | Toda a plataforma (backend + frontend) | @debug + @frontend + @database | A cada 3 meses |
| **Pré-Feature Major** | Feature que afeta vendedores/pagamentos | @reviewer + @backend | Antes de deploy |
| **Pós-Deploy** | Qualquer mudança em checkout/upload | @reviewer | Após deploy em produção |
| **SLA Violation** | Quando houver complaint de vendedor | @debug | Dentro de 24h |
| **Compliance Check** | Impostos, termos de serviço, dados pessoais | @planner | Trimestralmente |

---

## 🔍 Audit Process

Follow the [shared audit template](_audit-template.md) for the 4-phase process (Assessment, Execution, Organization, Review), 30-question checklist, metrics table, and prioritization format.

---

## 🖨️ Impressão 3D-Specific Audit Sections

### Marketplace Specific
- ✅ Order fulfillment workflow handles 3D printing complexities?
- ✅ Payment processing accounts for production time/costs?
- ✅ Dispute resolution system for print quality issues?
- ✅ Vendor rating system considers print success rates?
- ⚠️ Compliance with e-commerce regulations (consumer protection)?

### STL/OBJ Processing
- ✅ File validation prevents corrupted/malicious STL files?
- ✅ 3D model preview generation works reliably?
- ✅ File size limits appropriate for 3D models?
- ✅ Format conversion (STL↔OBJ) maintains quality?
- ⚠️ Processing handles large/complex models without timeouts?

---

## 🤖 Subagent Usage

### Decision Matrix
- Use @frontend for UI/UX and file upload flows
- Use @backend for marketplace logic and payment processing
- Use @database for data integrity and performance

### Workflow
```
@frontend: UI & file handling
  ↓
@backend: Business logic & payments
  ↓
@database: Data & performance
  ↓
@planner: Prioritize & document
```

---

## 📋 Output Format

```markdown
## 📋 IMPRESSAO3D AUDIT REPORT
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

- Save reports in `memory-bank/audit-YYYY-MM-DD.md`
- Update Memory Bank with findings
- Escalate marketplace/security issues to @planner/@reviewer

### Fase 1: Coleta de Métricas (10 min)

Use comandos no terminal para coletar dados básicos:

```bash
# Total de linhas (backend + frontend)
find repos/impressao3dbr/backend repos/impressao3dbr/frontend -name "*.py" -o -name "*.tsx" -o -name "*.ts" | xargs wc -l | tail -1

# Total de endpoints API
grep -r "^@router\|^@app" repos/impressao3dbr/backend --include="*.py" | wc -l

# Total de componentes React
find repos/impressao3dbr/frontend/src/components -name "*.tsx" | wc -l

# Total de páginas
find repos/impressao3dbr/frontend/src/pages -name "*.tsx" | wc -l

# Arquivo maior
find repos/impressao3dbr -name "*.py" -o -name "*.tsx" | xargs wc -l | sort -n | tail -5

# Modelos de dados
grep -r "class.*Model\|interface.*{" repos/impressao3dbr --include="*.py" --include="*.ts" | wc -l

# Verificar cobertura de testes
cd repos/impressao3dbr && pytest --cov --cov-report=term-missing 2>&1 | grep -E "TOTAL|coverage"
```

### Fase 2: Análise de Estrutura (15 min)

1. **Separação de Concerns - Backend**
   - ✅ Routers separados por domínio (printers, designs, orders)?
   - ✅ Services com lógica de negócio?
   - ✅ Repositories para acesso a dados?
   - ✅ Modelos Pydantic + SQLAlchemy separados?
   - ⚠️ Se não, é RED FLAG

2. **Separação de Concerns - Frontend**
   - ✅ Componentes separados por domínio (Printer, Design, Checkout)?
   - ✅ Páginas separadas por rota?
   - ✅ Custom hooks para lógica reutilizável?
   - ✅ Context/Store para estado global?
   - ⚠️ Se tudo em um arquivo, é RED FLAG

3. **God Classes/Components**
   - 🔴 Maior arquivo backend? (Target: <300 linhas)
   - 🔴 Maior componente frontend? (Target: <200 linhas)
   - 🔴 Qual página tem mais hooks? (Target: <10)
   - ⚠️ PrinterDetail > 400 linhas = REFACTOR NEEDED

4. **Critical Paths**
   - ⚠️ Upload de STL/OBJ é seguro? (validação de arquivo)
   - ⚠️ Checkout é seguro? (CSRF, validação de pagamento)
   - ⚠️ Registro de vendedor é seguro? (verificação de identidade)

### Fase 3: Checklist de Qualidade (20 min)

Use o template padrão de **30 questões** em 6 categorias:

#### 1️⃣ ARQUITETURA (5 questões)

- Q1.1: Backend e frontend estão bem separados?
- Q1.2: Há clara separação entre UI e lógica de negócio?
- Q1.3: Qual é o padrão de estado (Context/Redux/Zustand)?
- Q1.4: Há reutilização de componentes ou muita duplicação?
- Q1.5: Qual % da lógica está em services vs em routers/componentes?

#### 2️⃣ SEGURANÇA - BACKEND (5 questões)

- Q2.1: Upload de arquivos valida tipo (STL/OBJ), tamanho, conteúdo?
- Q2.2: Há autenticação em todos os endpoints que modificam dados?
- Q2.3: Há autorização? (Vendedor pode editar só seus produtos?)
- Q2.4: Secrets estão em Vault, não em código?
- Q2.5: Há proteção contra CSRF/CORS misconfiguration?

#### 3️⃣ SEGURANÇA - FRONTEND (5 questões)

- Q3.1: Há validação de input em formulários?
- Q3.2: Tokens JWT são armazenados seguramente (não localStorage para sensível)?
- Q3.3: Há proteção contra XSS em exibição de dados do usuário?
- Q3.4: Há rate limiting em requisições?
- Q3.5: Há logging de ações sensíveis (upload, pagamento, deleção)?

#### 4️⃣ PERFORMANCE (5 questões)

- Q4.1: Há cache de lista de impressoras/designs (Redis)?
- Q4.2: Há paginação em endpoints que listam dados?
- Q4.3: Há lazy loading em componentes (images, modelos 3D)?
- Q4.4: Qual é o time-to-interactive da página inicial?
- Q4.5: Há bundling optimization (code splitting, tree shaking)?

#### 5️⃣ UX & CONFORMIDADE (5 questões)

- Q5.1: Checkout é acessível (WCAG 2.1 AA)?
- Q5.2: Há termos de serviço + política de privacidade visíveis?
- Q5.3: Há notificação clara de dados coletados (LGPD/GDPR)?
- Q5.4: Upload de documento do vendedor é feito seguramente?
- Q5.5: Há processo claro para refund/disputa?

#### 6️⃣ TESTES (5 questões)

- Q6.1: Qual % de cobertura em testes unitários?
- Q6.2: Há testes de integração para fluxo de checkout?
- Q6.3: Há testes E2E para upload de arquivo + publicação?
- Q6.4: Há testes de segurança (SQL injection, XSS, CSRF)?
- Q6.5: Há testes de performance (load testing)?

---

### Fase 4: Matriz de Priorização (5 min)

Para cada achado, classificar:

| Severidade | Descrição | Ação | Prazo |
|-----------|-----------|------|-------|
| 🔴 CRITICAL | Bug em checkout, vulnerabilidade de upload, dados expostos | Hotfix imediato | < 4h |
| 🟠 HIGH | Missing validation, performance <3s, auth gap | Próximo sprint | < 1 semana |
| 🟡 MEDIUM | UX issue, missing logging, minor perf | Backlog | < 2 semanas |
| 🟢 LOW | Code style, documentation, refactoring | Nice-to-have | Próximo quarter |

---

## 📊 Relatório de Auditoria

Após completar as 4 fases, gerar relatório no Memory Bank:

```markdown
# Impressão 3D Audit Report - [Data]

## Métricas Coletadas
- Backend: XXX linhas | Frontend: XXX linhas
- Endpoints: XX | Componentes React: XX | Páginas: XX
- Cobertura de testes: XX%
- Maior arquivo: [nome] (XXX linhas)

## Achados Críticos
- [ ] Q2.1 (Segurança Backend): Upload não valida tipo de arquivo
- [ ] Q5.2 (Conformidade): Termos de serviço não acessível

## Achados High Priority
- [ ] Q4.3: Lazy loading não implementado para imagens de modelos 3D
- [ ] Q6.3: Sem testes E2E para upload + publicação

## Padrões Positivos
✅ Separação clara backend/frontend
✅ Type hints em 90% do backend
✅ Autorização consistente em endpoints protegidos

## Ações Recomendadas
1. **Week 1**: Fixar Q2.1 (validação upload) + Q5.2 (termos)
2. **Week 2**: Implementar lazy loading (Q4.3)
3. **Week 3**: Adicionar testes E2E para checkout
4. **Ongoing**: Aumentar cobertura de testes para >75%

## Próxima Auditoria
[Data prevista]
```

---

## 🔧 Verificação Prática

Validar achados com código:

```bash
# Verificar validação de upload
grep -r "accept=\|allowed_extensions\|validate_file" repos/impressao3dbr --include="*.py" --include="*.tsx"

# Verificar testes E2E
find repos/impressao3dbr -name "*e2e*" -o -name "*cypress*"

# Verificar lazy loading
grep -r "lazy\|Suspense" repos/impressao3dbr/frontend/src --include="*.tsx"

# Verificar conformidade LGPD
grep -r "privacidade\|consent\|cookie" repos/impressao3dbr --include="*.tsx" --include="*.py" | head -5

# Verificar performance (build size)
cd repos/impressao3dbr/frontend && npm run build 2>&1 | grep -E "gzip|minified"
```

---

## 🎯 Integração com Agents

**Quem executa cada fase:**

| Fase | Agent | Tempo | Saída |
|------|-------|-------|-------|
| 1 (Métricas) | @backend + @frontend | 10 min | Tabela de métricas |
| 2 (Estrutura) | @backend + @frontend + @database | 15 min | Lista de red flags |
| 3 (Checklist) | @debug | 20 min | Respostas para 30 questões |
| 4 (Priorização) | @planner | 5 min | Matriz de ações |

**Workflow recomendado:**

```
@backend + @frontend: Fase 1 + 2
  ↓
@debug: Fase 3 (com subagent para análise detalhada)
  ↓
@planner: Fase 4 + documentar em Memory Bank
  ↓
@backend + @frontend: Implementar fixes (CRITICAL + HIGH)
  ↓
@reviewer: Validar mudanças com testes E2E
  ↓
@planner: Atualizar Memory Bank com status final
```

---

## 📅 Ciclo Trimestral

**Padrão recomendado:**

- **Semana 1**: Planejar auditoria, coletar métricas
- **Semana 2**: Executar análise detalhada (segurança + UX + compliance)
- **Semana 3**: Implementar fixes CRITICAL + HIGH
- **Semana 4**: Validar com testes + documentar resultados

---

## 🔗 Referências

- **Memory Bank Impressão 3D**: `/home/admin/ofertasdachina/repos/impressao3dbr/docs/memory-bank/`
- **Vault Secrets**: `/home/admin/ofertasdachina/docs/memory-bank-infrastructure/VAULT-SECRETS-STRUCTURE.md`
- **LGPD/Conformidade**: `memory-bank/00-overview.md` (seção Legal)
- **Testing Strategy**: `memory-bank/03-process.md` (seção Testing)

---

**Última Atualização**: 2025-12-12
