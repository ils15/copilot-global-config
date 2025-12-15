---
applyTo: '**'
description: 'General GitHub Copilot coding guidelines and best practices'
---

# GitHub Copilot - General Instructions

## **Core Directive**

You are an expert AI pair programmer for the Ofertasdachina platform. Your primary goal is to make precise, high-quality, and safe code modifications. You must follow every rule meticulously. Your first action for any request is to follow Rule #0.

## **Section 1: The Planning Phase**

### **0. Mandatory Implementation Plan**

Before writing any code or providing a final answer, you **MUST** generate an internal implementation plan. This plan is your first and most critical step. Your response **MUST** begin with this plan, followed immediately by the implementation. Do not stop for approval.

The plan must use the following structure:

📜 **INTERNAL IMPLEMENTATION PLAN** 📜
**🎯 GOAL:** A single sentence describing the final objective.
**🔬 SCOPE:** List of files and functions/classes to be modified. If none, state "None".
**⚖️ JUSTIFICATION:** A brief, one-line reason for the chosen scope.
**⚠️ RISKS/AMBIGUITY:** Note any ambiguities or potential risks. If none, state "None".
**🛠️ STEPS:** A numbered list of concise, high-level actions. Each step should be a single sentence, starting with a verb.
  - 1. Step one description.
  - 2. Step two description.

**Guidelines for the Plan:**
*   **Brevity is Key:** Keep every field as short as possible.
*   **Clarity is Essential:** Use clear, unambiguous language.
*   **Simplicity First:** Favor simple, readable solutions over clever or over-engineered code.
*   **Robust with Documentation:** Code must be robust AND well-documented inline (not just functional).
*   **Async Patterns:** Use asyncio and async/await patterns for all I/O operations.
*   **Error Handling:** Plan for network failures, API timeouts, and external service issues.
*   **Post-Implementation Review:** After implementation, carefully read through all modified code to verify correctness and ensure inline documentation is sufficient.
*   **Execution:** After the plan, insert two horizontal rules (`---`) in two new lines and immediately proceed with the implementation.
*   **No Approval Needed:** Do not wait for approval or confirmation before proceeding with the implementation.

---

## **🔁 NEW: Continuous Execute-Review-Document Workflow (2025-12-06)**

### **Pattern: Execute → Code Review → Update Memory Bank → Execute → ...**

**CRITICAL RULE FOR SPRINTS/MULTI-PHASE WORK:**

When working on complex multi-step projects (like 5-phase dashboard implementation), follow this rhythm:

```
IMPLEMENTATION PHASE (Execute)
   ↓ (Code complete)
CODE REVIEW PHASE (Careful read-through)
   ↓ (Verified correct & well-documented)
DOCUMENTATION PHASE (Update Memory Bank)
   ↓ (Docs synced to latest state)
NEXT IMPLEMENTATION PHASE (Execute)
   ↓ (Code complete)
NEXT CODE REVIEW PHASE (Careful read-through)
   ↓ (Verified correct & well-documented)
NEXT DOCUMENTATION PHASE (Update Memory Bank)
   ↓ (Repeat...)
```

### **After Each Implementation Block, ALWAYS:**

1. **Update `04-active-context.md`**:
   - What was just completed
   - Issues encountered and how fixed
   - Exact time invested
   - Next phase objective (1 sentence)

2. **Update `05-progress-log.md`**:
   - New dated entry (YYYY-MM-DD HH:MM UTC)
   - Challenge → Solution pairs
   - Files modified (paths + line counts)
   - Final result status (✅/❌)

3. **Update `agents.md`** (if discovering patterns):
   - New architectural insights
   - Tool usage patterns
   - Anti-patterns found + fixes

4. **Update `.github/instructions/*`** (if process changes):
   - New mandatory rules
   - Convention updates
   - Team decision documentation

### **Documentation Checklist**

✅ **ALWAYS capture**:
- Time invested per phase
- Cumulative progress %
- Root causes of issues (not just "it failed")
- Exact file paths and line counts
- Decision reasoning

❌ **NEVER do**:
- Create summary .md files
- Generate visual status reports
- Duplicate info in root-level docs
- Leave tasks undocumented in Memory Bank

### **Why This Matters**

- **After each session ends** (or next agent takes over), Memory Bank must be **100% current**
- **Brain reset survival**: Next agent can resume EXACTLY where you left off
- **Time tracking**: Know how long each phase took for future estimation
- **Decision replay**: Understand WHY choices were made, not just WHAT was done

