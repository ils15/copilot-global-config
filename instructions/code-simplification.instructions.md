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

Code must be:
- **Obvious**: A junior developer should understand it without deep analysis
- **Readable**: Logic flow should be immediately clear
- **Maintainable**: Easy to debug, test, and modify

**Red Flags**:
- ❌ "This is clever code" = sign of over-engineering
- ❌ Complex one-liners instead of clear multi-line code
- ❌ Custom patterns when stdlib alternatives exist
- ❌ Abstraction levels that add no practical value

### **2. Pragmatism Over Patterns**

Use:
- ✅ Simple if/else instead of complex state machines
- ✅ Direct function calls instead of decorator chains
- ✅ Built-in libraries instead of custom abstractions
- ✅ Explicit error handling instead of silent try/except

### **3. Performance Through Clarity**

Simpler code = faster code because:
- Fewer indirections to trace
- Better compiler/interpreter optimizations
- Fewer runtime checks and conversions
- Easier to profile and optimize

---

## 📊 Complexity Metrics to Target

### **Cyclomatic Complexity (CC)**

Measures decision paths in code. Target: **< 10 per function**

```python
# ❌ BAD: CC = 8+ (too many decision paths)
def handle_command(user_id, command, args):
    if not user_id:
        return error
    if not is_admin(user_id):
        if is_premium(user_id):
            if validate_command(command):
                if not rate_limited(user_id):
                    if len(args) > 0:
                        if check_permissions(user_id, command):
                            return execute(command, args)
                        else:
                            return permission_error
                    else:
                        return missing_args_error
                else:
                    return rate_limit_error
            else:
                return invalid_command_error
        else:
            return premium_required_error
    else:
        if validate_command(command):
            return execute(command, args)
        else:
            return invalid_command_error

# ✅ GOOD: CC = 3 (early returns reduce nesting)
def handle_command(user_id, command, args):
    # Validate prerequisites
    if not user_id or not command:
        return error("Invalid input")
    
    # Check permissions
    if not can_execute_command(user_id, command):
        return permission_error(user_id, command)
    
    # Validate arguments
    if not args:
        return error("Missing arguments")
    
    # Rate limiting
    if rate_limited(user_id):
        return error("Rate limited")
    
    # Execute
    return execute(command, args)
```

**How to Measure**:
```bash
# Using radon (Python complexity analyzer)
pip install radon
radon cc bots/my_bot -a  # Show average complexity
radon mi bots/my_bot     # Maintainability Index
```

### **Nesting Depth**

Maximum: **3 levels** (preferably < 2)

```python
# ❌ BAD: 4 levels deep (nested hell)
for group in groups:
    if group.active:
        for member in group.members:
            if member.role == "admin":
                try:
                    result = api.call(member)
                    if result.success:
                        log.info("Success")
                except Exception:
                    pass

# ✅ GOOD: 2 levels max with early continues
for group in groups:
    if not group.active:
        continue
    
    for member in group.members:
        if member.role != "admin":
            continue
        
        try:
            result = api.call(member)
        except Exception:
            log.error(f"API failed for {member}")
            continue
        
        if result.success:
            log.info("Success")
```

**Technique**: Use `continue`, `break`, early `return` to reduce nesting

### **Function Parameters**

Maximum: **5-7 parameters** (preferably < 5)

```python
# ❌ BAD: 9 parameters (impossible to call correctly)
def process_data(
    data, user_id, group_id, admin_id, timestamp, 
    validate, notify, cache, retry
):
    ...

# ✅ GOOD: Use config object or dictionary
def process_data(data: dict, context: ProcessContext) -> dict:
    """
    Args:
        data: Raw input data
        context: Contains user_id, group_id, admin_id, etc
    """
    ...

# Or use dataclass
@dataclass
class ProcessContext:
    user_id: int
    group_id: int
    admin_id: int
    timestamp: datetime
    validate: bool
    notify: bool
    cache: bool
    retry: int
```

### **Lines per Function**

Maximum: **50 lines** (preferably < 30)

If function > 50 lines:
1. Extract helper functions
2. Break into smaller methods
3. Use composition instead of single monolithic function

---

## 🔴 Anti-Patterns to Eliminate

### **1. Over-Engineered Abstractions**

