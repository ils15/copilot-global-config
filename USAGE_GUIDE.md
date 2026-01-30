# 🚀 Generic Agents Usage Guide

This guide shows how to use the refactored **generic agents** for any software project using the `runSubagent` orchestration pattern.

## 🎯 Quick Start: Orchestrating a Feature

### Example 1: Building a User Authentication System (Any Stack)

```javascript
// Step 1: Plan the feature
const plan = await runSubagent({
  agentName: 'planner-architect',
  description: 'Plan auth system',
  prompt: `Plan a user authentication system with:
    - User registration
    - Login with JWT/session
    - Password reset flow
    - 2FA support
  
  Use TDD approach. Consider security best practices.`
});

// Step 2: Discover existing auth files (if project exists)
const discoveries = await Promise.all([
  runSubagent({
    agentName: 'explorer',
    description: 'Find auth files',
    prompt: 'Locate all authentication-related files, middleware, and patterns in codebase'
  }),
  runSubagent({
    agentName: 'explorer',
    description: 'Find user models',
    prompt: 'Find all user entity definitions, models, and schemas'
  })
]);

// Step 3: Parallel implementation
const implementations = await Promise.all([
  runSubagent({
    agentName: 'domain-implementer',
    description: 'Implement auth API',
    prompt: `Implement authentication endpoints:
      - POST /auth/register (validation, hash password)
      - POST /auth/login (verify credentials, return token)
      - POST /auth/refresh (refresh expired token)
      - POST /auth/logout (invalidate token)
      
      Follow the plan. Use TDD. Add proper error handling.`,
    base_ref: 'main'  // optional: which branch to work from
  }),
  runSubagent({
    agentName: 'database-implementer',
    description: 'Create user schema',
    prompt: `Create/migrate database schema for:
      - users table (id, email, password_hash, created_at)
      - roles table (id, name)
      - user_roles junction table
      
      Add proper indexes and constraints.`
  }),
  runSubagent({
    agentName: 'ui-implementer',
    description: 'Build auth forms',
    prompt: `Build reusable authentication UI components:
      - LoginForm component
      - RegisterForm component  
      - PasswordResetForm component
      - 2FA verification component
      
      Include validation and error display.`
  })
]);

// Step 4: Code review
const review = await runSubagent({
  agentName: 'code-reviewer',
  description: 'Review auth implementation',
  prompt: `Review the authentication implementation for:
    - Correctness of JWT/session handling
    - Password security (hashing, salt)
    - Input validation and injection prevention
    - Error handling (no sensitive info leaks)
    - Test coverage (>80%)
    - OWASP Top 10 compliance
    
    Focus on security issues especially.`
});

// Step 5: Deployment
if (review.status === 'APPROVED') {
  await runSubagent({
    agentName: 'infra-implementer',
    description: 'Deploy auth service',
    prompt: `Create deployment configuration for authentication service:
      - Container image with proper secrets handling
      - Environment variables (DB_HOST, JWT_SECRET, etc.)
      - Health checks for auth endpoints
      - Zero-downtime deployment strategy`
  });
}
```

## 📋 Common Usage Patterns

### Pattern 1: Build a CRUD Feature (Minimal)

```javascript
async function buildFeature(featureName, description) {
  // 1. Plan
  await runSubagent({
    agentName: 'planner-architect',
    description: `Plan ${featureName}`,
    prompt: `Create a TDD implementation plan for: ${description}`
  });

  // 2. Implement in parallel
  await Promise.all([
    runSubagent({
      agentName: 'domain-implementer',
      description: `Implement ${featureName} API`,
      prompt: `Build CRUD endpoints for ${featureName}: create, read, list, update, delete`
    }),
    runSubagent({
      agentName: 'database-implementer',
      description: `Create ${featureName} schema`,
      prompt: `Design and migrate database schema for ${featureName}`
    }),
    runSubagent({
      agentName: 'ui-implementer',
      description: `Build ${featureName} UI`,
      prompt: `Create CRUD UI components for ${featureName}`
    })
  ]);

  // 3. Review
  await runSubagent({
    agentName: 'code-reviewer',
    description: `Review ${featureName}`,
    prompt: `Review all ${featureName} implementation for quality and security`
  });
}

// Usage
await buildFeature('Product Management', 'Admin dashboard to manage products');
```

### Pattern 2: Investigate Performance Issue