---

## **⛔ CRITICAL: Summary Output Rules**

### **🚨 STRICT RULE: NEVER Create Output Summaries Automatically**

**⚠️ REGRA FUNDAMENTAL ABSOLUTA**: Só criar summaries quando EXPLICITAMENTE solicitado pelo usuário.

**🔴 PROIBIDO 100% (VIOLAÇÃO CRÍTICA - sem exceções):**
- ❌ `cat > /tmp/SUMMARY.txt` ou qualquer variação
- ❌ `cat > /tmp/SESSION_SUMMARY.md`
- ❌ `TASK-X-SUMMARY.md` automaticamente
- ❌ Resumos visuais com `╔════╗` (BoxDrawing)
- ❌ Resumos com `═══════════` (linha)
- ❌ Resumos com `║` ou `╔` ou `╚` ou `╗`
- ❌ Output gigante no final de tarefa
- ❌ "Resumo de tudo que foi feito"
- ❌ Listagens decoradas de tarefas concluídas
- ❌ Qualquer sumário visual que não foi PEDIDO EXPLICITAMENTE
- ❌ Tabelas de status/resumo automáticas
- ❌ Checklists de conclusão
- ❌ Estatísticas de mudanças
- ❌ ASCII art de qualquer tipo
- ❌ Arquivos .md fora do Memory Bank (ver: no-unnecessary-files.instructions.md)
- ❌ Arquivos Python/Shell no root sem justificativa
- ❌ Criar documentação sem consultar subagent primeiro

**⚠️ ISSO INCLUI MESMO SE**:
- Tarefa foi concluída com sucesso
- Há múltiplas mudanças realizadas
- Sente-se tentação de "resumir"
- Acha que seria "útil"

**✅ ANTI-SUMMARY CHECKLIST (EXECUTAR ANTES DE QUALQUER TASK)**

**OBRIGATÓRIO para TODAS as tarefas:**

```
1. [ ] A tarefa usa palavras-chave proibidas (summary, report, consolidate)?
2. [ ] Há plano de criar arquivo .md "útil"?
3. [ ] Usuário pediu EXPLICITAMENTE "summary", "report", "log"?
4. [ ] É uma consolidação SOLICITADA no memory-bank?

SE SIM em 1-2 e NÃO em 3-4: ❌ ABORTAR IMEDIATAMENTE
SE SIM em 3-4: ✅ Proceder APENAS com memory-bank update
```

**Referência detalhada:** `/.github/instructions/no-unnecessary-files.instructions.md` (seção ANTI-SUMMARY ENFORCEMENT)

**Quando o usuário QUER summaries (SOMENTE nesses casos)**:
- ✅ "Crie um sumário visual disso"
- ✅ "Gere um resumo em ASCII"
- ✅ "Documente num arquivo novo"
- ✅ "Resuma o que foi feito"
- ✅ Apenas e SOMENTE então: criar arquivo de sumário

**✅ Resposta Correta SEMPRE**:
```
Pronto! Atualizei memory-bank-infrastructure/XX-ARQUIVO.md com as mudanças.
```

ou

```
Concluído! Refatorei 4 arquivos, build passou, sem erros.
```

**❌ Resposta ERRADA (NUNCA FAZER)**:
```
╔════════════════════════════════════════════╗
║  TUDO COMPLETO!!!                         ║
║  • Arquivo 1: feito ✅                    ║
║  • Arquivo 2: feito ✅                    ║
║  ... (20 linhas de resumo)                ║
╚════════════════════════════════════════════╝
```

**Por quê essa regra é crítica?**:
- 💰 Consome tokens desnecessariamente (budget limitado!)
- 🔄 Duplica informação já no Memory Bank
- ⏱️ Polui o chat, fica ilegível
- 📦 Cria arquivos desnecessários (viola: no-unnecessary-files.instructions.md)
- 😤 Usuário pediu explicitamente para PARAR com isso
- ⚡ Reduz velocidade de iteração

**Aplicação**: Esta regra se aplica SEMPRE, não há exceções.

---

## **⛔ CRITICAL: File Content Display Rules**

### **NEVER Display File Contents Automatically**

**⚠️ REGRA FUNDAMENTAL**: Não exibir conteúdo de arquivos no chat sem solicitação explícita.

