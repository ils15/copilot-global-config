# Agent Skills

This directory contains custom Agent Skills for GitHub Copilot in VS Code. Agent Skills are an open standard that enable specialized capabilities and workflows.

## Overview

Agent Skills are folders of instructions, scripts, and resources that GitHub Copilot can load when relevant to perform specialized tasks. Unlike custom instructions that primarily define coding guidelines, skills enable specialized capabilities and workflows.

**Storage location**: `.github/skills/` (recommended) or `~/.github/skills/` for personal skills

## Available Skills

| Skill | Purpose |
|-------|---------|
| **api-design-patterns** | Design RESTful APIs with proper HTTP methods, status codes, pagination, filtering, error responses, and OpenAPI documentation |
| **code-review-checklist** | Systematic code review using quality gates, SOLID principles, error handling patterns, and test coverage analysis |
| **database-optimization** | Optimize SQL queries, analyze indexes, review Alembic migrations, and identify N+1 problems |
| **docker-best-practices** | Create optimized Dockerfiles with multi-stage builds, security hardening, layer caching, and health checks |
| **fastapi-async-patterns** | Create async FastAPI endpoints with proper error handling, dependency injection, service/repository patterns |
| **frontend-analyzer** | Analyze React/Next.js components to extract typography, colors, layout, fonts, spacing systems |
| **nextjs-seo-optimization** | Implement SEO best practices in Next.js applications with metadata, OG tags, schema markup |
| **playwright-e2e-testing** | Write end-to-end tests with Playwright for web applications with fixtures and page objects |
| **prompt-improver** | Improve prompts for AI agents using OpenAI's best practices |
| **security-audit** | Audit code for security vulnerabilities using OWASP Top 10 and STRIDE threat modeling |
| **telegram-bot-ui-design** | Design Telegram bot interfaces with keyboards, buttons, and conversational flows |
| **telegram-keyboard-design** | Design Telegram bot keyboards with inline keyboards, callbacks, and UX patterns |
| **web-ui-analysis** | Analyze web interfaces for UX issues, accessibility compliance, and Core Web Vitals |

## Skill Structure

Each skill follows this directory structure:

```
skills/
├── skill-name/
│   ├── SKILL.md                    # Main skill definition with YAML frontmatter
│   ├── templates/                  # Optional: template files
│   ├── examples/                   # Optional: example implementations
│   └── resources/                  # Optional: additional resources
└── README.md                       # This file
```

## SKILL.md Format

Each skill must have a `SKILL.md` file with YAML frontmatter:

```markdown
---
name: skill-name
description: Description of what the skill does and when to use it (max 1024 chars)
---

# Skill Title

Your detailed instructions, guidelines, and examples go here...
```

### YAML Frontmatter Fields

- **name** (required): Unique identifier, lowercase with hyphens, max 64 characters
- **description** (required): What the skill does and when to use it, max 1024 characters

### Naming Conventions

- Use lowercase letters, numbers, and hyphens only (no spaces or underscores)
- Examples: `web-testing`, `database-optimization`, `api-design-patterns`

## How Copilot Uses Skills

Skills use progressive disclosure to efficiently load content:

1. **Level 1 - Skill Discovery**: Copilot reads metadata (name and description) from YAML frontmatter
2. **Level 2 - Instructions Loading**: When relevant to your request, Copilot loads the SKILL.md body
3. **Level 3 - Resource Access**: Copilot can access additional files in the skill directory as needed

This ensures only relevant skills load, keeping context efficient.

## Creating a New Skill

1. Create a new directory: `skills/your-skill-name/`
2. Create `SKILL.md` with YAML frontmatter and detailed instructions
3. Optionally add supporting files (templates, examples, scripts)
4. Update this README with the new skill

### Best Practices

- Write clear, specific instructions
- Include examples of expected input and output
- Be explicit about when and how to use the skill
- Reference supporting files using relative paths: `[template](./template.js)`
- Keep descriptions concise and actionable
- Document dependencies and prerequisites

## Using Skills

Skills are automatically loaded by Copilot when relevant to your task. You can use skills in:

- **GitHub Copilot in VS Code**: Chat and agent mode
- **GitHub Copilot CLI**: Terminal commands
- **GitHub Copilot coding agent**: Automated coding tasks

No manual selection is needed—Copilot intelligently loads skills based on your request.

## External Resources

- [Agent Skills Documentation](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Agent Skills Standard (agentskills.io)](https://agentskills.io/)
- [GitHub Awesome Copilot](https://github.com/github/awesome-copilot) - Community skills
- [Anthropic Skills Reference](https://github.com/anthropics/skills) - Reference implementations

## References

- **Ofertasdachina Memory Bank**: `/docs/memory-bank/`
- **Copilot Instructions**: `/home/admin/.github/copilot-instructions.md`
- **Custom Instructions**: `.github/instructions/`
