---
name: tdd-testing
description: "Test-Driven Development methodology - RED, GREEN, REFACTOR cycle for all implementations"
---

# TDD Testing Skill

## When to Use
- Qualquer nova feature implementation
- Bug fixes
- Quando quer confidence que código funciona

## TDD Cycle

### Phase 1: RED - Write Failing Test
```python
def test_user_creation():
    user_service = UserService(db, cache)
    user = user_service.create_user({
        "email": "test@example.com",
        "name": "Test User"
    })
    assert user.id is not None
    assert user.email == "test@example.com"
```

### Phase 2: GREEN - Minimal Code to Pass
```python
class UserService:
    async def create_user(self, data):
        user = User(**data)
        await self.db.add(user)
        return user
```

### Phase 3: REFACTOR - Improve Without Breaking
```python
class UserService:
    async def create_user(self, data):
        # Add validation
        self.validate_email(data["email"])
        
        # Add deduplication
        existing = await self.db.query(User).filter(
            User.email == data["email"]
        ).first()
        if existing:
            raise UserAlreadyExists()
        
        user = User(**data)
        await self.db.add(user)
        return user
```

## Best Practices
- 1 test → 1 feature
- Keep tests focused and small
- Test behavior, not implementation
- Rerun tests frequently
- Use fixtures for setup
- Mock external dependencies

## Tools Needed
- unittest / pytest
- Mock (for dependencies)
- Faker (for test data)

## Success Metrics
- >80% code coverage
- All tests pass
- Tests run in <30 seconds
- No flaky tests