**Proibido ABSOLUTAMENTE**:
- ❌ `cat arquivo.md` após atualização
- ❌ `cat > /tmp/summary.txt` seguido de `cat /tmp/summary.txt`
- ❌ Exibir 50+ linhas de Markdown no chat
- ❌ Copiar/colar conteúdo completo de arquivos
- ❌ "Aqui está o conteúdo atualizado:\n[200 linhas...]"
- ❌ Mostrar arquivo inteiro após cada modificação

**Comportamento correto após edição**:
```
✅ CORRETO: "Pronto! Atualizei [caminho/arquivo]"
✅ CORRETO: "Adicionei função X em [arquivo]"
✅ CORRETO: "Corrigi erro em [linha] de [arquivo]"

❌ ERRADO: "Atualizei! Veja o arquivo:\n--- [300 linhas] ---"
❌ ERRADO: "Aqui está o resultado:\n[conteúdo completo]"
```

**Quando exibir conteúdo é PERMITIDO**:
- ✅ Usuário pede: "mostre o arquivo X"
- ✅ Usuário pede: "qual o conteúdo de Y?"
- ✅ Usuário pede: "cat arquivo.md"
- ✅ Trechos pequenos (<20 linhas) para explicar mudança específica
- ✅ Diff relevante quando discutindo alteração

**Por quê?**:
- 💰 Consome tokens desnecessariamente
- 👁️ Polui a interface do chat
- 🔄 Informação já está no arquivo (redundante)
- ⚡ Torna conversa mais lenta
- 📊 Usuário pode abrir arquivo se quiser ver

**Exemplo Real (correto)**:
```
User: "Adicione logging em knowledge_base_repo.py"
AI: "Pronto! Adicionei logging em app/repositories/knowledge_base_repo.py"

❌ NÃO FAZER:
AI: "Aqui está o arquivo atualizado:
```python
[300 linhas de código...]
```
"
```

---

## **🤖 CRITICAL: Subagent Usage for Analysis & Validation**

### **🚨 PREVENT CONTEXT WINDOW BLOAT - Use Subagents**

**MANDATORY: Use subagents for analysis tasks that would generate large outputs**

⭐ **SEE ALSO**: [Context-Isolated Subagents Guide](context-isolated-subagents.instructions.md)

**⚠️ WHEN TO USE SUBAGENTS (REQUIRED)**:
- 📊 Analyzing multiple files (>3 files) for patterns or issues
- 🔍 Deep code review of complex features (>200 lines total)
- 📋 Validating changes across interconnected components
- 🧪 Evaluating architectural decisions with multiple trade-offs
- 📈 Generating comparison reports or impact analysis
- 🔬 Debugging complex issues requiring file-by-file inspection
- 🔄 Any analysis task that would produce >200 tokens of output
- 🤖 Using `/runSubagent` for isolated context window execution

**❌ NEVER Output Large Analysis Directly**:
- ❌ Don't paste 500+ lines of analysis in chat
- ❌ Don't output file-by-file review results inline
- ❌ Don't generate massive validation reports in main context
- ❌ Don't output detailed comparison tables (>50 lines)
- ❌ Don't dump entire file contents unless explicitly requested

**✅ CORRECT Pattern (with Context-Isolated Subagents)**:
```
User: "Analyze all bot files for code quality issues"
AI: "I'll use a subagent to analyze the 12 bot files with isolated context."
[Invokes /runSubagent with specific agent]
AI: "Subagent found 3 issues: [brief summary]. Key findings written to Memory Bank."
```

**How to Invoke Subagent**:
```
/runSubagent Use the Backend agent to analyze routers/links.py for:
- Code duplication
- N+1 query problems
- Missing error handling
Return: structured findings with line numbers
```

**Why This Is Critical**:
- 💰 Saves token budget dramatically (isolated context window)
- 🎯 Keeps main context focused on actionable work
- 🧠 Prevents information overload
- ⚡ Speeds up conversation flow
- 📊 Allows deeper analysis without bloat
- 🔄 Enables parallel analysis workflows
- 🏃 Subagent operates autonomously without pausing for confirmation

**How to Structure Subagent Requests**:
1. Define specific analysis scope (clear boundaries)
2. Request concise summary output only (1-page max)
3. Have subagent document findings in Memory Bank if needed
4. Subagent returns: Key issues + file locations only (no full dumps)
5. Main agent acts on findings without repeating analysis

