---
applyTo: '**'
description: 'Sistema de Roteamento Automático com Context-Isolated Subagents'
---

# 🤖 Auto Subagent Routing - Context-Isolated Integration

## Visão Geral

Sistema de roteamento automático que integra com **Context-Isolated Subagents** do VS Code. Cada subagente opera de forma isolada com seu próprio context window, otimizando a gestão de contexto para tarefas complexas.

**Vantagens:**
- ✅ Cada subagente tem context window separado (não polui contexto principal)
- ✅ Autonomia completa (sem pausa para confirmação do usuário)
- ✅ Retorna apenas resultado final ao chat principal
- ✅ Perfeito para tarefas de research, analysis, refactoring

---

## Como Funciona

### Fluxo de Execução

```
User Chat (Main Session)
    ↓
Auto Router (Analyzes task)
    ↓ (confidence >= 80%)
runSubagent Tool
    ↓
Subagent (Isolated Context)
    └─ Own context window
    └─ Access to same tools
    └─ No async/background
    └─ Returns final result only
    ↓
Result back to Main Chat
```

### Exemplo Prático

**Usuário em Chat Principal:**
```
"Use a subagent to research the best authentication methods 
for our FastAPI backend. Then provide a 1-page summary."
```

**Sistema:**
1. ✅ Detecta: "subagent" + "research" + "backend"
2. ✅ Seleção automática: Backend Researcher Subagent (90% confiança)
3. ✅ Subagent executa autonomamente:
   - Lê documentação FastAPI
   - Pesquisa melhores práticas JWT
   - Analisa segurança
   - Gera relatório
4. ✅ Retorna ao chat principal: "Aqui está o resumo de 1 página..."

---

## 🔍 Transparência e Comunicação de Subagentes

**NOVO PADRÃO (2025-12-15)**: Sempre comunicar qual subagente está sendo usado e o quê ele está fazendo.

### Quando Invocar um Subagente

Antes de chamar o subagente, comunicar claramente:

```
🤖 Subagente em uso: [Nome do Agente]
📋 Tarefa: [O que está fazendo, em 1-2 linhas]
⏳ Processando...
```

### Quando o Subagente Retorna

Apresentar resultado da forma estruturada:

```
✅ [Nome do Agente] completou:
   - [Resultado 1]
   - [Resultado 2]
   - [Resultado 3]
```

### Exemplos Reais

**1. Análise de Código (Debug Subagent)**
```
🤖 Subagente: debug
📋 Analisando routers/links.py para duplicação de código e problemas N+1
⏳ Processando...

✅ debug completou:
   - Encontrou 5 funções duplicadas (linhas 23, 45, 67, 89, 102)
   - Identificou 3 queries N+1 em endpoints de lista
   - Sugeriu consolidação em 2 arquivos novos
```

**2. Validação de Mudanças (Reviewer Subagent)**
```
🤖 Subagente: Reviewer
📋 Validando 3 arquivos modificados em services/ para segurança e lógica
⏳ Processando...

✅ Reviewer completou:
   - Código validado: sem vulnerabilidades críticas
   - Cobertura de testes: 82% (OK)
   - Linha mais complexa: função X no arquivo Y (refatorar? recomendado)
```

**3. Planejamento (Planner Subagent)**
```
🤖 Subagente: Planner
📋 Criando plano de implementação de autenticação JWT (4 fases)
⏳ Processando...

✅ Planner completou:
   - Fase 1: Setup e models (2 dias)
   - Fase 2: Endpoints de login/refresh (1 dia)
   - Fase 3: Middleware e proteção de rotas (1 dia)
   - Fase 4: Testes e documentação (1 dia)
   - Plano completo atualizado em Memory Bank
```

**4. Análise de Bot Ecosystem (Debug Subagent para auditoria)**
```
🤖 Subagente: debug
📋 Auditando todos 4 bots (alertas, ofertas, affiliate, username) em paralelo
⏳ Processando... (análise complexa, ~3-5 min)

✅ debug completou:
   - alertas_bot: 5 issues críticas (race conditions, pool exhaustion)
   - ofertas_bot: 4 high-priority issues (duplicate code, bare exceptions)
   - affiliate_bot: 3 medium issues (AI fallback gaps, retry logic)
   - username_bot: ✅ Saudável após fixes (85/100 score)
```

### Por Que Comunicar?

- **Transparência**: Você sabe exatamente o que está acontecendo
- **Rastreabilidade**: Fácil ver qual agent processou cada coisa
- **Debugging**: Se algo der errado, sabemos onde procurar
- **Performance**: Você acompanha progresso de tarefas longas
- **Confiança**: Não é uma "caixa preta" — cada passo é visível

