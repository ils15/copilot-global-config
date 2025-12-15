---
name: memory-bank-updater
description: Update Memory Bank documentation systematically after completing features, fixing bugs, or making architectural changes. Ensures activeContext, progress, and task files stay current.
---

# Memory Bank Updater

Keep Memory Bank documentation synchronized with code changes.

## What This Skill Does

Systematically updates Memory Bank files after:
- Completing features or tasks
- Fixing bugs or issues
- Making architectural changes
- Refactoring code
- Adding new components
- Deployment or configuration changes

## When to Use This Skill

- After completing a significant task
- Before closing a session
- When architectural decisions are made
- After fixing critical bugs
- When user requests "update memory bank"
- At end of sprint/milestone

## Memory Bank Structure

```
.github/memory-bank/
├── projectbrief.md       # Foundation: scope, goals, phases
├── productContext.md     # Why: problems, solutions, UX
├── activeContext.md      # Current: focus, changes, next steps
├── systemPatterns.md     # Architecture: design, patterns
├── techContext.md        # Stack: technologies, setup
├── progress.md           # Status: what works, what's left
├── tasks/
│   ├── _index.md         # Master task list
│   └── TASKXXX-name.md   # Individual task details
└── audits/
    ├── _index.md         # Audit history
    └── AUDIT-DATE.md     # Audit reports
```

## Update Decision Matrix

| What Changed | Update These Files |
|--------------|-------------------|
| New feature completed | `activeContext.md`, `progress.md`, `tasks/TASKXXX.md` |
| Bug fixed | `progress.md`, `tasks/TASKXXX.md` if exists |
| Architecture decision | `systemPatterns.md`, `activeContext.md` |
| Technology added | `techContext.md`, `systemPatterns.md` |
| Current focus changed | `activeContext.md` |
| Task started/completed | `tasks/TASKXXX.md`, `tasks/_index.md` |
| Quarterly audit | `audits/AUDIT-DATE.md`, `audits/_index.md` |

## Standard Update Workflow

### 1. Review Context
```markdown
Questions to ask:
- What was completed?
- What changed architecturally?
- What's the current state?
- What's next?
- Are there blockers?
```

### 2. Update activeContext.md

**Format**:
```markdown
# Active Context

**Last Updated**: YYYY-MM-DD
**Current Sprint/Phase**: Phase X - Description

## Current Focus

[What you're working on NOW - 1-2 paragraphs]

## Recent Changes

### YYYY-MM-DD
- Completed feature X
- Fixed bug Y
- Decided to use pattern Z

### YYYY-MM-DD
- Previous changes...

## Next Steps

1. [ ] Next immediate task
2. [ ] Following task
3. [ ] Future task

## Active Decisions

**Decision**: Use PostgreSQL instead of MySQL
**Reason**: Better JSON support, active development
**Date**: YYYY-MM-DD

## Blockers/Risks

- **Blocker**: Waiting for API key
- **Risk**: Database migration complexity
```

### 3. Update progress.md

**Format**:
```markdown
# Progress Log

## What Works Now

### Core Features
- ✅ User authentication (JWT)
- ✅ Product listing API
- 🚧 Product search (in progress)
- ⏳ Product recommendations (planned)

### Infrastructure
- ✅ Docker Compose setup
- ✅ CI/CD pipeline
- ✅ SSL certificates

## Recent Completions

### YYYY-MM-DD - Feature Name
**Status**: ✅ Complete
**Summary**: Brief description
**Changes**:
- File X: Added function Y
- File Z: Refactored logic

### YYYY-MM-DD - Bug Fix
**Status**: ✅ Fixed
**Issue**: Description of bug
**Root Cause**: Why it happened
**Solution**: How it was fixed

## What's Left

### High Priority
1. [ ] Feature A
2. [ ] Bug fix B

### Medium Priority
1. [ ] Optimization C
2. [ ] Refactoring D

### Low Priority
1. [ ] Nice-to-have E

## Known Issues

- **Issue**: Description
- **Impact**: Who/what is affected
- **Workaround**: Temporary solution
- **Planned Fix**: ETA for resolution
```

### 4. Update Task Files

**Create new task** (`tasks/TASK123-feature.md`):
```markdown
# [TASK123] - Feature Name

**Status**: In Progress
**Added**: YYYY-MM-DD
**Updated**: YYYY-MM-DD

## Original Request
[User's original request]

## Thought Process
[Discussion and reasoning]

## Implementation Plan
- [ ] Step 1
- [ ] Step 2
- [ ] Step 3

## Progress Tracking

**Overall Status**: In Progress - 60%

### Subtasks
| ID | Description | Status | Updated | Notes |
|----|-------------|--------|---------|-------|
| 1.1 | Setup | Complete | YYYY-MM-DD | Done |
| 1.2 | Implementation | In Progress | YYYY-MM-DD | 60% done |
| 1.3 | Testing | Not Started | - | - |

## Progress Log

### YYYY-MM-DD
- Completed subtask 1.1
- Started subtask 1.2
- Encountered issue with X, solved by Y
```

**Update task index** (`tasks/_index.md`):
```markdown
# Tasks Index

## In Progress
- [TASK123] Feature Name - 60% complete

## Pending
- [TASK124] Other Feature - Not started

## Completed
- [TASK122] Previous Feature - Done YYYY-MM-DD

## Abandoned
- [TASK121] Old Idea - No longer needed
```

