---
applyTo: '**'
description: 'Core Rules - Fundamental planning, documentation, and task management rules'
---

# Core Rules - Ofertasdachina Platform

## 0. CODE QUALITY EXECUTION (NEW - v3.0)

**4 REGRAS CRÍTICAS OBRIGATÓRIAS:**

- Rule 0.1: @Quality subagent ALWAYS after code changes (every file, every feature)
- Rule 0.2: Use specialized subagent to evaluate generated code (@Backend for Python, @Frontend for TS/React, etc)
- Rule 0.3: Research best practices BEFORE coding (grep_search → @Architect → @Analyst → document)
- Rule 0.4: Remove backward compatibility & legacy code with EVERY modification (checklist required)

**See**: `/home/admin/website/copilot-instructions.md` for detailed workflow

---

## 1. PLANNING RULES (from copilot-execution.instructions.md)

- Rule 1.1: Always create INTERNAL IMPLEMENTATION PLAN before coding
- Rule 1.2: Plan structure: GOAL (1 sentence), SCOPE (files/functions), JUSTIFICATION (1 line), RISKS (if any), STEPS (numbered list)
- Rule 1.3: Favor simple, readable solutions over clever code
- Rule 1.4: Code must be robust AND well-documented inline
- Rule 1.5: Use asyncio/async/await for all I/O operations
- Rule 1.6: Plan for network failures, API timeouts, external service issues
- Rule 1.7: After implementation, review all modified code for correctness and documentation
- Rule 1.8: Execute immediately after plan (no approval needed)

## 2. DOCUMENTATION RULES

- Rule 2.1: NEVER create .md files automatically (README.md, GUIDE.md, TUTORIAL.md, CHANGELOG.md, NOTES.md, SUMMARY.md)
- Rule 2.2: NEVER create SESSION-SUMMARY.md, CONSOLIDADO.md, FINAL.md, STATUS.md after conversations
- Rule 2.3: NEVER create multiple versions of same document or "resumos visuais"
- Rule 2.4: NEVER display file content automatically (no cat, no giant outputs >50 lines)
- Rule 2.5: All documentation goes in Memory Bank (/docs/memory-bank/)
- Rule 2.6: Only allowed .md outside Memory Bank: README.md (if requested), CONTRIBUTING.md, .github/templates

## 3. TASK MANAGEMENT RULES (from [memory-bank.instructions.md](memory-bank.instructions.md))

- Rule 3.1: Update Memory Bank after complex implementations
- Rule 3.2: Use tasks/_index.md for tracking all tasks with statuses
- Rule 3.3: Create individual task files: TASKID-taskname.md for each task
- Rule 3.4: Update both subtask status table and progress log when progressing
- Rule 3.5: Update overall task status, completion percentage, and _index.md

## ⚠️ CONFLICT RESOLUTION

If rules conflict, apply this priority:
- Level 1 (Highest): Documentation rules (never override "no auto .md" rule)
- Level 2: Planning rules (MUST create plans before implementation)
- Level 3: Task management (NICE-TO-HAVE, don't override #1-2)