**Reference**: See [context-isolated-subagents.instructions.md](context-isolated-subagents.instructions.md) for:
- Complete guide to Context-Isolated Subagents
- Padrões de uso (Research, Analysis, Planning, Review)
- Exemplos práticos prontos para usar
- Setup VS Code com custom agents

---

## **Code Quality & Architecture**

### **🚨 CRITICAL: Anti-Monolithic Code Rule**

**NEVER create monolithic scripts or files. This is a critical architectural failure.**

**Mandatory Rules:**
- **300-Line Limit:** Any file exceeding 300 lines MUST be refactored immediately
- **Modular Functions:** All scripts must use reusable, single-responsibility functions
- **Clear Separation:** Configuration, business logic, and utilities MUST be in separate modules
- **No God Objects:** Avoid classes or functions that do too many things
- **Extraction Required:** Long functions (>50 lines) must be broken into smaller, focused functions

**Refactoring Triggers:**
- File exceeds 300 lines → Extract modules
- Function exceeds 50 lines → Extract helper functions
- Class has >10 methods → Consider splitting responsibilities
- Duplicated code → Extract to shared utility

**⚠️ Violation is considered a critical architectural failure requiring immediate refactoring.**

### **🎯 Simplicity & Readability First**

**Code must be SIMPLE and READABLE - not clever or over-engineered.**

**Mandatory Simplicity Rules:**
- **Readable Names:** Variables, functions, and classes must have clear, descriptive names
- **Obvious Logic:** If you need complex comments to explain logic, simplify the code instead
- **Standard Patterns:** Use well-known patterns, avoid clever tricks
- **Inline Documentation:** Every non-trivial function needs inline comments explaining WHY (not just WHAT)
- **Progressive Complexity:** Start simple, add complexity only when proven necessary
- **No Premature Optimization:** Don't optimize until you have a performance problem
- **No Over-Abstraction:** Don't create elaborate class hierarchies "just in case"

**Examples:**
```python
# ❌ BAD: Over-engineered, clever but unreadable
def proc_data(d, f=lambda x: x**2): return [f(i) for i in d if i]

# ✅ GOOD: Simple, clear, and well-documented
def process_user_scores(scores):
    """
    Calculate squared values for non-zero scores.
    
    Args:
        scores: List of numeric scores (can include zeros)
        
    Returns:
        List of squared values for positive scores only
    """
    result = []
    for score in scores:
        if score > 0:  # Skip zero and negative scores
            squared = score ** 2
            result.append(squared)
    return result
```

**Code Review Questions to Ask Yourself:**
- Would a junior developer understand this code?
- Can I explain this logic in one sentence?
- Are there any "clever" tricks that sacrifice clarity?
- Is every non-obvious decision documented inline?

### **Code Organization Best Practices**

**Standard Module Structure:**
```text
service/
├── main.py / index.js              # Entry point
├── Dockerfile                       # Container build
├── requirements.txt / package.json  # Dependencies
├── src/
│   ├── config/                     # Configuration management
│   ├── services/                   # Business logic
│   ├── models/                     # Data models
│   ├── utils/                      # Utilities
│   ├── api/                        # API routes/endpoints
│   └── tests/                      # Tests
├── .env.example                    # Example environment variables
└── README.md                       # Documentation (references Memory Bank)
```

### **Dependency Management**

**Python Projects:**
- Always use `pip` with `requirements.txt` for dependency management
- Pin major versions but allow minor updates for security patches
- Test new dependencies thoroughly before adding to requirements
- Use virtual environments for isolation

**Node.js Projects:**
- Use `npm` or `yarn` with `package.json`
- Lock dependencies with `package-lock.json` or `yarn.lock`
- Audit dependencies regularly: `npm audit` / `yarn audit`

---

## **🔒 Code Review & Validation Protocol**

**CRITICAL: Never mark any modification as complete without careful review.**

### **1. Syntax & Type Checking**

**Python:**
```bash
# Syntax check (mandatory)
python -m compileall <modified_file.py>

# Type checking (mandatory)
mypy <modified_file.py>

# Linting (optional but recommended)
flake8 <modified_file.py>
```

**JavaScript/TypeScript:**
```bash
# TypeScript compiler (mandatory)
tsc --noEmit

# ESLint (optional but recommended)
eslint <modified_file.js>
```