```python
# ❌ BAD: Abstract factory pattern for simple thing
class CommandFactory:
    @staticmethod
    def create(command_type):
        if command_type == "admin":
            return AdminCommand()
        elif command_type == "user":
            return UserCommand()
        # ... 10 more conditions

# ✅ GOOD: Simple dictionary
COMMANDS = {
    "admin": AdminCommand,
    "user": UserCommand,
}

def get_command(command_type):
    return COMMANDS.get(command_type)()
```

### **2. Silent Exception Handlers**

```python
# ❌ BAD: Hiding errors
try:
    result = api.call()
except Exception:
    pass  # ← Nobody knows it failed!

# ✅ GOOD: Log and handle appropriately
try:
    result = api.call()
except TimeoutError:
    logger.warning(f"API timeout for {request_id}")
    return None
except Exception as e:
    logger.error(f"API failed: {e}", exc_info=True)
    raise  # Re-raise if unrecoverable
```

### **3. Overly Generic Type Hints**

```python
# ❌ BAD: `Any` hides actual types
def process(data: Any) -> Any:
    ...

# ✅ GOOD: Explicit types
from typing import Dict, List, Optional

def process(data: Dict[str, List[str]]) -> Optional[Dict]:
    ...
```

### **4. Deep Class Hierarchies**

```python
# ❌ BAD: 4+ levels of inheritance
class BaseCommand: pass
class AdminCommand(BaseCommand): pass
class AdvancedAdminCommand(AdminCommand): pass
class SuperSpecialAdminCommand(AdvancedAdminCommand): pass

# ✅ GOOD: Composition with simple classes
@dataclass
class Command:
    name: str
    handler: Callable
    requires_admin: bool = False
    requires_premium: bool = False
```

### **5. Multiple Responsibilities Per Class**

```python
# ❌ BAD: God object (27 methods)
class UserManager:
    def authenticate(self): ...
    def get_user(self): ...
    def update_profile(self): ...
    def send_notification(self): ...
    def check_permissions(self): ...
    def process_payment(self): ...
    def generate_report(self): ...
    # ... 20 more methods!

# ✅ GOOD: Separated concerns
class UserRepository:
    def authenticate(self): ...
    def get_user(self): ...
    def update_profile(self): ...

class NotificationService:
    def send(self): ...

class PermissionManager:
    def check_permissions(self): ...

class PaymentProcessor:
    def process(self): ...
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
            if user.verified:
                return True
    return False

# ✅ After
def validate_user(user_id):
    user = get_user(user_id)
    if not user:
        return False
    if not user.active:
        return False
    return user.verified
```

### **Pattern 2: Extract Constants (Reduce Magic Numbers)**

```python
# ❌ Before
if user.score > 1000 and days_active > 365:
    if random() > 0.8:
        give_reward()

# ✅ After
PREMIUM_SCORE_THRESHOLD = 1000
MIN_DAYS_ACTIVE = 365
REWARD_PROBABILITY = 0.2  # 1 - 0.8

if user.score > PREMIUM_SCORE_THRESHOLD and days_active > MIN_DAYS_ACTIVE:
    if random() < REWARD_PROBABILITY:
        give_reward()
```

### **Pattern 3: Guard Clauses (Validate First)**

```python
# ❌ Before
def process_order(order):
    if order and order.valid:
        if order.items:
            total = 0
            for item in order.items:
                if item.in_stock:
                    total += item.price
            return total
    return None

# ✅ After
def process_order(order):
    if not order or not order.valid:
        return None
    if not order.items:
        return None
    
    return sum(
        item.price for item in order.items 
        if item.in_stock
    )
```

### **Pattern 4: Replace Conditionals with Polymorphism (When Appropriate)**

```python
# ❌ Before (many conditions)
def send_notification(user, message, channel):
    if channel == "email":
        email_service.send(user.email, message)
    elif channel == "sms":
        sms_service.send(user.phone, message)
    elif channel == "push":
        push_service.send(user.device, message)
    else:
        log_error("Unknown channel")

# ✅ After (but only if you have 3+ handlers AND they're complex)
class NotificationHandler:
    def send(self, user, message): pass

handlers = {
    "email": EmailHandler(),
    "sms": SMSHandler(),
    "push": PushHandler(),
}

def send_notification(user, message, channel):
    handler = handlers.get(channel)
    if not handler:
        log_error(f"Unknown channel: {channel}")
        return
    handler.send(user, message)
```

---

## 📋 Simplification Checklist

When reviewing code for complexity:

