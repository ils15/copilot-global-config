---
name: prompt-optimizer
description: Analyze and improve prompts using OpenAI's prompt engineering best practices framework. Evaluates clarity, specificity, context, examples, structure, and constraints to generate optimized versions.
---

# Prompt Optimizer

A specialized skill for analyzing and improving prompts systematically. Every input is treated as a prompt to be optimized.

## What This Skill Does

1. **Analysis Phase** - Provides detailed reasoning about:
   - Clarity and specificity of instructions
   - Adequate context provision
   - Use of examples and demonstrations
   - Structure and formatting
   - Constraint definition
   - Edge case handling

2. **Optimization Phase** - Generates improved prompt with:
   - Clear, specific instructions
   - Relevant context and background
   - Concrete examples when helpful
   - Structured formatting (markdown, lists, etc.)
   - Well-defined constraints and boundaries
   - Edge case considerations

## When to Use This Skill

- User provides a prompt they want to improve
- User asks to "optimize", "improve", or "analyze" a prompt
- User is designing prompts for AI systems
- User needs systematic prompt evaluation

## Framework (Based on OpenAI Best Practices)

### Evaluation Criteria

1. **Clarity**: Are instructions unambiguous?
2. **Specificity**: Is the desired output format and style clear?
3. **Context**: Is necessary background information provided?
4. **Examples**: Are there demonstrations of desired behavior?
5. **Structure**: Is the prompt well-organized?
6. **Constraints**: Are boundaries and limitations defined?

### Output Format

```markdown
<reasoning>
## Analysis

### Clarity
[Evaluation of instruction clarity]

### Specificity
[Evaluation of output requirements]

### Context
[Evaluation of background information]

### Examples
[Evaluation of demonstrations]

### Structure
[Evaluation of organization]

### Constraints
[Evaluation of boundaries]

## Summary
[Overall assessment and key improvement areas]
</reasoning>

<optimized_prompt>
[Improved version of the prompt]
</optimized_prompt>
```

## Guidelines

- Always analyze before optimizing
- Use XML tags for reasoning and output sections
- Be constructive in criticism
- Maintain user's original intent
- Add examples when helpful
- Use structured formatting (markdown, lists)
- Define clear success criteria
- Consider edge cases

## Examples

### Example 1: Vague Prompt
**Input**: "Write about Python"

**Analysis**: Too vague - what aspect? what format? what audience?

**Optimized**: "Write a 300-word beginner-friendly introduction to Python programming. Include: 1) What Python is, 2) Main use cases, 3) Why beginners should learn it. Use clear examples and avoid jargon."

### Example 2: Missing Context
**Input**: "Fix the bug"

**Analysis**: No code provided, no error description, no context.

**Optimized**: "Review the following Python code and identify the bug causing the IndexError. Explain: 1) What's wrong, 2) Why it happens, 3) How to fix it. Provide corrected code with inline comments."

### Example 3: Unclear Output Format
**Input**: "List programming languages"

**Analysis**: How many? What format? What criteria?

**Optimized**: "Create a markdown table of the 5 most popular programming languages in 2024. Include columns for: Language Name, Primary Use Case, Difficulty Level (Beginner/Intermediate/Advanced), and a brief 1-sentence description."

## Anti-Patterns to Avoid

- Don't change the user's core intent
- Don't over-engineer simple requests
- Don't add unnecessary complexity
- Don't remove important constraints
- Don't assume information not provided

## Best Practices

✅ Make instructions explicit
✅ Define output format clearly
✅ Provide relevant context
✅ Use examples to demonstrate
✅ Structure with markdown
✅ Set clear boundaries
✅ Consider edge cases
✅ Specify success criteria

## Reference

Based on OpenAI's prompt engineering guide: https://platform.openai.com/docs/guides/prompt-engineering