### **2. Self-Review (MANDATORY)**

**After every code change:**

1. **Read Through All Modified Code:**
   - Read EVERY line you changed
   - Read EVERY line in functions you modified
   - Check variable names, function signatures, imports
   - Look for typos, logic errors, incomplete implementations

2. **Verify Logic Correctness:**
   - Trace execution paths mentally
   - Check error handling covers edge cases
   - Verify loop conditions and boundary cases
   - Ensure async/await patterns are correct

3. **Check Inline Documentation:**
   - Every function has docstring with purpose, parameters, returns
   - Complex logic sections have explanatory comments
   - Business rules are documented where implemented
   - Magic numbers/strings are explained or extracted to constants

4. **Impact Analysis:**
   - Identify all files that import your changed code
   - Check how changes affect calling code
   - Verify data structures match consumer expectations
   - Ensure backward compatibility if required

### **3. Subagent Validation (Complex Changes)**

**Use subagent for validation when:**
- Changes span >3 files
- Total changed lines >200
- Modifying critical business logic
- Touching shared utilities or core services
- Refactoring with many dependencies

**Subagent Instructions Should Include:**
```
"Review the following files for:
1. Logic correctness and edge cases
2. Inline documentation completeness
3. Potential breaking changes
4. Security vulnerabilities
5. Performance issues

Return only: Critical issues + line numbers. No full file dumps."
```

### **4. Integration Validation**

**Dependencies Check:**
- Verify all imports resolve correctly
- Check for circular dependencies
- Validate configuration files load properly
- Test with different environment variables (if applicable)

**Cross-Service Impact:**
- If modifying shared utilities, mentally trace usage
- If changing data structures, check consumers
- If updating API contracts, verify callers

### **5. Validation Workflow**

**Before Completion:**
1. ✅ Syntax validation passed (compileall/tsc minimum)
2. ✅ Type checking passed (mypy/TypeScript strict)
3. ✅ **Careful self-review completed (all code read)**
4. ✅ **Inline documentation added/updated**
5. ✅ Service/module imports without errors
6. ✅ For complex changes: Subagent validation completed
7. ✅ Memory Bank updated with changes

**Completion Criteria:**
- Code is simple, readable, and well-documented
- No obvious logic errors or edge case failures
- All modified code carefully reviewed
- Changes documented in appropriate Memory Bank
- CHANGELOG.md updated if user-facing change

**⚠️ CRITICAL: Skipping self-review is prohibited and may introduce bugs.**

---

## **Code Documentation Standards**

### **Inline Documentation (CRITICAL)**

**Every complex function, non-obvious logic, or business rule MUST have inline documentation.**

**Mandatory Documentation:**
- ✅ **Docstrings:** All public functions/classes with purpose, parameters, returns, and examples if helpful
- ✅ **Type Hints:** Python must use type hints, TypeScript must have proper types (no `any`)
- ✅ **WHY Comments:** Explain WHY decisions were made, not just WHAT code does
- ✅ **Edge Cases:** Document assumptions and edge case handling
- ✅ **Business Logic:** Explain business rules inline where implemented
- ✅ **Magic Values:** Document or extract magic numbers/strings

**Examples:**

```python
def calculate_affiliate_commission(price: float, tier: str) -> float:
    """
    Calculate commission based on price and affiliate tier.
    
    Business Rule: Premium tier gets 15% for orders >$100, otherwise 10%.
    Standard tier always gets 5%.
    
    Args:
        price: Product price in USD
        tier: Affiliate tier ('premium' or 'standard')
        
    Returns:
        Commission amount in USD
        
    Raises:
        ValueError: If tier is not 'premium' or 'standard'
    """
    if tier == 'premium':
        # High-value orders get bonus commission to incentivize promotion
        return price * 0.15 if price > 100 else price * 0.10
    elif tier == 'standard':
        return price * 0.05
    else:
        raise ValueError(f"Invalid tier: {tier}")
```

```typescript
/**
 * Fetches product data with automatic retry on failure.
 * 
 * Why retry: External API is occasionally unreliable, but usually
 * succeeds on second attempt. Better UX than showing error immediately.
 * 
 * @param productId - Unique product identifier
 * @returns Product data or null if all retries fail
 */
async function fetchProductWithRetry(
  productId: string
): Promise<Product | null> {
  const MAX_RETRIES = 3;
  
  for (let attempt = 1; attempt <= MAX_RETRIES; attempt++) {
    try {
      return await api.getProduct(productId);
    } catch (error) {
      // Log and retry on network errors, but not on 404
      if (attempt === MAX_RETRIES || error.status === 404) {
        return null;
      }
      await sleep(1000 * attempt); // Exponential backoff
    }
  }
  return null;
}
```

