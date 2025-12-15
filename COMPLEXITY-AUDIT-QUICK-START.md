# Bot Complexity Audit System - Quick Start Guide

**Date Created**: 2025-12-14  
**Status**: ✅ Ready to Use  
**Owner**: @backend (Complexity Expert)

---

## What Changed

### 1. Bot Audit System Extended (25 → 30 Questions)
- **Added**: Category 6 - COMPLEXIDADE with 5 new questions (Q6.1-Q6.5)
- **Focus**: Cyclomatic complexity, nesting depth, parameters, over-engineering
- **File**: `/.github/instructions/bot-audit.instructions.md`

### 2. New Code Simplification Guide
- **Created**: `/.github/instructions/code-simplification.instructions.md`
- **Covers**: Metrics, anti-patterns, simplification patterns, workflows
- **Purpose**: Practical guide for reducing code complexity

### 3. Agent Updates
- **Enhanced**: `@backend` with complexity expertise
- **New capability**: Code simplification & refactoring
- **File**: `/home/admin/agents.md` (v1.9)

---

## Quick Commands

### **Audit Phase**
```bash
@planner Run audit for alertas_bot including Q6 complexity metrics
```

### **Analysis Phase**
```bash
@debug Analyze alertas_bot for complexity issues from Q6.1-Q6.5
```

### **Simplification Phase**
```bash
@backend Simplify alertas_bot following code-simplification patterns:
- Reduce CC from X to <10
- Break nesting from 5 to <3 levels
- Extract helper functions
- Replace over-engineering
```

### **Validation Phase**
```bash
@reviewer Validate simplified alertas_bot code for correctness
```

---

## Metrics to Track

| Metric | Target | Status |
|--------|--------|--------|
| Cyclomatic Complexity | < 10 | 🟢 Good |
| Nesting Depth | < 3 levels | 🟡 Warning |
| Function Parameters | < 5-7 | 🔴 Critical |
| Lines per Function | < 50 | ✅ OK |
| Over-engineered patterns | 0 | ✅ None |

---

## Key Files Updated

1. **bot-audit.instructions.md** (464 lines)
   - Added Q6 COMPLEXIDADE category
   - Updated priority levels with complexity metrics
   - Extended anti-patterns table

2. **code-simplification.instructions.md** (553 lines) - NEW
   - 5 core principles
   - 4 complexity metrics
   - 5 anti-patterns
   - 4 simplification patterns
   - Workflow templates

3. **agents.md** (version 1.9)
   - Enhanced @backend capabilities
   - Updated Decision Matrix
   - New version history entry

---

## Expected Outcomes

✅ **Performance**: Fewer abstractions = less overhead  
✅ **Quality**: Simpler code = fewer bugs  
✅ **Maintainability**: Clearer logic = faster debugging  
✅ **Testability**: Smaller functions = easier tests  

---

## Next Steps

1. **Week 1**: Run audit with Q6 questions on all 4 bots
2. **Week 2-3**: @backend simplifies identified functions
3. **Week 4**: Validate changes and update Memory Banks
4. **Ongoing**: Track metrics quarterly

---

**See Also**:
- Complete guide: `/.github/instructions/code-simplification.instructions.md`
- Audit system: `/.github/instructions/bot-audit.instructions.md`
- Agent roles: `/home/admin/agents.md`

