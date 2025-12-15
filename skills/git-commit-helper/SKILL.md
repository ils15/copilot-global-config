---
name: git-commit-helper
description: Generate conventional commit messages from git diff. Follows conventional commits format (feat, fix, docs, etc.) with clear descriptions and optional body/footer for breaking changes.
---

# Git Commit Helper

Generate well-formatted conventional commit messages from your staged changes.

## What This Skill Does

Analyzes `git diff --staged` and generates commit messages following [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

## When to Use This Skill

- You have staged changes ready to commit
- You want to follow conventional commits
- You need help writing clear commit messages
- You're working in a team with commit standards

## Commit Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style (formatting, semicolons, etc)
- `refactor`: Code refactoring (no feature/fix)
- `perf`: Performance improvements
- `test`: Adding/updating tests
- `build`: Build system/dependencies
- `ci`: CI/CD configuration
- `chore`: Maintenance tasks

## How to Use

1. **Stage your changes**:
   ```bash
   git add <files>
   ```

2. **Show me the diff**:
   ```bash
   git diff --staged
   ```

3. **I'll generate a commit message** in this format:
   ```
   type(scope): clear description
   
   [Detailed explanation if needed]
   
   [Breaking changes if any]
   ```

4. **Review and commit**:
   ```bash
   git commit -m "generated message"
   ```

## Examples

### Example 1: New Feature
**Diff**:
```diff
+ def send_email(to: str, subject: str, body: str):
+     """Send email via SMTP"""
+     smtp = smtplib.SMTP(...)
+     smtp.send_message(...)
```

**Commit**:
```
feat(email): add SMTP email sending functionality

Implement send_email function using smtplib
Supports plain text and HTML emails
```

### Example 2: Bug Fix
**Diff**:
```diff
- if user.is_authenticated:
+ if user and user.is_authenticated:
      return redirect('/dashboard')
```

**Commit**:
```
fix(auth): prevent AttributeError when user is None

Add null check before accessing user.is_authenticated
Fixes crash on logout redirect
```

### Example 3: Documentation
**Diff**:
```diff
+ ## Installation
+ 
+ ```bash
+ pip install -r requirements.txt
+ ```
```

**Commit**:
```
docs(readme): add installation instructions
```

### Example 4: Refactoring
**Diff**:
```diff
- def process_data(data):
-     result = []
-     for item in data:
-         result.append(item * 2)
-     return result
+ def process_data(data):
+     return [item * 2 for item in data]
```

**Commit**:
```
refactor(utils): simplify process_data with list comprehension

Replace loop with more Pythonic list comprehension
Same functionality, more concise
```

### Example 5: Breaking Change
**Diff**:
```diff
- def get_user(id: int) -> dict:
+ def get_user(id: int) -> User:
      """Get user by ID"""
-     return {"id": id, "name": "..."}
+     return User(id=id, name="...")
```

**Commit**:
```
feat(users): return User model instead of dict

BREAKING CHANGE: get_user() now returns User object instead of dict
Update all callers to access user.id instead of user["id"]
```

## Message Guidelines

### Subject Line
- Use imperative mood ("add" not "added")
- Don't capitalize first letter
- No period at the end
- Max 50 characters
- Be specific and clear

### Body (Optional)
- Explain **why** the change was made
- Describe **what** changed at high level
- Mention side effects or implications
- Wrap at 72 characters

### Footer (Optional)
- Reference issues: `Closes #123`
- Note breaking changes: `BREAKING CHANGE: ...`
- Co-authors: `Co-authored-by: Name <email>`

## Scope Examples by Project Area

**Backend API**:
- `(auth)` - Authentication
- `(users)` - User management
- `(products)` - Product features
- `(api)` - API endpoints
- `(db)` - Database

**Frontend**:
- `(ui)` - UI components
- `(forms)` - Forms
- `(routing)` - Navigation
- `(state)` - State management
- `(styles)` - Styling

**Infrastructure**:
- `(docker)` - Docker configuration
- `(ci)` - CI/CD pipelines
- `(deploy)` - Deployment
- `(nginx)` - Web server
- `(db)` - Database

**Bots/Services**:
- `(bots)` - Telegram bots
- `(webhook)` - Webhook handlers
- `(scheduler)` - Scheduled tasks
- `(queue)` - Message queues

## Anti-Patterns to Avoid

❌ Vague messages: `fix bug` → ✅ `fix(auth): prevent null pointer in login`
❌ Too long: 100+ char → ✅ Keep under 50 chars
❌ Past tense: `added feature` → ✅ `add feature`
❌ No scope: `fix something` → ✅ `fix(users): something`
❌ Multiple changes: → ✅ Split into multiple commits

## Good vs Bad Examples

**Bad**:
```
fixed stuff
```

**Good**:
```
fix(api): handle timeout errors in product endpoint

Add try-catch for network timeouts
Return 503 instead of crashing
Closes #456
```

---

**Bad**:
```
Updated code and docs and tests
```

**Good** (split into 3 commits):
```
refactor(users): extract validation logic to separate function
docs(api): update user endpoint documentation
test(users): add tests for email validation
```

---

**Bad**:
```
WIP
```

**Good**:
```
feat(dashboard): add initial dashboard layout

Components ready for review
Still needs: data fetching, error handling
```

## Workflow Integration

### Standard Workflow
```bash
# 1. Make changes
vim src/feature.py

# 2. Stage changes
git add src/feature.py

# 3. Review diff
git diff --staged

# 4. Get commit message suggestion (use this skill)
# Show diff to Claude and ask for commit message

# 5. Commit with generated message
git commit -m "feat(feature): add new capability"

# 6. Push
git push origin feature-branch
```

### Pre-commit Hook (Optional)
Create `.git/hooks/prepare-commit-msg`:
```bash
#!/bin/bash
# Validate commit message format
COMMIT_MSG_FILE=$1
MSG=$(cat $COMMIT_MSG_FILE)

if ! echo "$MSG" | grep -qE '^(feat|fix|docs|style|refactor|perf|test|build|ci|chore)(\(.+\))?: .+'; then
    echo "❌ Commit message must follow conventional commits format"
    echo "Examples:"
    echo "  feat(auth): add login endpoint"
    echo "  fix(users): prevent null pointer error"
    exit 1
fi
```

## Reference

- Conventional Commits: https://www.conventionalcommits.org/
- Git Commit Guidelines: https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project
- Semantic Versioning: https://semver.org/
