---
description: "Frontend development standards for React/TypeScript"
name: "Frontend Development Standards"
applyTo: "**/*.{tsx,jsx}"
---

# Frontend Development Standards (Afrodite)

## TypeScript
- Strict mode Always (no `any` types)
- Props interfaces em todos componentes
- Return type annotations em todas funções

## Components
- Single Responsibility Principle
- Reusable e composable
- Max 300 linhas por componente
- Atomic Design pattern

## Accessibility
- ARIA labels em interactive elements
- Keyboard navigation
- Color contrast WCAG AA
- Semantic HTML

## Responsive Design
- Mobile-first approach
- Breakpoints: 640px, 768px, 1024px, 1280px
- Test em múltiplos devices

## State Management
- Hooks (useState, useContext, useReducer)
- Centralized state para app-wide data
- Local state para component-specific

## Testing
- React Testing Library (não snapshot testing)
- Test behavior não implementation
- >80% coverage
- Test user workflows

## Styling
- Tailwind CSS + custom CSS quando necessário
- Design tokens para cores/spacing
- Responsive classes
- No inline styles
