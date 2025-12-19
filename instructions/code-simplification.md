---
applyTo: 'bots/**'
description: 'Code Simplification & Complexity Reduction Guidelines for Bot Ecosystem'
---

# Code Simplification & Complexity Reduction

## Overview

**Problem**: Ofertachina bots suffer from over-engineered patterns, unnecessary abstractions, and complex code that reduces performance and maintainability.

**Solution**: Systematic code simplification guided by complexity metrics and pragmatic design principles.

**Owner**: `@backend` agent (Complexity Expert for bots)

---

## 🎯 Core Principles

### **1. Simplicity > Cleverness**
Code must be obvious, readable, maintainable. Red flags: "clever code", complex one-liners, custom patterns over stdlib, unnecessary abstractions.

### **2. Pragmatism Over Patterns**
Use simple if/else instead of state machines, direct calls instead of decorator chains, built-in libraries over custom abstractions, explicit error handling.

### **3. Performance Through Clarity**
Simpler code = faster code: fewer indirections, better optimizations, fewer runtime checks, easier profiling.

---

## 📊 Complexity Metrics

### **Cyclomatic Complexity (CC)**
Target: **< 10 per function**

```python
# ❌ BAD: CC = 8+ (too many paths)
def handle_command(user_id, command, args):
    if not user_id: return error
    if not is_admin(user_id):
        if is_premium(user_id):
            if validate_command(command):
                # ... many nested conditions

# ✅ GOOD: CC = 3 (early returns)
def handle_command(user_id, command, args):
    if not user_id or not command: return error("Invalid input")
    if not can_execute_command(user_id, command): return permission_error(user_id, command)
    if not args: return error("Missing arguments")
    if rate_limited(user_id): return error("Rate limited")
    return execute(command, args)
```

### **Nesting Depth**
Maximum: **3 levels** (preferably < 2)

```python
# ❌ BAD: 4 levels deep
for group in groups:
    if group.active:
        for member in group.members:
            if member.role == "admin":
                try: result = api.call(member)
                except: pass

# ✅ GOOD: 2 levels max with continues
for group in groups:
    if not group.active: continue
    for member in group.members:
        if member.role != "admin": continue
        try: result = api.call(member)
        except Exception: log.error(f"API failed for {member}")
        if result.success: log.info("Success")
```

### **Function Parameters**
Maximum: **5-7 parameters** (preferably < 5)

```python
# ❌ BAD: 9 parameters
def process_data(data, user_id, group_id, admin_id, timestamp, validate, notify, cache, retry): ...

# ✅ GOOD: Use config object
def process_data(data: dict, context: ProcessContext) -> dict: ...
```

### **Lines per Function**
Maximum: **50 lines** (preferably < 30)

---

## 🔴 Anti-Patterns to Eliminate

### **1. Over-Engineered Abstractions**
```python
# ❌ BAD: Abstract factory for simple thing
class CommandFactory:
    @staticmethod
    def create(command_type):
        if command_type == "admin": return AdminCommand()
        # ... 10 more conditions

# ✅ GOOD: Simple dictionary
COMMANDS = {"admin": AdminCommand, "user": UserCommand}
def get_command(command_type): return COMMANDS.get(command_type)()
```

### **2. Silent Exception Handlers**
```python
# ❌ BAD: Hiding errors
try: result = api.call()
except Exception: pass  # Nobody knows it failed!

# ✅ GOOD: Log and handle
try: result = api.call()
except TimeoutError: logger.warning(f"API timeout"); return None
except Exception as e: logger.error(f"API failed: {e}"); raise
```

### **3. Multiple Responsibilities Per Class**
```python
# ❌ BAD: God object (27 methods)
class UserManager:  # authenticate, get_user, update_profile, etc.

# ✅ GOOD: Separated concerns
class UserRepository: def authenticate(self): ...
class NotificationService: def send(self): ...
```

---

## ✅ Simplification Patterns

### **Pattern 1: Early Returns (Reduce Nesting)**
```python
# ❌ Before
def validate_user(user_id):
    user = get_user(user_id)
    if user:
        if user.active:
            if user.verified: return True
    return False

# ✅ After
def validate_user(user_id):
    user = get_user(user_id)
    if not user: return False
    if not user.active: return False
    return user.verified
```

### **Pattern 2: Extract Constants (Reduce Magic Numbers)**
```python
# ❌ Before
if user.score > 1000 and days_active > 365:
    if random() > 0.8: give_reward()

# ✅ After
PREMIUM_SCORE_THRESHOLD = 1000
MIN_DAYS_ACTIVE = 365
REWARD_PROBABILITY = 0.2

if user.score > PREMIUM_SCORE_THRESHOLD and days_active > MIN_DAYS_ACTIVE:
    if random() < REWARD_PROBABILITY: give_reward()
```

---

## 📋 Simplification Checklist

### **Structure**
- [ ] No function > 50 lines
- [ ] No class > 300 lines
- [ ] Max 3 levels of nesting
- [ ] Max 5-7 function parameters
- [ ] Single Responsibility Principle

### **Clarity**
- [ ] Descriptive variable names
- [ ] Function names describe actions
- [ ] No magic numbers
- [ ] No "clever" code

### **Error Handling**
- [ ] No silent `except: pass`
- [ ] All exceptions logged
- [ ] Errors handled explicitly

### **Performance**
- [ ] No O(n²) algorithms
- [ ] Efficient database queries
- [ ] No unnecessary object creation

---

## 🛠️ Refactoring Workflow

**When to Trigger**: CC > 15, nesting > 4 levels, >7 parameters, over-engineered patterns

**Workflow**:
```
@backend Simplify [module/file]:
- Reduce CC from X to <10
- Break nested if/else into guard clauses
- Extract helper functions
- Replace over-engineering with pragmatic patterns

Return: Before/after comparison with metrics
```

**Steps**:
1. Measure current complexity
2. Identify sources (nesting, conditions, parameters)
3. Refactor with patterns
4. Validate functionality
5. Test for regressions
6. Measure new complexity (< 10)

---

## 📈 Expected Improvements

### **Performance Impact**
- Less CPU/memory overhead
- Fewer function calls
- Better compiler optimizations
- Easier to cache/optimize

### **Maintainability Impact**
- Easier debugging
- Faster onboarding
- Fewer bugs
- Easier testing

### **Metrics to Track**
```
Before: Max CC 18, Max nesting 5, Avg size 80 lines, 35% >50 lines
After: Max CC 8, Max nesting 2, Avg size 25 lines, 5% >50 lines
```

---

## 🚀 Quarterly Simplification Sprint

### **Phase 1: Audit & Discovery**
- Run complexity audit
- Identify top 10 worst functions
- Document baseline metrics
- Prioritize targets

### **Phase 2: Refactoring**
- @backend refactors top functions
- Keep tests passing
- Document patterns used

### **Phase 3: Validation**
- Full test suite passes
- Performance benchmarks
- Code review

### **Phase 4: Documentation**
- Update Memory Bank
- Share learnings

---

## 📚 References

- **Cyclomatic Complexity**: Wikipedia
- **Code Simplicity**: Max Kanat-Alexander
- **Radon (Python Complexity)**: radon.readthedocs.io

---

**Version**: 1.0  
**Owner**: @backend  
**Integration**: bot-audit.instructions.md (Q6 - COMPLEXIDADE)

