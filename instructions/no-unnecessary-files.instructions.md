---
applyTo: '**'
description: 'CRITICAL: Prevent creation of unnecessary .md files. All documentation must go in Memory Banks.'
---

# ⛔ REGRAS CRÍTICAS - NÃO CRIAR ARQUIVOS .md DESNECESSÁRIOS

**ATENÇÃO: Estas regras têm prioridade máxima e devem ser seguidas SEMPRE.**

---

## 🚫 Proibições Absolutas

### ❌ NÃO CRIAR Automaticamente

1. **README.md**: 
   - ❌ NÃO criar README.md em cada pasta
   - ❌ NÃO criar múltiplos READMEs por serviço
   - ✅ Apenas criar se explicitamente solicitado
   - ✅ Apenas 1 README por serviço/repo

2. **Arquivos de Documentação**:
   - ❌ NÃO criar `GUIDE.md`, `TUTORIAL.md`, `INSTRUCTIONS.md` automaticamente
   - ❌ NÃO criar `CHANGELOG.md`, `NOTES.md`, `SUMMARY.md` sem pedido
   - ❌ NÃO criar documentação "por precaução"

3. **Arquivos de Resumo**:
   - ❌ NÃO criar `SESSION-SUMMARY.md` após cada conversa
   - ❌ NÃO criar `CONSOLIDADO.md`, `FINAL.md`, `STATUS.md` repetidamente
   - ❌ NÃO criar múltiplas versões do mesmo documento
   - ❌ NÃO criar "resumos visuais" ou arquivos de sumário automaticamente
   - ❌ NÃO criar `/tmp/summary.txt` ou arquivos temporários de resumo

### ❌ NÃO EXIBIR Conteúdo de Arquivos

**PROIBIDO exibir conteúdo automaticamente na janela de contexto**:
- ❌ `cat arquivo.md` - NUNCA exibir conteúdo completo
- ❌ `cat > /tmp/summary.txt` - NUNCA criar e exibir summaries
- ❌ Output gigante de arquivos Markdown (>50 linhas)
- ❌ Listar conteúdo completo sem solicitação explícita
- ❌ Copiar/colar blocos grandes de texto de arquivos
- ❌ **"Aqui está o conteúdo de [arquivo]"** seguido de 200+ linhas

**Comportamento correto após atualização**:
```
✅ CORRETO: "Atualizei memory-bank-api/05-progress-log.md"
❌ ERRADO: "Atualizei o arquivo! Aqui está o conteúdo:\n[300 linhas...]"
```

**Quando exibir conteúdo é permitido**:
- ✅ Usuário pede explicitamente: "mostre o arquivo X"
- ✅ Usuário pede: "qual o conteúdo de Y?"
- ✅ Trechos pequenos (<20 linhas) para contexto quando necessário
- ✅ Diff específico quando relevante para a discussão

---

## ✅ Documentação Permitida

### Estrutura Oficial

**Toda documentação DEVE estar em Memory Banks**:

```
docs/
├── memory-bank/                    # Central (referência)
├── memory-bank-api/                # Backend API
├── memory-bank-bots/               # Telegram Bots
├── memory-bank-social/             # Social Media
├── memory-bank-frontend-ofertachina/
├── memory-bank-frontend-impressao3d/
├── memory-bank-infrastructure/     # Infisical, VPS, Docker
└── memory-bank-waha/               # WhatsApp
```

### Arquivos Permitidos (Exceções)

**Apenas estes arquivos .md são permitidos fora do Memory Bank**:

1. **README.md** (1 por repo/serviço):
   - Apenas se solicitado explicitamente
   - Deve referenciar o Memory Bank correspondente
   - Conteúdo minimalista (< 100 linhas)

2. **CONTRIBUTING.md** (opcional):
   - Apenas em repos públicos
   - Guidelines para contribuidores

3. **.github/ templates**:
   - `ISSUE_TEMPLATE.md`
   - `PULL_REQUEST_TEMPLATE.md`

**TODO o resto vai no Memory Bank!**

---

## 📝 Regras de Comportamento

### Quando o Usuário Pede "Crie um guia"

```
❌ NÃO: Criar arquivo `GUIA-COMPLETO.md` solto
✅ SIM: Adicionar/atualizar no Memory Bank apropriado
```

### Quando o Usuário Diz "Documente isso"

```
❌ NÃO: Criar `DOCUMENTACAO.md` ou `NOTAS.md`
✅ SIM: Atualizar arquivo existente no Memory Bank
```

### Quando Terminar uma Tarefa

```
❌ NÃO: Criar `SESSION-SUMMARY-2025-11-11.md`
❌ NÃO: Criar `WORK-DONE.md`
❌ NÃO: Criar `NEXT-STEPS.md`
❌ NÃO: Criar "resumo visual" com cat > /tmp/summary.txt
✅ SIM: Atualizar `activeContext.md` ou `progress.md` no Memory Bank
✅ SIM: Apenas responder ao usuário o que foi feito (sem criar arquivos)
```

### Quando o Usuário Pede Consolidação

```
❌ NÃO: Criar novo `CONSOLIDADO-FINAL-V2.md`
✅ SIM: Arquivar documentos antigos
✅ SIM: Atualizar documento existente no Memory Bank
```

---

## 🎯 Estrutura de Memory Bank

### Arquivos Padrão (Sempre Usar)

Cada Memory Bank tem esta estrutura:

```
memory-bank-{service}/
├── 00-overview.md           # O que é? Por quê? (começa aqui)
├── 01-architecture.md       # Design, componentes, fluxos
├── 02-components.md         # Módulos, classes, funções
├── 03-process.md            # Workflows, algoritmos
├── 04-active-context.md     # Estado atual, decisões
├── 05-progress-log.md       # Histórico de mudanças
├── 06-deployment.md         # Deploy, troubleshooting
└── 07-reference.md          # Links, recursos externos
```