### 5. Update Architecture (if applicable)

**systemPatterns.md**:
```markdown
## Recent Architectural Changes

### YYYY-MM-DD - New Pattern
**Change**: Adopted repository pattern
**Reason**: Better separation of concerns
**Impact**: All database access goes through repos
**Files Affected**: `services/`, `repositories/`
```

## Update Checklist

```markdown
Pre-Update:
- [ ] Read all current Memory Bank files
- [ ] Understand what changed since last update
- [ ] Gather all relevant information

Required Updates:
- [ ] activeContext.md - Current focus and recent changes
- [ ] progress.md - What works, what's completed, what's left
- [ ] tasks/TASKXXX.md - Task progress if applicable
- [ ] tasks/_index.md - Task status if applicable

Optional Updates:
- [ ] systemPatterns.md - If architecture changed
- [ ] techContext.md - If technology changed
- [ ] productContext.md - If UX/goals changed
- [ ] projectbrief.md - If scope/phases changed

Post-Update:
- [ ] Verify all dates are current
- [ ] Verify all statuses are accurate
- [ ] Verify no duplicate information
- [ ] Verify links work
```

## Common Update Patterns

### Pattern 1: Feature Completion
```
1. Update activeContext.md:
   - Move feature from "Current Focus" to "Recent Changes"
   - Update "Next Steps" with new immediate task

2. Update progress.md:
   - Add to "Recent Completions"
   - Update "What Works Now"
   - Remove from "What's Left"

3. Update tasks/TASKXXX.md:
   - Change status to "Completed"
   - Add final progress log entry
   - Update subtasks to 100%

4. Update tasks/_index.md:
   - Move from "In Progress" to "Completed"
```

### Pattern 2: Bug Fix
```
1. Update progress.md:
   - Add to "Recent Completions" (Bug Fix section)
   - Remove from "Known Issues" if listed

2. Update activeContext.md:
   - Add to "Recent Changes"

3. Create/update task file if significant bug
```

### Pattern 3: Architectural Change
```
1. Update systemPatterns.md:
   - Document new pattern/decision
   - Explain reasoning
   - Note files affected

2. Update activeContext.md:
   - Add to "Active Decisions"
   - Update "Current Focus" if needed

3. Update techContext.md if tech stack changed
```

### Pattern 4: Sprint/Phase End
```
1. Review ALL Memory Bank files
2. Update progress.md with complete status
3. Update activeContext.md with next sprint focus
4. Archive completed tasks
5. Create new tasks for next sprint
```

## Example: Complete Update Session

**Scenario**: Completed JWT authentication feature

**1. activeContext.md**:
```diff
## Current Focus

- Implementing user authentication with JWT
+ Building product recommendation engine

## Recent Changes

+ ### 2025-12-15
+ - ✅ Completed JWT authentication implementation
+ - Added login, logout, refresh token endpoints
+ - Integrated with all protected routes
+
### 2025-12-10
...
```

**2. progress.md**:
```diff
## What Works Now

### Core Features
+ - ✅ User authentication (JWT)
- - 🚧 User authentication (in progress)

## Recent Completions

+ ### 2025-12-15 - JWT Authentication
+ **Status**: ✅ Complete
+ **Summary**: Full JWT auth implementation
+ **Changes**:
+ - `routers/auth.py`: Login, logout, refresh endpoints
+ - `middleware/auth.py`: JWT verification middleware
+ - `services/auth_service.py`: Token generation/validation
```

**3. tasks/TASK089-jwt-auth.md**:
```diff
- **Status**: In Progress
+ **Status**: Completed
- **Updated**: 2025-12-14
+ **Updated**: 2025-12-15

**Overall Status**: Complete - 100%

### Subtasks
| ID | Description | Status | Updated | Notes |
|----|-------------|--------|---------|-------|
- | 3.1 | Testing | In Progress | 2025-12-14 | 80% |
+ | 3.1 | Testing | Complete | 2025-12-15 | All tests pass |

## Progress Log

+ ### 2025-12-15
+ - ✅ Completed all tests (unit + integration)
+ - ✅ Deployed to staging, all checks passed
+ - ✅ Task fully complete
```

**4. tasks/_index.md**:
```diff
## In Progress
- - [TASK089] JWT Authentication - 80% complete
+ - [TASK090] Product Recommendations - Just started

## Completed
+ - [TASK089] JWT Authentication - Completed 2025-12-15
```

## Guidelines

- Update immediately after significant changes
- Be specific about what changed and why
- Keep dates current (YYYY-MM-DD format)
- Link related files/tasks when relevant
- Don't duplicate information across files
- Use clear status indicators (✅ ⏳ 🚧 ❌)
- Remove stale information

## Anti-Patterns to Avoid

❌ Waiting too long to update (memory fades)
❌ Vague descriptions ("updated stuff")
❌ Missing dates on changes
❌ Duplicating same info in multiple files
❌ Not updating task statuses
❌ Forgetting to update _index.md
❌ Leaving stale "Current Focus" items

## Reference

- Memory Bank Guidelines: `/.github/instructions/memory-bank.instructions.md`
- Project Context: `/.github/instructions/project-context.instructions.md`
