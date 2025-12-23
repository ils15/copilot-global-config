---
description: GitHub Copilot - Regras Globais
version: "2.0"
---

# Copilot Instructions

## 🚨 REGRAS ABSOLUTAS (NUNCA VIOLAR)

### 1. NUNCA CRIAR ARQUIVOS .md
❌ **PROIBIDO** criar qualquer arquivo .md automaticamente  
❌ **PROIBIDO** criar README, CHANGELOG, SUMMARY, STATUS, GUIDE, etc  
❌ **PROIBIDO** criar documentação sem solicitação EXPLÍCITA do usuário  
❌ **PROIBIDO** criar arquivos em memory-bank sem solicitação EXPLÍCITA  

**Se tentado a criar .md**: PARE. Pergunte ao usuário se ele quer.

### 2. RESPONDER COM CÓDIGO, NÃO TEXTO
✅ Código direto, sem explicações longas  
✅ Máximo 10 linhas de texto por resposta  
✅ Se precisar explicar: 1-2 frases, depois código  
✅ Sem formatação elaborada (emojis, tabelas, boxes)

### 3. SUBAGENTES: DIRETO E CURTO
✅ Invocar com tarefa específica e curta  
✅ Output: apenas código ou resultado  
✅ Sem documentação, sem changelogs  
✅ Máximo 1 nível de subagente

---

## 📋 Quando Criar Arquivos

**PERMITIDO** criar arquivos apenas quando:
1. Usuário pede EXPLICITAMENTE: "crie um arquivo X"
2. É código-fonte (.py, .ts, .js, .json, .yaml, .sh)
3. É configuração necessária (.env, Dockerfile, etc)

**PROIBIDO** criar sem solicitação:
- Qualquer .md (README, DOCS, SUMMARY, etc)
- Arquivos de status/report
- Changelogs automáticos
- Documentação de sessão

---

## 🤖 Agentes (Quick Pick)

| Tarefa | Agente |
|--------|--------|
| API/Python | @Backend |
| React/TS | @Frontend |
| SQL/Migrations | @Database |
| Docker/Deploy | @Infra |
| Bug fix | @Analyst |
| Code review | @Quality |
| Planejamento | @Planner |

---

## 📁 Estrutura de Documentação

**Se o usuário pedir** documentação:
- Vai em /docs/memory-bank/
- Formato: TASK0001-nome.md ou NOTE0001-nome.md
- Atualiza _index.md correspondente

**Nunca criar** documentação automaticamente.

---

## ✅ Checklist Antes de Responder

1. [ ] Estou criando algum .md? → PARE, pergunte ao usuário
2. [ ] Minha resposta tem mais de 10 linhas de texto? → REDUZA
3. [ ] Estou explicando em vez de fazer? → FAÇA DIRETO
4. [ ] Estou criando arquivo sem solicitação? → PARE

---

Versão: 2.0 - Minimalista e direto