```javascript
async function investigatePerformance(symptom) {
  // 1. Discover related files
  const findings = await runSubagent({
    agentName: 'explorer',
    description: 'Find performance-critical code',
    prompt: `Find all files related to: ${symptom}. 
      Look for: database queries, loops, API calls, external integrations`
  });

  // 2. Analyze and plan optimization
  const plan = await runSubagent({
    agentName: 'planner-architect',
    description: 'Plan optimization',
    prompt: `Based on these files: ${findings}
      Create an optimization plan focusing on:
      - Database query optimization (N+1 queries, proper indexes)
      - Caching strategies
      - API response time reduction`
  });

  // 3. Implement optimization
  await runSubagent({
    agentName: 'domain-implementer',
    description: 'Optimize code',
    prompt: `Implement the optimization plan: ${plan}`
  });

  // 4. Review and measure
  await runSubagent({
    agentName: 'code-reviewer',
    description: 'Review optimization',
    prompt: `Review optimization implementation. Verify:
      - Performance improvement
      - No regressions
      - Proper test coverage`
  });
}

// Usage
await investigatePerformance('Slow product listing page takes 5+ seconds');
```

### Pattern 3: Refactor Legacy Code

```javascript
async function refactorCode(module) {
  // 1. Understand current state
  const analysis = await runSubagent({
    agentName: 'explorer',
    description: `Analyze ${module}`,
    prompt: `Map all files in the ${module} module:
      - Entry points
      - Public APIs
      - Dependencies
      - Tests
      - Documentation`
  });

  // 2. Plan refactor
  const refactorPlan = await runSubagent({
    agentName: 'planner-architect',
    description: `Plan ${module} refactor`,
    prompt: `Create refactoring plan for ${module}:
      - Identify tech debt and issues
      - Propose modern patterns
      - Plan incremental changes
      - Each phase should be testable`
  });

  // 3. Implement phase by phase
  for (let phase of refactorPlan.phases) {
    await runSubagent({
      agentName: 'domain-implementer',
      description: `Refactor ${module} - Phase ${phase.number}`,
      prompt: `Execute this refactoring phase: ${phase.description}
        
        Constraints:
        - Keep all tests passing
        - No breaking changes to public API
        - Each commit must be atomic`
    });

    // Review each phase
    await runSubagent({
      agentName: 'code-reviewer',
      description: `Review Phase ${phase.number}`,
      prompt: `Review this refactoring phase for correctness and test coverage`
    });
  }
}

// Usage
await refactorCode('User Authentication Module');
```

## 🎨 Tech Stack Examples

### Node.js + React + PostgreSQL

```javascript
await runSubagent({
  agentName: 'domain-implementer',
  description: 'Implement user API',
  prompt: `Implement user REST API using Express.js:
    - POST /users (create user, validate input)
    - GET /users/:id (fetch user data)
    - PUT /users/:id (update user)
    - DELETE /users/:id (soft delete)
    
    Use TDD with Jest tests. Handle errors properly.`
});

await runSubagent({
  agentName: 'ui-implementer',
  description: 'Build user form',
  prompt: `Build React components for user management using:
    - TypeScript for type safety
    - React Hooks for state
    - Tailwind CSS for styling
    - React Query for API calls
    
    Include error handling and loading states.`
});

await runSubagent({
  agentName: 'database-implementer',
  description: 'Create user schema',
  prompt: `Create PostgreSQL migrations using Prisma:
    - users table
    - indexes for email and created_at
    - proper constraints`
});
```

### Python + FastAPI + MongoDB

```javascript
await runSubagent({
  agentName: 'domain-implementer',
  description: 'Implement user API',
  prompt: `Implement user REST API using FastAPI:
    - MongoDB as database
    - Pydantic for validation
    - Async/await patterns
    
    TDD with pytest. Handle async operations properly.`
});

await runSubagent({
  agentName: 'database-implementer',
  description: 'Design MongoDB schema',
  prompt: `Design MongoDB collections for users:
    - users collection with proper indexes
    - profiles subcollection
    - audit log for changes`
});
```

### Go + Vue + MySQL

```javascript
await runSubagent({
  agentName: 'domain-implementer',
  description: 'Implement user API',
  prompt: `Implement user REST API using Go (Gin framework):
    - Clean architecture (handler, service, repository)
    - Interface-based design
    - Proper error handling
    
    TDD with testify. Follow Go best practices.`
});

await runSubagent({
  agentName: 'ui-implementer',
  description: 'Build user form',
  prompt: `Build Vue 3 components for user management:
    - Composition API for logic
    - Pinia for state management
    - Vite for build
    
    Include TypeScript and tests.`
});
```

## 🔍 Discovery Patterns

### Find Similar Code