### **Structure**
- [ ] No function > 50 lines
- [ ] No class > 300 lines
- [ ] No class with > 10 methods
- [ ] Max 3 levels of nesting
- [ ] Max 5-7 function parameters
- [ ] Single Responsibility Principle (SRP) enforced

### **Clarity**
- [ ] Variable names are descriptive (not `x`, `tmp`, `data`)
- [ ] Function names describe what they do
- [ ] Complex logic has explanatory comments
- [ ] No "clever" code that sacrifices readability
- [ ] No magic numbers (all extracted to constants)

### **Error Handling**
- [ ] No silent `except: pass` blocks
- [ ] All exceptions logged with context
- [ ] Errors propagate or are handled explicitly
- [ ] No swallowing of stack traces

### **Performance**
- [ ] No obvious O(n²) or O(n³) algorithms
- [ ] Database queries don't fetch everything
- [ ] No unnecessary object creation in loops
- [ ] Proper connection pooling and cleanup

### **Maintainability**
- [ ] Code follows project conventions
- [ ] Type hints present (Python)
- [ ] Docstrings explain "why" not "what"
- [ ] Easy to write tests
- [ ] Easy to debug

---

## 🛠️ Refactoring Workflow (Via @backend Agent)

**When to Trigger**:
```
1. Audit finds Q6.1 - Q6.5 complexity issues
2. Function has CC > 15
3. Nesting > 4 levels
4. >7 function parameters
5. Over-engineered pattern detected
```

**Workflow**:
```
@backend Simplify [module/file]:
- Reduce cyclomatic complexity from X to <10
- Break nested if/else into guard clauses
- Extract helper functions for clarity
- Replace over-engineering with pragmatic patterns

Return: Before/after comparison with metrics
```

**Refactoring Steps**:
1. **Measure** current complexity
2. **Identify** complexity sources (nesting, conditions, parameters)
3. **Refactor** with simplification patterns
4. **Validate** functionality unchanged
5. **Test** to ensure no regressions
6. **Measure** new complexity (should be < 10)

---

## 📈 Expected Improvements

### **Performance Impact**
- **Simpler code** = less CPU/memory overhead
- **Fewer abstractions** = fewer function calls
- **Better code paths** = compiler optimizations possible
- **Clearer logic** = easier to cache/optimize

### **Maintainability Impact**
- **Easier debugging** (shorter stack traces, clearer logic)
- **Faster onboarding** (new devs understand faster)
- **Fewer bugs** (simpler = fewer places to hide bugs)
- **Easier testing** (simpler functions easier to unit test)

### **Metrics to Track**
```
Before Refactoring:
- Max CC per function: 18
- Max nesting depth: 5
- Avg function size: 80 lines
- % functions > 50 lines: 35%

After Refactoring:
- Max CC per function: 8
- Max nesting depth: 2
- Avg function size: 25 lines
- % functions > 50 lines: 5%
```

---

## 🚀 Quarterly Simplification Sprint

### **Phase 1: Audit & Discovery (Week 1)**
- Run audit with Q6.1-Q6.5 complexity questions
- Identify top 10 worst functions (by CC, nesting, size)
- Document current metrics baseline
- Prioritize refactoring targets

### **Phase 2: Refactoring (Week 2-3)**
- @backend refactors top functions
- Keep tests passing
- Document patterns used and lessons learned
- Update bot Memory Banks with simplifications

### **Phase 3: Validation (Week 4)**
- Full test suite passes
- Performance benchmarks show improvement (or no regression)
- Code review confirms quality
- Update agents.md with new patterns

### **Phase 4: Documentation (Ongoing)**
- Update Memory Bank with simplification patterns
- Document which anti-patterns were eliminated
- Share learnings across bot ecosystem

---

## 📚 References

- **Cyclomatic Complexity**: [McComish et al](https://en.wikipedia.org/wiki/Cyclomatic_complexity)
- **Code Simplicity**: [Code Simplicity by Max Kanat-Alexander](https://www.codesimplicity.com/)
- **Pragmatic Programmer**: [Chapter 8: Pragmatic Paranoia](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-your-journey-to-mastery-20th-anniversary-edition/)
- **Radon (Python Complexity)**: [radon.readthedocs.io](https://radon.readthedocs.io/)

---

**Version**: 1.0  
**Created**: 2025-12-14  
**Owner**: @backend (Complexity Expert)  
**Integration**: bot-audit.instructions.md (Q6 - COMPLEXIDADE)

