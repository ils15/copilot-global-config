---
name: web-e2e-tester
description: Design and execute end-to-end web application tests using Playwright. Creates comprehensive test scenarios covering user flows, edge cases, and error handling with best practices for reliability and maintainability.
---

# Web E2E Tester

A specialized skill for designing and executing end-to-end tests for web applications using Playwright.

## What This Skill Does

1. **Test Planning** - Analyzes requirements and creates test scenarios
2. **Test Implementation** - Writes Playwright tests following best practices
3. **Test Execution** - Runs tests and analyzes results
4. **Test Maintenance** - Suggests improvements and refactoring

## When to Use This Skill

- User wants to test a web application
- User needs to create E2E test scenarios
- User asks to verify user flows
- User wants to automate browser testing
- User mentions Playwright or E2E testing

## Core Capabilities

### Test Scenarios

- **Happy Path**: Main user journey with valid inputs
- **Edge Cases**: Boundary conditions, empty states, limits
- **Error Handling**: Invalid inputs, network failures, timeouts
- **Permissions**: Authenticated vs unauthenticated flows
- **Responsiveness**: Mobile, tablet, desktop viewports
- **Accessibility**: Keyboard navigation, ARIA labels

### Playwright Best Practices

1. **Locator Strategy**
   - Prefer user-facing attributes (role, label, text)
   - Use `page.getByRole()`, `page.getByLabel()`, `page.getByText()`
   - Avoid brittle CSS selectors or XPath
   - Use `data-testid` only as last resort

2. **Async/Await**
   - Always `await` Playwright actions
   - Use `waitForSelector()` for dynamic content
   - Handle network requests with `waitForResponse()`

3. **Assertions**
   - Use `expect(locator).toBeVisible()`
   - Use `expect(locator).toHaveText()`
   - Use `expect(page).toHaveURL()`
   - Add meaningful assertion messages

4. **Test Independence**
   - Each test should be isolated
   - Clean up state after tests
   - Don't rely on test execution order
   - Use `beforeEach`/`afterEach` hooks

5. **Page Object Model**
   - Encapsulate page interactions
   - Reuse common actions
   - Maintain single source of truth

## Test Structure Template

```typescript
import { test, expect } from '@playwright/test';

test.describe('Feature Name', () => {
  test.beforeEach(async ({ page }) => {
    // Setup: Navigate, login, etc
    await page.goto('/feature');
  });

  test('should handle happy path', async ({ page }) => {
    // Arrange: Setup test data
    
    // Act: Perform user action
    await page.getByRole('button', { name: 'Submit' }).click();
    
    // Assert: Verify expected outcome
    await expect(page.getByText('Success!')).toBeVisible();
  });

  test('should handle invalid input', async ({ page }) => {
    // Act: Submit invalid data
    await page.getByLabel('Email').fill('invalid-email');
    await page.getByRole('button', { name: 'Submit' }).click();
    
    // Assert: Error message shown
    await expect(page.getByText('Invalid email')).toBeVisible();
  });

  test('should handle network error', async ({ page }) => {
    // Arrange: Mock network failure
    await page.route('**/api/submit', route => route.abort());
    
    // Act: Attempt submission
    await page.getByRole('button', { name: 'Submit' }).click();
    
    // Assert: Error handling
    await expect(page.getByText('Network error')).toBeVisible();
  });
});
```

## Common Test Scenarios

### 1. Form Submission
```typescript
test('should submit form with valid data', async ({ page }) => {
  await page.getByLabel('Name').fill('John Doe');
  await page.getByLabel('Email').fill('john@example.com');
  await page.getByRole('button', { name: 'Submit' }).click();
  
  await expect(page.getByText('Form submitted')).toBeVisible();
});
```

### 2. Navigation
```typescript
test('should navigate to details page', async ({ page }) => {
  await page.getByRole('link', { name: 'View Details' }).click();
  
  await expect(page).toHaveURL(/\/details\/\d+/);
  await expect(page.getByRole('heading')).toBeVisible();
});
```