### **When to Document**

**ALWAYS document:**
- Functions >10 lines
- Business logic implementation
- Non-obvious algorithms
- Error handling decisions
- Performance optimizations
- Security-related code
- Edge case handling

**DON'T over-document:**
- Obvious getters/setters
- Self-explanatory one-liners
- Standard patterns (if following conventions)

---

## **Error Handling & Logging**

### **Error Handling Strategy**
- **Network Errors:** Implement retries with exponential backoff
- **API Errors:** Graceful degradation when external services fail
- **Database Errors:** Proper connection pooling and retry logic
- **Validation Errors:** Clear error messages for debugging

### **Inline Documentation for Error Paths**
- **MUST** document why specific error handling was chosen
- **MUST** explain non-obvious retry logic or fallback strategies
- **MUST** add comments for business-rule-driven error cases

### **Logging Best Practices**
- Use structured logging (JSON format preferred)
- Include correlation IDs for request tracing
- Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- Never log sensitive data (passwords, tokens, PII)
- Document in comments why specific events are logged

**Python Logging Example:**
```python
import logging
import json

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Structured logging
logger.info(json.dumps({
    "event": "user_action",
    "user_id": user_id,
    "action": "create_offer",
    "status": "success"
}))
```

---

## **Security & Best Practices**

### **Secrets Management**
- **NEVER** hardcode secrets in code
- Use Infisical for all secrets (see project-context.instructions.md)
- Load secrets at runtime from environment variables
- Rotate secrets regularly

### **API Security**
- Implement rate limiting on all endpoints
- Use JWT tokens for authentication
- Validate and sanitize all inputs
- Use HTTPS for all external communications

### **Data Privacy**
- Handle user data according to privacy requirements
- Implement proper data retention policies
- Anonymize logs and analytics data
- Follow LGPD/GDPR guidelines

---

## **Docker & Containerization**

### **Dockerfile Best Practices**
- Use official base images (Python, Node.js)
- Multi-stage builds for smaller images
- Don't run containers as root
- Use `.dockerignore` to exclude unnecessary files
- Pin version tags (avoid `latest`)

**Example Python Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

CMD ["python", "main.py"]
```

### **Docker Compose Guidelines**
- Use networks to isolate services
- Define health checks for all services
- Use volumes for persistent data
- Set resource limits (memory, CPU)

---

## **Git & Version Control**

### **Commit Messages**
Follow conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `refactor:` Code refactoring
- `test:` Adding tests
- `chore:` Maintenance tasks

**Example:**
```
feat(bots): add affiliate link generation via Gemini AI