---

## 🎯 Padrões de Uso

### Padrão 1: Simple Task (no subagent needed)
```
"Create GET /users endpoint"
↓
@backend executa diretamente no chat (quick response)
```

### Padrão 2: Research Task (subagent)
```
"Use a subagent to research authentication methods"
↓
runSubagent invokes Backend Research Subagent
↓ (isolated context)
Subagent returns final summary
```

### Padrão 3: Complex Multi-Step (subagent)
```
"Run the planner subagent to create implementation plan for JWT auth"
↓
runSubagent invokes Planner Subagent
↓ (isolated context, full access to Memory Bank)
Planner returns: structured plan + task breakdown
```

### Padrão 4: Analysis Task (subagent)
```
"Use a subagent to analyze the 89 API files and identify code quality issues"
↓
runSubagent invokes Code Quality Subagent
↓ (isolated context, can read all files)
Subagent returns: structured findings + recommendations
```

---

## 🛠️ Setup no VS Code

### Passo 1: Habilitar Custom Agents em Subagents

**settings.json:**
```json
{
  "chat.customAgentInSubagent.enabled": true,
  "chat.agentSessionsViewLocation": "primarySidebar"
}
```

### Passo 2: Configurar Agents como .agent.md Files

Cada agente tem seu próprio `.agent.md` file com configuração:

**`.github/agents/backend.agent.md`:**
```yaml
---
name: Backend
description: "FastAPI, Python, async, services, repositories"
instructions: "You are a backend specialist..."
tools:
  - read_file
  - write_file
  - grep_search
  - run_in_terminal
  - list_code_usages
infer: true  # ⭐ Permite usar em subagents
---
```

### Passo 3: Usar runSubagent em Chat

No chat do VS Code:

```
/runSubagent Use the Backend Agent to analyze url_service.py and identify refactoring opportunities
```

Ou invoke automático via prompt:

```
"Use a subagent to review the authentication implementation for security issues"
```

---

## 🤖 Subagents Disponíveis

| Subagent | Use Cases | Context Window | Return Style |
|----------|-----------|-----------------|------------|
| **Backend Research** | Analyze code, research libraries, identify bugs | Full file access | Structured findings |
| **Frontend Analysis** | React patterns, TypeScript issues, UI/UX | Full component access | Recommendations |
| **Database Optimizer** | Query analysis, schema review, migration planning | Full schema access | Optimization report |
| **Infra Auditor** | Docker config, security, performance | Full config access | Audit report |
| **Planner Coordinator** | Implementation plans, architecture design, roadmaps | Full Memory Bank access | Structured plan |
| **Code Quality Reviewer** | Bug detection, security issues, code style | Full codebase access | Issue summary |

---

## 📋 Padrões de Prompt para Subagents

### Research Pattern
```
"Use a subagent to research [topic]. Look for [specific aspects]. 
Return a 1-page summary with key findings."
```

**Exemplo:**
```
"Use a subagent to research best practices for FastAPI async middleware.
Look for: error handling, performance optimization, security.
Return a 1-page summary with 3-5 key recommendations."
```

### Analysis Pattern
```
"Run a subagent to analyze [target]. Focus on: [specific areas].
Return: structured findings with examples from the code."
```

**Exemplo:**
```
"Run a subagent to analyze the url_service.py file.
Focus on: code duplication, function responsibilities, 
performance bottlenecks.
Return: 5-10 specific findings with line references."
```

### Planning Pattern
```
"Use the Planner subagent to create [deliverable] for [feature].
Include: [specific sections]. Use Memory Bank as reference."
```

**Exemplo:**
```
"Use the Planner subagent to create implementation plan for JWT authentication.
Include: architecture diagram, step-by-step tasks, risk analysis.
Reference the Memory Bank for project context."
```

### Review Pattern
```
"Run a subagent to review [code/design] for [criteria].
Check: [specific checks]. Return: pass/fail with details."
```

**Exemplo:**
```
"Run a subagent to review the new affiliate_service.py for security.
Check: input validation, auth requirements, SQL injection risks.
Return: security audit report."
```

---

## 🎮 Comando Automático no Chat

### Exemplo 1: Análise de Código

```
@backend Use a subagent to analyze routers/links.py for:
- Code duplication (find similar endpoints)
- N+1 query problems
- Missing error handling
- Endpoint consolidation opportunities

Return: structured findings with line numbers
```

**Subagent vai:**
1. Ler arquivo completo
2. Buscar duplicações
3. Analisar queries
4. Retornar relatório ao chat

### Exemplo 2: Planejamento Complexo

