---
applyTo: '**'
---

# Memory Bank - STRICT GUIDELINES

⚠️ **CRITICAL**: ALL documentation (except code) goes ONLY in `/docs/memory-bank/`. NO .md files outside this folder.

## 📁 Exact Directory Structure

```
docs/memory-bank/
├── 00-overview.md           # Project brief (REQUIRED)
├── 01-architecture.md       # System design (REQUIRED)
├── 02-components.md         # Component breakdown (REQUIRED)
├── 03-tech-context.md       # Technologies, setup (REQUIRED)
├── 04-active-context.md     # Current focus, decisions (REQUIRED)
├── 05-progress-log.md       # What works, what's left (REQUIRED)
├── _tasks/                  # ALL task files
│   ├── _index.md            # Task master list (REQUIRED)
│   ├── TASK0001-name.md     # Individual task
│   ├── TASK0002-name.md
│   └── ...
└── _notes/                  # ALL note files
    ├── _index.md            # Note master list (REQUIRED)
    ├── NOTE0001-subject.md  # Individual note
    ├── NOTE0002-subject.md
    └── ...
```

## 🎯 When to Create Files

| Type | Format | Location | When |
|------|--------|----------|------|
| **TASK** | `TASK0001-feature-name.md` | `_tasks/` | New feature/bug/refactor |
| **NOTE** | `NOTE0001-subject.md` | `_notes/` | Decision/finding/pattern |
| **PROGRESS** | Update `05-progress-log.md` | `/` | After sprint/milestone |
| **DECISION** | Update `04-active-context.md` | `/` | Architecture/design choice |

## 📝 Task File Template

```markdown
# TASK0001 - Implement JWT Auth

**Status**: Not Started | In Progress | Completed | Blocked  
**Priority**: P0 | P1 | P2  
**Added**: 2025-12-23  
**Updated**: 2025-12-23  

## Original Request
[What user asked for]

## Implementation Plan
- Step 1
- Step 2
- Step 3

## Progress

| Subtask | Status | Notes |
|---------|--------|-------|
| 1.1 Design schema | Complete | Schema in models/ |
| 1.2 Implement service | In Progress | 60% complete |
| 1.3 Add tests | Not Started | - |

## Updates
**2025-12-23**: Started implementation, designed schema
```

## 📌 Note File Template

```markdown
# NOTE0001 - JWT Token Expiration Strategy

**Created**: 2025-12-23  
**Category**: Architecture | Security | Pattern | Decision  
**Related Tasks**: TASK0001  

## Context
[Why this matters, background]

## Decision
[What was decided]

## Rationale
[Why this choice]
```

## 🔄 Index Files (MANDATORY)

### `_tasks/_index.md`
```markdown
# Tasks Index

## Active
- [TASK0001] JWT Auth - 60% complete

## Pending
- [TASK0002] API Documentation - Waiting for design

## Completed
- [TASK0000] Project Setup - Finished 2025-12-20
```

### `_notes/_index.md`
```markdown
# Notes Index

## Architecture
- [NOTE0001] JWT Token Strategy
- [NOTE0002] API Versioning

## Decisions
- [NOTE0003] Use async/await everywhere
```

## ✅ RULES (Non-negotiable)

1. **NO random .md files** → Everything in `_tasks/` or `_notes/`
2. **Numbered sequentially** → TASK0001, TASK0002, NOTE0001, NOTE0002
3. **_index.md always updated** → When adding task/note, update index
4. **No summary files** → No SUMMARY.md, CHANGELOG.md, SESSION.md
5. **No verbose docs** → Concise, scannable, action-oriented
6. **Read ALL files on session start** → Mandatory for context

## 🚀 Quick Commands

**Create new task:**
```
Create TASK0001-feature-name.md in _tasks/
Update _tasks/_index.md
```

**Create new note:**
```
Create NOTE0001-subject.md in _notes/
Update _notes/_index.md
```

**Update progress:**
```
Edit 05-progress-log.md ONLY
Update task status in _tasks/TASKXXXX.md
```