### Como Adicionar Documentação

1. **Identificar o Memory Bank correto**:
   - Infraestrutura → `memory-bank-infrastructure/`
   - API → `memory-bank-api/`
   - Bots → `memory-bank-bots/`
   - Etc.

2. **Escolher arquivo apropriado**:
   - Visão geral → `00-overview.md`
   - Arquitetura → `01-architecture.md`
   - Estado atual → `04-active-context.md`
   - Histórico → `05-progress-log.md`

3. **Atualizar arquivo existente** (não criar novo)

---

## 🔒 Checklist Antes de Criar .md

Antes de criar QUALQUER arquivo `.md`, perguntar:

- [ ] O usuário pediu EXPLICITAMENTE para criar este arquivo?
- [ ] Este conteúdo não pode ir em um Memory Bank existente?
- [ ] Este arquivo não é duplicação de algo já existente?
- [ ] Este arquivo é realmente necessário ou é "por precaução"?

**Se qualquer resposta for NÃO, não criar o arquivo.**

---

## 💬 Respostas Corretas

### Usuário: "Documente o que fizemos hoje"

```
❌ ERRADO: "Vou criar um SESSION-SUMMARY.md..."
❌ ERRADO: "Vou criar um resumo visual em /tmp/summary.txt..."
✅ CORRETO: "Vou atualizar memory-bank-{service}/05-progress-log.md"
```

### Usuário: "Crie um guia de secrets"

```
❌ ERRADO: Criar `SECRETS-GUIDE.md` solto
✅ CORRETO: Criar em `memory-bank-infrastructure/00-INFISICAL-SECRETS-GUIDE.md`
```

### Usuário: "Consolide a documentação"

```
❌ ERRADO: Criar `CONSOLIDADO-FINAL.md`
✅ CORRETO: 
  1. Mover arquivos antigos para .archive/
  2. Atualizar Memory Banks existentes
  3. Não criar novos arquivos
```

---

## 🤖 USAR SUBAGENTS PARA ANÁLISE

**Antes de criar QUALQUER arquivo .md, use um subagent para análise:**

```
Use a subagent to analyze if this documentation should go in Memory Bank
or if it's a violation of the no-unnecessary-files rule.
```

**Subagent vai verificar:**
- ✅ Pertence a um Memory Bank existente?
- ✅ É realmente necessário ou pode ser inline documentation?
- ✅ Não é duplicação de conteúdo existente?
- ❌ É summary/notes/guide temporário? → PROIBIDO

**Exemplo correto:**
```
@reviewer Use a subagent to validate if "API-CHANGES.md" 
should exist or if content belongs in memory-bank-api/05-progress-log.md
```

---

## 🚨 Exemplos de Violações Comuns

### ❌ Proliferação de Arquivos

```
# NÃO FAZER ISTO:
docs/
├── API-GUIDE.md
├── API-REFERENCE.md
├── API-TUTORIAL.md
├── API-EXAMPLES.md
├── API-BEST-PRACTICES.md
├── API-TROUBLESHOOTING.md
└── README.md

# Tudo isso deveria estar em:
docs/memory-bank-api/
├── 00-overview.md      # Tutorial, exemplos
├── 01-architecture.md  # Best practices
└── 07-reference.md     # Reference, troubleshooting
```

### ❌ Sessões Documentadas Demais

```
# NÃO FAZER ISTO:
docs/
├── SESSION-2025-11-08.md
├── SESSION-2025-11-09.md
├── SESSION-2025-11-10.md
├── SESSION-2025-11-11-MORNING.md
├── SESSION-2025-11-11-AFTERNOON.md
└── CONSOLIDADO-FINAL-SESSION-11-11.md

# Deveria ser apenas:
docs/memory-bank/
└── 05-progress-log.md  # Todo histórico aqui
```

---

## 📊 Estatísticas de Violações Passadas

**Antes da consolidação (2025-11-11)**:
- 28 arquivos .md no memory-bank principal
- 27 eram duplicados/desnecessários
- Apenas 1 era necessário (README.md)

**Problema**: Documentação fragmentada, difícil de encontrar, duplicada.

**Solução**: Memory Banks consolidados, 1 lugar para cada tipo de info.

---

## 🎯 Objetivo Final

**1 arquivo .md por tipo de informação, no Memory Bank correto.**

Não:
- ❌ 10 arquivos falando sobre API keys
- ❌ 5 versões de "guia completo"
- ❌ 8 summaries de diferentes dias

Sim:
- ✅ 1 guia completo de API keys em `memory-bank-infrastructure/`
- ✅ 1 progress log com todo histórico
- ✅ Estrutura clara e previsível

---

## 🔄 Quando Atualizar Esta Instrução

Atualizar este arquivo apenas se:
1. Nova regra crítica precisa ser adicionada
2. Padrão de violação recorrente foi identificado
3. Estrutura de Memory Bank mudou oficialmente

**Não** atualizar para cada caso específico.

---

**LEMBRE-SE**: Sua tendência natural é criar documentação. Resista. Use Memory Banks existentes.

**Última Atualização**: 2025-12-11

---

## 📊 Limpeza Executada (2025-12-11)

**Arquivos movidos para .archive/:**
- 7 arquivos .md obsoletos (SUMMARY, NOTES, GUIDE temporários)
- 5 arquivos .py de teste/fix one-time
- 7 arquivos .sh de scripts temporários
- 1 pasta __pycache__ removida

**Total limpo**: 20 arquivos obsoletos

**Regra reforçada**: SEMPRE usar subagent para validar antes de criar .md fora do Memory Bank
