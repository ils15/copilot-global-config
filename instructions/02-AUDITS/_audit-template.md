# Audit Template - Shared Structure

## 4 Phases

### Phase 1: Assessment (5 min)
Collect basic metrics using terminal commands:
- Total lines: `find {path} -name "*.py" | xargs wc -l | tail -1`
- Functions/methods: `grep -r "^def " {path} | wc -l`
- Classes: `grep -r "^class " {path} | wc -l`
- Largest file: `find {path} -name "*.py" -exec wc -l {} + | sort -n | tail -5`
- Import duplication: `grep -r "^from " {path} | sort | uniq -d`

### Phase 2: Execution (10 min)
1. **Separation of Concerns**: Check for /handlers, /services, /models
2. **God Objects**: Identify largest classes/files (>10 methods, >300 lines)
3. **Code Duplication**: Grep common patterns, compare across components

### Phase 3: Organization (15 min)
Use 30-question checklist in 6 categories:

#### 1. STRUCTURE (5 questions)
- Q1.1: Largest file and line count?
- Q1.2: Which class/module violates SRP?
- Q1.3: Clear separation between handlers/, services/, models/?
- Q1.4: Methods in largest class?
- Q1.5: Code duplication percentage from other components?

#### 2. QUALITY (5 questions)
- Q2.1: Test coverage percentage?
- Q2.2: Type hints on public functions?
- Q2.3: Docstrings on public classes/methods?
- Q2.4: Consistent error handling (try/except/finally)?
- Q2.5: Structured logging with appropriate levels?

#### 3. SECURITY (5 questions)
- Q3.1: Admin IDs hardcoded or in config/Vault?
- Q3.2: Tokens/secrets loaded via Vault AppRole?
- Q3.3: Input validation on all commands?
- Q3.4: DB connections closed properly (context managers)?
- Q3.5: Rate limiting implemented?

#### 4. PERFORMANCE (5 questions)
- Q4.1: Caching implemented? Where?
- Q4.2: DB queries optimized (indexes, pagination)?
- Q4.3: External connections use timeout/retry?
- Q4.4: Known memory leaks?
- Q4.5: Connection pool configured correctly?

#### 5. MAINTAINABILITY (5 questions)
- Q5.1: Memory Bank updated and complete?
- Q5.2: README or documentation exists?
- Q5.3: Configuration via env vars or hardcoded?
- Q5.4: Schema versioning/migrations exist?
- Q5.5: Commands documented in /help?

#### 6. COMPLEXITY (5 questions)
- Q6.1: Max cyclomatic complexity per function? (Target: <10)
- Q6.2: Deep nesting of if/loops (>3 levels)? Where?
- Q6.3: Functions with unnecessary parameters or over-engineered logic?
- Q6.4: Code that could be simplified with standard libraries?
- Q6.5: Excessive abstractions (unnecessary interfaces/classes)?

### Phase 4: Review (10 min)
Prioritize issues:
- 🔴 CRITICAL: Fix today (runtime errors, security breaches, performance degradation)
- 🟠 HIGH: Fix this sprint (major refactoring, code complexity)
- 🟡 MEDIUM: Fix next sprint (improvements, simplification)
- 🟢 LOW: Backlog (nice-to-have)

## Metrics Table

| Metric | Value | Status | Target |
|--------|-------|--------|--------|
| Total Lines | X | 🟢/🟡/🔴 | <5000 |
| Largest Class | Y methods | 🟢/🟡/🔴 | <10 |
| Largest File | Z lines | 🟢/🟡/🔴 | <300 |
| Test Coverage | W% | 🟢/🟡/🔴 | >70% |
| Code Duplication | V% | 🟢/🟡/🔴 | <20% |
| Vault Integration | OK/FAIL | ✅/❌ | All secrets |
| Security Score | S/10 | 🟢/🟡/🔴 | >8 |
| Architecture Score | R/10 | 🟢/🟡/🔴 | >7 |

## Critical/High/Medium Findings Format

### 🔴 CRITICAL ISSUES
1. **[Issue Title]**
   - Location: File:Line
   - Impact: Description
   - Fix: Recommended fix (1-2 lines)
   - Effort: X hours

### 🟠 HIGH PRIORITY ISSUES
1. **[Issue Title]**
   - Location: File:Line
   - Impact: Description
   - Fix: Recommendation
   - Effort: X hours

### 🟡 MEDIUM PRIORITY ISSUES
1. **[Issue Title]**
   - Location: File:Line
   - Impact: Description
   - Fix: Recommendation
   - Effort: X hours

## Safety Guidelines

**Do's:**
- Use subagents for audits >500 lines or >5 files
- Follow exact 30-question checklist
- Prioritize CRITICAL issues immediately
- Update Memory Bank with audit results
- Test fixes after implementation

**Don'ts:**
- Skip phases - complete all 4
- Ignore code duplication across components
- Leave security vulnerabilities unfixed
- Create audit files outside memory-bank/
- Audit without updating metrics table