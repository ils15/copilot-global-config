---
applyTo: '**'
description: 'Documentation Standards - Where, What, and How to document'
---

# Documentation Standards for Ofertasdachina

## 🚨 THE GOLDEN RULE

**NEVER create .md files automatically.**

```
┌──────────────────────────────────────────┐
│ ❌ NO .md files outside Memory Bank      │
│ ❌ NO STATUS.md, SUMMARY.md, etc         │
│ ❌ NO session documentation              │
│ ✅ Memory Bank ONLY for persistence      │
└──────────────────────────────────────────┘
```

---

## 📁 Official Documentation Structure

### **REQUIRED** in `/docs/memory-bank/`:

```
docs/memory-bank/
├── 00-overview.md           # Project brief
├── 01-architecture.md       # System design
├── 02-components.md         # Component breakdown
├── 03-tech-context.md       # Technologies, setup
├── 04-active-context.md     # Current focus, decisions
├── 05-progress-log.md       # What works, what's left
├── _tasks/
│   ├── _index.md            # Task master list
│   ├── TASK0001-name.md     # Completed tasks/bugs
│   └── ...
└── _notes/
    ├── _index.md            # Note master list
    ├── NOTE0001-subject.md  # Decisions, patterns, discoveries
    └── ...
```

### **ALLOWED** outside Memory Bank:

- `.github/` - Instructions, agents, skills, prompts (FIXED CONFIG)
- `README.md` - Project overview (ONLY if explicitly requested)
- `CONTRIBUTING.md` - Contribution guidelines (ONLY if explicitly requested)

### **PERMANENTLY FORBIDDEN**:

- `/agent-output/analysis/` - Temporary analysis docs ❌
- Root `.md` files - ANALYSIS_*, SUMMARY_*, STATUS_* ❌
- `/docs/` - Random documentation outside memory-bank ❌
- Session-based docs - QA_*, IMPLEMENTATION_*, CHANGELOG_*, RESUMO_* ❌

---

## 🎯 What Type of Documentation Goes Where?

| Type | Location | Owner | Format |
|------|----------|-------|--------|
| **Completed Task** | `_tasks/TASK000X-*.md` | Implementer (handoff to Planner) | Structured task file |
| **Bug Fix Analysis** | `_tasks/TASK000X-*.md` or `_notes/NOTE000X-*.md` | Analyst/Implementer → Planner | Description + Solution |
| **Architectural Decision** | `_notes/NOTE000X-*.md` | Architect → Planner | Decision + Rationale |
| **Technical Pattern** | `_notes/NOTE000X-*.md` | Discoverer → Planner | Pattern + Usage |
| **Security Finding** | `_notes/NOTE000X-*.md` | Security → Planner | Finding + Remediation |
| **Temporary Analysis** | ❌ NOWHERE (can be verbal) | - | - |
| **Session Status** | ❌ NOWHERE (use 05-progress-log.md) | Planner | Inline in memory-bank |

---

## 👥 Agent Responsibilities

### **@Planner** (EXCLUSIVE OWNER)
✅ Creates/updates ALL Memory Bank files  
✅ Manages `_tasks/_index.md` and `_notes/_index.md`  
✅ Handoff: None (Planner is final destination)  

### **All Other Agents** (Backend, Frontend, Database, Analyst, etc)
❌ NEVER create .md files  
✅ Handoff to @Planner with structured data  
✅ Example: "Update Memory Bank with bug fix analysis"  

### **Subagents**
❌ NEVER create any documentation  
✅ Return only: code, test results, or analysis  
✅ Handoff to parent agent for documentation  

---

## 📝 How to Create Documentation

### **Option 1: When User Explicitly Requests**

User says: *"Create a note about the JWT implementation"*

**Then you must:**
1. Create in `/docs/memory-bank/_notes/`
2. Use format: `NOTE000X-jwt-implementation.md`
3. Update `_notes/_index.md`
4. Store final reference in Memory Bank

### **Option 2: During Implementation (Handoff to Planner)**

