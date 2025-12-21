---
name: database-optimization
description: Optimize SQL queries, analyze indexes, review Alembic migrations, and identify N+1 problems. Provides query execution plans, index recommendations, and migration best practices for SQLAlchemy async.
---

# Database Optimization Skill

## When to Use

Use this skill when:
- Optimizing slow SQL queries
- Analyzing missing or redundant indexes
- Reviewing Alembic migrations for safety
- Identifying N+1 query problems
- Designing database schemas
- Planning data migrations
- Reviewing query execution plans

## Optimization Checklist

### 1. Index Analysis

```sql
-- Check missing indexes
SELECT schemaname, tablename, indexname, indexdef
FROM pg_indexes
WHERE tablename = 'your_table';

-- Identify unused indexes
SELECT * FROM pg_stat_user_indexes
WHERE idx_scan = 0;
```

**Index Recommendations:**
```
✅ Always index:
- Primary keys (automatic)
- Foreign keys
- Columns in WHERE clauses
- Columns in ORDER BY
- Columns in JOIN conditions

❌ Avoid indexing:
- Low cardinality columns (boolean, status)
- Frequently updated columns
- Small tables (<1000 rows)
```

### 2. N+1 Query Detection

```python
# ❌ N+1 Problem
users = await session.execute(select(User))
for user in users:
    # This triggers N additional queries!
    orders = await session.execute(
        select(Order).where(Order.user_id == user.id)
    )

# ✅ Solution: Eager loading
from sqlalchemy.orm import selectinload

users = await session.execute(
    select(User).options(selectinload(User.orders))
)
```

### 3. Query Optimization Patterns

```python
# ✅ Use pagination
from sqlalchemy import select
from app.models import Product

async def get_products(skip: int = 0, limit: int = 20):
    query = select(Product).offset(skip).limit(limit)
    result = await session.execute(query)
    return result.scalars().all()

# ✅ Use specific columns (not SELECT *)
query = select(Product.id, Product.name, Product.price)

# ✅ Use exists() for existence checks
from sqlalchemy import exists
query = select(exists().where(User.email == email))
```

### 4. Migration Safety

```python
# ✅ Safe migration patterns
def upgrade():
    # Add column with default (no table lock)
    op.add_column('users', sa.Column('status', sa.String(20), 
                                      server_default='active'))

# ❌ Dangerous patterns
def upgrade():
    # Avoid: Rename column (breaks app)
    op.alter_column('users', 'name', new_column_name='full_name')
    
    # Avoid: Change column type (data loss risk)
    op.alter_column('users', 'age', type_=sa.String())
```

### 5. Async Best Practices

```python
# ✅ Proper async session handling
from sqlalchemy.ext.asyncio import AsyncSession

async def get_user(session: AsyncSession, user_id: int):
    result = await session.execute(
        select(User).where(User.id == user_id)
    )
    return result.scalar_one_or_none()

# ✅ Bulk operations
async def bulk_insert(session: AsyncSession, items: list):
    session.add_all(items)
    await session.commit()
```

## Output Format

```markdown
## Database Optimization Report

### Query Analysis
- Queries analyzed: X
- Slow queries (>100ms): X
- N+1 problems: X

### Index Recommendations
| Table | Column | Type | Reason |
|-------|--------|------|--------|
| users | email | UNIQUE | WHERE clause filter |
| orders | user_id | INDEX | Foreign key JOIN |

### Optimization Suggestions
1. [Query] - [Current time] - [Optimized time] - [How]

### Migration Review
- ✅ Safe to run
- ⚠️ Requires maintenance window
- ❌ Breaking change detected
```

## Example Usage

```
@database Optimize the slow query in order_service.py:120
@database Review the new migration for safety issues
@database Find N+1 problems in the user module
@database Suggest indexes for the products table
```