### 3. Authentication
```typescript
test('should login successfully', async ({ page }) => {
  await page.goto('/login');
  await page.getByLabel('Username').fill('testuser');
  await page.getByLabel('Password').fill('password123');
  await page.getByRole('button', { name: 'Login' }).click();
  
  await expect(page).toHaveURL('/dashboard');
  await expect(page.getByText('Welcome, testuser')).toBeVisible();
});
```

### 4. API Interaction
```typescript
test('should load data from API', async ({ page }) => {
  const responsePromise = page.waitForResponse('**/api/data');
  await page.goto('/data-page');
  
  const response = await responsePromise;
  expect(response.status()).toBe(200);
  
  await expect(page.getByRole('table')).toBeVisible();
});
```

### 5. Dynamic Content
```typescript
test('should handle loading states', async ({ page }) => {
  await page.goto('/async-page');
  
  // Loading state
  await expect(page.getByText('Loading...')).toBeVisible();
  
  // Content loaded
  await expect(page.getByRole('article')).toBeVisible();
  await expect(page.getByText('Loading...')).not.toBeVisible();
});
```

## Debugging Tips

1. **Screenshots**: `await page.screenshot({ path: 'debug.png' })`
2. **Video**: Enable in config `use: { video: 'on' }`
3. **Trace**: `await page.context().tracing.start()`
4. **Slow Mo**: `use: { launchOptions: { slowMo: 1000 } }`
5. **Headed Mode**: `npx playwright test --headed`

## Configuration Best Practices

```typescript
// playwright.config.ts
export default {
  testDir: './tests',
  timeout: 30000,
  retries: 2,
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit', use: { ...devices['Desktop Safari'] } },
    { name: 'mobile', use: { ...devices['iPhone 13'] } },
  ],
};
```

## Guidelines

- Write clear, descriptive test names
- Follow Arrange-Act-Assert pattern
- Test user behavior, not implementation
- Keep tests focused and atomic
- Use meaningful assertion messages
- Clean up test data
- Handle async operations properly
- Test across multiple browsers/devices
- Mock external dependencies
- Document complex test scenarios

## Anti-Patterns to Avoid

❌ Testing implementation details
❌ Tests depending on each other
❌ Hardcoding wait times (`page.waitForTimeout()`)
❌ Overly complex test setup
❌ Testing third-party libraries
❌ Brittle selectors (CSS classes, XPath)
❌ Not handling async properly
❌ Ignoring accessibility

## Example: Complete Test Suite

```typescript
import { test, expect } from '@playwright/test';

test.describe('Product Catalog', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/products');
  });

  test('should display product list', async ({ page }) => {
    await expect(page.getByRole('heading', { name: 'Products' })).toBeVisible();
    await expect(page.getByRole('article')).toHaveCount(10);
  });

  test('should filter by category', async ({ page }) => {
    await page.getByLabel('Category').selectOption('Electronics');
    
    await page.waitForResponse('**/api/products?category=Electronics');
    await expect(page.getByRole('article')).toHaveCount(5);
  });

  test('should search products', async ({ page }) => {
    await page.getByPlaceholder('Search...').fill('laptop');
    await page.getByRole('button', { name: 'Search' }).click();
    
    await expect(page).toHaveURL(/search=laptop/);
    await expect(page.getByText(/laptop/i)).toBeVisible();
  });

  test('should add to cart', async ({ page }) => {
    await page.getByRole('button', { name: 'Add to Cart' }).first().click();
    
    await expect(page.getByText('Added to cart')).toBeVisible();
    await expect(page.getByRole('link', { name: /Cart \(1\)/ })).toBeVisible();
  });

  test('should handle out of stock', async ({ page }) => {
    await page.route('**/api/cart/add', route => 
      route.fulfill({ status: 400, body: 'Out of stock' })
    );
    
    await page.getByRole('button', { name: 'Add to Cart' }).first().click();
    await expect(page.getByText('Out of stock')).toBeVisible();
  });
});
```

## Reference

- Playwright Documentation: https://playwright.dev/
- Best Practices: https://playwright.dev/docs/best-practices
- Locators Guide: https://playwright.dev/docs/locators