**Implementer/Analyst finishes work:**
```
Use @Planner to: Document the following in Memory Bank:
- Task: Product extraction bug fix
- Type: TASK update or NOTE creation
- Content: [brief summary of what to document]
```

**Planner:**
```
✅ TASK0044 updated with findings
✅ NOTE0010 created with pattern discovery
✅ _tasks/_index.md and _notes/_index.md updated
```

---

## 🚫 Anti-Patterns (What NOT to Do)

### ❌ Anti-Pattern 1: Session Documentation
```
DO NOT create:
- ANALYSIS_COMPLETE_STATUS.md
- IMPLEMENTATION_SUMMARY.txt
- QA_REVIEW_RESULTS.md
- SESSION_SUMMARY.md

USE:
- Update 05-progress-log.md instead
- Create TASK/NOTE via @Planner
```

### ❌ Anti-Pattern 2: Duplicate Documentation
```
DO NOT create:
- docs/QUICK_START.md (if Memory Bank exists)
- docs/ARCHITECTURE.md (if 01-architecture.md exists)
- docs/IMPLEMENTATION_CHECKLIST.md (if _tasks/ exists)

USE:
- Reference Memory Bank files
- Update existing Memory Bank files
```

### ❌ Anti-Pattern 3: Unstructured Notes
```
DO NOT create:
- docs/NOTES.md (random thoughts)
- root/TODO.txt (scattered tasks)
- config/DECISIONS.log (untracked decisions)

USE:
- _notes/NOTE000X-subject.md (structured)
- _tasks/TASK000X-subject.md (structured)
- manage_todo_list tool (for session tasks)
```

---

## ✅ Checklist Before Creating Any .md

1. [ ] User explicitly asked for this documentation? (or is it code output)
2. [ ] Does it belong in Memory Bank?
3. [ ] Is it a TASK or NOTE that needs tracking?
4. [ ] Should I handoff to @Planner instead?
5. [ ] Am I replacing or duplicating an existing file?
6. [ ] Will this still be useful in 1 month?

If ANY answer is "no", DON'T CREATE IT.

---

## 📚 Reference Documents

- [memory-bank.instructions.md](memory-bank.instructions.md) - Full Memory Bank spec
- [core-rules.instructions.md](core-rules.instructions.md) - Documentation Rules (Rule 2.x)
- [copilot-instructions.md](../copilot-instructions.md) - Rule 1: Never auto-create .md
- [subagents.instructions.md](subagents.instructions.md) - Subagent rules (no .md)

---

## 🎓 Examples

### ✅ GOOD: Document a Bug Fix

**Scenario**: Backend agent fixes product extraction bug

**Action**:
```
Handoff to @Planner:
"Document the product extraction bug fix. 
Root cause: JSON mapping missing null check.
Solution: Added validation in ProductExtractor.validate_json()
Impact: Fixes 15% of failed extractions"
```

**Result**:
```
/docs/memory-bank/_tasks/TASK0044-product-extraction-bugs.md
(Created with timestamp, status, solution details)
```

### ✅ GOOD: Document an Architecture Decision

**Scenario**: Architect decides to use async/await everywhere

**Action**:
```
Handoff to @Planner:
"Create a note about async/await decision.
Decision: All I/O operations must use async/await
Rationale: Performance, consistency, handles network timeouts
Status: Approved and implemented"
```

**Result**:
```
/docs/memory-bank/_notes/NOTE0001-async-await-pattern.md
(Created with decision, rationale, implementation status)
```

### ❌ BAD: Random Documentation

**Scenario**: Analysis finds an issue

**Wrong**:
```
Create:
- docs/ANALYSIS_FINDINGS.md
- root/FINDINGS_20250112.txt
- agent-output/analysis/findings.md
```

**Correct**:
```
Handoff to @Planner:
"Update Memory Bank with analysis findings regarding [topic]"
```

---

**Last Updated**: 2025-01-12  
**Version**: 1.0  
**Owner**: Copilot Global Standards