```javascript
await runSubagent({
  agentName: 'explorer',
  description: 'Find similar APIs',
  prompt: `Find all similar CRUD API patterns in codebase:
    - Look for list, create, update, delete endpoints
    - Identify common patterns and inconsistencies
    - Find opportunities to standardize`
});
```

### Map Dependencies

```javascript
await runSubagent({
  agentName: 'explorer',
  description: 'Map dependencies',
  prompt: `Map all dependencies for the payment module:
    - What other modules depend on payment?
    - What does payment module depend on?
    - Identify circular dependencies`
});
```

### Find Test Gaps

```javascript
await runSubagent({
  agentName: 'explorer',
  description: 'Find untested code',
  prompt: `Discover all functions/classes without tests:
    - Critical business logic not tested
    - Error paths not covered
    - Integration points not tested`
});
```

## ✅ Code Review Workflows

### Pre-Merge Review

```javascript
await runSubagent({
  agentName: 'code-reviewer',
  description: 'Pre-merge review',
  prompt: `Review all changes in this PR for:
    - Correctness and logic
    - Test coverage >80%
    - Security issues (OWASP Top 10)
    - Performance regressions
    - Memory leaks
    - Proper error handling
    
    Provide APPROVED, NEEDS_REVISION, or FAILED`
});
```

### Security Audit

```javascript
await runSubagent({
  agentName: 'code-reviewer',
  description: 'Security audit',
  prompt: `Perform security audit of payment module:
    - SQL injection prevention
    - XSS protection
    - Authentication/authorization
    - Encryption (in-transit and at-rest)
    - Sensitive data handling
    - Secret management
    - Rate limiting on sensitive endpoints`
});
```

## 🏗️ Infrastructure Patterns

### Setup New Project

```javascript
await runSubagent({
  agentName: 'infra-implementer',
  description: 'Setup project infrastructure',
  prompt: `Create Docker setup for a Node.js + React + PostgreSQL project:
    - Node API container (Dockerfile)
    - React app container (Dockerfile)
    - PostgreSQL container config
    - docker-compose.yml with all services
    - Nginx reverse proxy
    - Environment configuration
    - Health checks for all services
    - Development and production variants`
});
```

### Deploy to Production

```javascript
await runSubagent({
  agentName: 'infra-implementer',
  description: 'Create production deployment',
  prompt: `Create production deployment configuration:
    - Kubernetes manifests or docker-compose for production
    - Load balancing strategy
    - Database backups
    - Monitoring and alerting
    - Zero-downtime deployment
    - Rollback procedure
    - Scaling strategy`
});
```

## 🎯 Best Practices

### 1. Always Start with Planning
```javascript
// Good: Plan first
await runSubagent({
  agentName: 'planner-architect',
  description: 'Plan payment integration',
  prompt: 'Plan payment integration with TDD approach'
});

// Bad: Skip planning
await runSubagent({
  agentName: 'domain-implementer',
  description: 'Implement payment',
  prompt: 'Add Stripe payment support'
});
```

### 2. parallelize Independent Work
```javascript
// Good: Parallel execution
await Promise.all([
  runSubagent({ ... API implementation ... }),
  runSubagent({ ... Database migration ... }),
  runSubagent({ ... UI components ... })
]);

// Bad: Sequential
await runSubagent({ ... API ... });
await runSubagent({ ... Database ... });
await runSubagent({ ... UI ... });
```

### 3. Always Review Before Deployment
```javascript
// Good: Review before deploy
await runSubagent({ agentName: 'code-reviewer', ... });
if (review.status === 'APPROVED') {
  await runSubagent({ agentName: 'infra-implementer', ... });
}

// Bad: Deploy without review
await runSubagent({ agentName: 'infra-implementer', ... });
```

### 4. Use Clear, Detailed Prompts
```javascript
// Good: Specific prompt
prompt: `Implement user registration with:
  - Email validation
  - Password strength requirements (min 12 chars, uppercase, number)
  - Email verification before activation
  - Rate limiting (max 5 attempts per hour)
  - Proper error responses`

// Bad: Vague prompt  
prompt: `Implement user registration`
```

## 📚 Reference

See individual agent documentation:
- [Orchestrator](agents/orchestrator.md)
- [Planner-Architect](agents/planner-architect.md)
- [Explorer](agents/explorer.md)
- [Domain-Implementer](agents/domain-implementer.md)
- [UI-Implementer](agents/ui-implementer.md)
- [Code-Reviewer](agents/code-reviewer.md)
- [Database-Implementer](agents/database-implementer.md)
- [Infra-Implementer](agents/infra-implementer.md)

---

**These agents work with any tech stack, framework, and type of software project. Adapt them to your specific needs!**