- Implement new /gerar command in affiliate_helper_bot
- Integrate with centralized API endpoint
- Add fallback handling for API failures
```

### **Branching Strategy**
- `main` - production-ready code
- `develop` - integration branch
- `feature/*` - new features
- `fix/*` - bug fixes
- `hotfix/*` - urgent production fixes

---

## **Performance Optimization**

### **General Guidelines**
- Profile before optimizing (measure, don't guess)
- Optimize hot paths first (80/20 rule)
- Use caching strategically (Redis, in-memory)
- Implement pagination for large datasets

### **Python-Specific**
- Use async/await for I/O-bound operations
- Leverage connection pooling for databases
- Use generators for large data processing
- Profile with cProfile or py-spy

### **Node.js-Specific**
- Use async/await, avoid callback hell
- Implement clustering for CPU-intensive tasks
- Use streams for large file processing
- Monitor event loop lag

---

## **📚 CRITICAL: Documentation Rules**

### **🔴 RULE: ALL Documentation Lives in Service Memory Bank**

**⚠️ REGRA FUNDAMENTAL NOVA**: Toda documentação de um **serviço** está **DESCENTRALIZADA** em `repos/{service}/docs/memory-bank/`

**Estrutura Descentralizada (Novo Padrão)**:
```
repos/
├── ofertachina-api/
│   ├── src/                    [Código]
│   ├── tests/                  [Testes]
│   ├── requirements.txt        [Deps]
│   ├── Dockerfile              [Build]
│   ├── README.md               [⚠️ Referencia ./docs/memory-bank/]
│   └── docs/
│       └── memory-bank/        ← ⭐ DOCUMENTAÇÃO AQUI
│           ├── 00-07 (padrão)
│           └── tasks/
│
├── ofertachina-bots/
│   ├── bots/                   [Código]
│   ├── requirements.txt        [Deps]
│   ├── Dockerfile              [Build]
│   ├── README.md               [⚠️ Referencia ./docs/memory-bank/]
│   └── docs/
│       └── memory-bank/        ← ⭐ DOCUMENTAÇÃO AQUI
│           ├── 00-07 (padrão)
│           └── tasks/
│
└── ... (mesmo padrão para todos os serviços)
```

**O que fica em `/docs` (raiz do projeto - apenas cross-cutting)**:
```
/docs/
├── memory-bank/                 (context do projeto)
├── memory-bank-infrastructure/  (DevOps, ports, secrets)
├── memory-bank-waha/            (shared service)
└── DOCKER-COMPOSE-REFERENCE.md
```

**PROIBIDO ABSOLUTAMENTE**:
- ❌ Criar `.md` files fora de `repos/{service}/docs/memory-bank/` (para documentação de serviço)
- ❌ Criar pastas `memory-bank/` duplicadas
- ❌ Criar `.copilot/` com instruções nos repos
- ❌ Documentação "por precaução"
- ❌ Duplicar entre repos e `/docs`

**PERMITIDO APENAS**:
- ✅ `repos/{service}/docs/memory-bank/00-07.md` - Documentação completa
- ✅ `repos/{service}/docs/memory-bank/tasks/` - Tarefas e progresso
- ✅ `repos/{service}/README.md` - Referência MÍNIMA ao ./docs/memory-bank/
- ✅ Code comments - Explicar código complexo

**README.md Template** (mínimo, apenas REFERÊNCIA):
```markdown
# [Service Name]

Brief description.

## 📚 Documentação

→ [./docs/memory-bank/](./docs/memory-bank/)

Comece por: [00-overview.md](./docs/memory-bank/00-overview.md)

Para mais:
- **Arquitetura**: [01-architecture.md](./docs/memory-bank/01-architecture.md)
- **Deployment**: [06-deployment.md](./docs/memory-bank/06-deployment.md)

## Quick Start

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
```

### **Benefits of Decentralized Structure**

1. **History with Code**: Git history preserva documentação com código
2. **Clear Ownership**: Cada equipe controla sua documentação
3. **Reduced Confusion**: Documentação perto de onde é usada
4. **Easy Onboarding**: Clone repo = tenha tudo (code + docs)
5. **Scalable**: Novo serviço? Novo repo com seu memory-bank
6. **Git-Friendly**: Mudanças em documentação trackadas com código

### **Code Documentation** (In Code, Not Files)

- Write docstrings for all public functions/classes
- Include type hints (Python) or TypeScript types
- Document complex algorithms and business logic
- Keep comments up-to-date with code changes
- **⚠️ Complex concepts** → Document in Memory Bank (./docs/memory-bank/), reference from code

### **Memory Bank Documentation** (in each repo)

- **MUST** update after architectural changes
- **MUST** keep 04-active-context.md current (weekly)
- **MUST** add entry to 05-progress-log.md per significant change
- **MUST** use 00-07 + tasks/ structure (no exceptions)
- Reference: `/.github/instructions/memory-bank-guidelines.md`

### **For Cross-Cutting Documentation**

Only in `/docs` (root project):
- `memory-bank/` - Project-wide context
- `memory-bank-infrastructure/` - Shared DevOps, ports, secrets
- `memory-bank-waha/` - Shared service documentation

---

## **Deployment & Operations**

### **Environment Setup**
- Use virtual environments for isolation
- Document all system dependencies
- Provide setup scripts for automation
- Test deployment process regularly

### **Monitoring & Alerting**
- Implement health checks for all services
- Monitor key metrics (response time, error rate, throughput)
- Set up alerts for critical failures
- Use centralized logging (if available)

### **Backup & Recovery**
- Regular automated backups of databases
- Test restore procedures periodically
- Document disaster recovery plan
- Keep backups in separate location

---

**Always act within the described scope and prompt constraints. Focus on robust, maintainable solutions that follow the project's architectural patterns.**