```
@planner Use a subagent to plan the API refactoring:
- Break down 89 files analysis into phases
- Identify critical dependencies
- Create implementation roadmap
- Update Memory Bank with plan

Return: structured refactoring plan
```

**Subagent vai:**
1. Acessar todos os arquivos
2. Analisar dependências
3. Criar plan
4. Atualizar docs

### Exemplo 3: Research + Implementation

```
@backend Use a subagent to:
1. Research current FastAPI best practices for pagination
2. Analyze our current pagination implementation
3. Identify gaps
4. Provide 3 refactoring recommendations

Return: comparison table + code examples
```

---

## ⚙️ Configuração Automática no .prompt.md

Para prompts reutilizáveis com subagents:

**`.github/prompts/analyze-api-code.prompt.md`:**
```markdown
---
name: "API Code Analysis"
description: "Comprehensive analysis of API codebase"
tools:
  - read_file
  - grep_search
  - list_code_usages
  - runSubagent  # ⭐ Enables subagent invocation
---

# API Code Analysis

You are analyzing the ofertachina-api codebase.

Use a subagent to:
1. Analyze all files in `backend/app/services/` for code duplication
2. Identify God Classes and overly complex functions
3. Find N+1 query issues
4. Detect missing error handling

Return: structured findings with specific recommendations.
```

---

## 🔄 Fluxo Avançado: Subagent Chain

```
Main Chat
   ↓
"Plan refactoring using Planner subagent"
   ↓
Planner Subagent (isolated context)
   ├─ Creates refactoring plan
   ├─ Identifies tasks
   └─ Returns to main chat
   ↓
"Now use Backend subagent to implement Phase 1"
   ↓
Backend Subagent (isolated context)
   ├─ Implements Phase 1
   ├─ Runs tests
   └─ Returns results
   ↓
"Use Reviewer subagent to validate"
   ↓
Reviewer Subagent (isolated context)
   ├─ Reviews code
   ├─ Checks quality
   └─ Returns report
```

---

## 🚨 Boas Práticas

### ✅ Quando Usar Subagent
- Análise de múltiplos arquivos (> 3 arquivos)
- Research que precisa de contexto isolado
- Tarefas que geram muito output (> 500 tokens)
- Análise que não precisa de confirmação do usuário
- Planejamento estratégico com acesso a Memory Bank

### ❌ Quando NÃO Usar Subagent
- Tarefas simples (< 50 linhas, 1 arquivo)
- Tudo que precisa de feedback imediato do usuário
- Quick fixes ou hotpatches
- Conversas interativas

### 📋 Checklist para Subagent Prompt

```
☐ Objetivo clara (1 sentença)
☐ Escopo específico (quais arquivos/áreas)
☐ Critérios de sucesso (como validar resultado)
☐ Formato de retorno especificado (1-page, table, list, etc)
☐ Sem pausa para confirmação (subagent é autônomo)
☐ Context suficiente para executar sozinho
```

---

## 📊 Exemplos de Prompts Prontos

### Research Backend Libraries
```
Use a subagent to research Pydantic v2 validation best practices.
Focus on: custom validators, error handling, performance.
Return: 1-page summary with 3 code examples.
```

### Analyze API Endpoints
```
Run a subagent to analyze routers/ directory.
Check: duplicate endpoints, missing validations, error consistency.
Return: findings in table format (endpoint, issue, severity, fix).
```

### Plan Database Migration
```
Use the Database subagent to plan migration for user authentication.
Include: schema changes, index strategy, rollback plan.
Return: migration file outline + notes.
```

### Audit Codebase Security
```
Run a subagent for security audit of api/services/.
Check: input validation, SQL injection, auth gaps, secrets exposure.
Return: risk assessment + remediation priority list.
```

---

## 🔗 Referências

- [VS Code Context-Isolated Subagents Docs](https://code.visualstudio.com/docs/copilot/chat/chat-sessions#_contextisolated-subagents)
- [VS Code Chat Sessions Management](https://code.visualstudio.com/docs/copilot/chat/chat-sessions)
- [runSubagent Tool Documentation](https://code.visualstudio.com/docs/copilot/chat/chat-sessions#_invoke-a-subagent)

---

## 💡 Quick Start

1. **Habilitar em settings.json:**
   ```json
   { "chat.customAgentInSubagent.enabled": true }
   ```

2. **No chat, escrever:**
   ```
   Use a subagent to analyze the api codebase for quality issues
   ```

3. **Subagent executa autonomamente**

4. **Resultado retorna ao chat principal**

---

**Status**: Padrão pronto para uso via VS Code Chat sessions 🚀

