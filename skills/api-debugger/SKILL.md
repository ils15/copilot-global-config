---
name: api-debugger
description: Debug REST APIs systematically by analyzing requests, responses, headers, status codes, and payloads. Provides structured troubleshooting for common API issues like 400, 401, 403, 404, 500 errors.
---

# API Debugger

Debug REST API issues systematically using a structured approach.

## What This Skill Does

Helps diagnose and fix common API problems:
- HTTP status code interpretation
- Request/response analysis
- Header debugging (auth, content-type, CORS)
- Payload validation
- Network and timeout issues
- Authentication/authorization problems

## When to Use This Skill

- API returning unexpected status codes
- Request/response debugging needed
- CORS or authentication issues
- Payload format problems
- Timeout or network errors
- Integration testing failures

## Debugging Framework

### 1. Gather Context
- What's the API endpoint?
- What HTTP method? (GET, POST, PUT, DELETE, PATCH)
- What's the expected behavior?
- What's the actual behavior/error?
- Full request details (URL, headers, body)
- Full response details (status, headers, body)

### 2. Analyze Status Code

**2xx Success**
- 200 OK - Request succeeded
- 201 Created - Resource created successfully
- 204 No Content - Success but no response body

**4xx Client Errors**
- 400 Bad Request - Invalid request format/validation
- 401 Unauthorized - Missing or invalid auth token
- 403 Forbidden - Valid auth but no permission
- 404 Not Found - Endpoint or resource doesn't exist
- 422 Unprocessable Entity - Validation errors

**5xx Server Errors**
- 500 Internal Server Error - Server-side exception
- 502 Bad Gateway - Upstream server error
- 503 Service Unavailable - Server overloaded/down
- 504 Gateway Timeout - Upstream server timeout

### 3. Check Common Issues

#### Authentication Issues
```bash
# Missing token
curl -X GET https://api.example.com/protected
# 401 Unauthorized

# Fix: Add Authorization header
curl -X GET https://api.example.com/protected \
  -H "Authorization: Bearer YOUR_TOKEN"
```

#### Content-Type Issues
```bash
# Wrong content-type
curl -X POST https://api.example.com/data \
  -d '{"name": "test"}'
# 415 Unsupported Media Type

# Fix: Add Content-Type header
curl -X POST https://api.example.com/data \
  -H "Content-Type: application/json" \
  -d '{"name": "test"}'
```

#### CORS Issues
```bash
# Check CORS headers in response
curl -I https://api.example.com/endpoint
# Look for: Access-Control-Allow-Origin

# If missing, server needs to add CORS headers
```

#### Validation Errors
```bash
# Check response body for validation details
curl -X POST https://api.example.com/users \
  -H "Content-Type: application/json" \
  -d '{"email": "invalid-email"}'

# Response might include:
# {"error": "Invalid email format", "field": "email"}
```

### 4. Systematic Debugging Steps

1. **Verify Endpoint URL** - Is it correct? Check for typos
2. **Check HTTP Method** - GET, POST, PUT, DELETE match the API spec?
3. **Validate Headers** - Content-Type, Authorization, Accept
4. **Inspect Request Body** - Valid JSON? Required fields present?
5. **Check Response Body** - Error messages? Validation details?
6. **Review Server Logs** - What does the backend say?
7. **Test with curl/Postman** - Isolate the issue from code
8. **Compare Working Example** - What's different?

## Debugging Checklist

```markdown
- [ ] Endpoint URL is correct (no typos)
- [ ] HTTP method matches API specification
- [ ] Authorization header present and valid
- [ ] Content-Type header set correctly
- [ ] Request body is valid JSON (if POST/PUT/PATCH)
- [ ] Required fields are present in request
- [ ] Field types match API expectations
- [ ] Response body examined for error details
- [ ] Server logs checked for exceptions
- [ ] Network connectivity verified
- [ ] Firewall/proxy not blocking request
- [ ] API rate limits not exceeded
```

## Common Patterns

### Pattern 1: 401 Unauthorized

**Problem**: Token missing or expired

**Debug**:
```bash
# Check if token is present
echo $AUTH_TOKEN

# Check token expiration (JWT)
echo $AUTH_TOKEN | cut -d'.' -f2 | base64 -d | jq .exp

# Compare with current time
date +%s
```

**Fix**:
- Generate new token
- Add to Authorization header
- Verify token format (Bearer vs Basic)

### Pattern 2: 422 Validation Error

**Problem**: Request data doesn't match schema

**Debug**:
```bash
# Get detailed error response
curl -v -X POST https://api.example.com/endpoint \
  -H "Content-Type: application/json" \
  -d @request.json | jq .

# Response shows which field failed:
# {"detail": [{"loc": ["body", "email"], "msg": "invalid email"}]}
```

**Fix**:
- Check API documentation for required fields
- Validate field types (string vs number vs boolean)
- Check field constraints (min/max length, enum values)

### Pattern 3: 500 Internal Server Error

**Problem**: Server-side exception

**Debug**:
1. Check server logs for stack trace
2. Check database connectivity
3. Check external service dependencies
4. Verify environment variables loaded
5. Check for recent code changes

**Fix**:
- Fix exception in server code
- Handle edge cases
- Add error logging
- Deploy fix and test

### Pattern 4: CORS Error (Browser Only)

**Problem**: `Access-Control-Allow-Origin` header missing

**Debug**:
```bash
# Check preflight response
curl -X OPTIONS https://api.example.com/endpoint \
  -H "Origin: https://yourapp.com" \
  -H "Access-Control-Request-Method: POST" \
  -I
```

**Fix** (server-side):
```python
# FastAPI example
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourapp.com"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Tools for Debugging

### curl (Command Line)
```bash
# Verbose output
curl -v https://api.example.com/endpoint

# Include response headers
curl -i https://api.example.com/endpoint

# Follow redirects
curl -L https://api.example.com/endpoint

# Save response to file
curl https://api.example.com/endpoint -o response.json

# POST with JSON
curl -X POST https://api.example.com/endpoint \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'

# With authentication
curl https://api.example.com/endpoint \
  -H "Authorization: Bearer TOKEN"
```

### jq (JSON Processing)
```bash
# Pretty print response
curl https://api.example.com/data | jq .

# Extract specific field
curl https://api.example.com/data | jq '.items[0].name'

# Filter array
curl https://api.example.com/data | jq '.items[] | select(.active == true)'
```

### httpie (User-Friendly curl Alternative)
```bash
# Simple GET
http https://api.example.com/endpoint

# POST with JSON
http POST https://api.example.com/endpoint name=test email=test@example.com

# With auth
http https://api.example.com/endpoint Authorization:"Bearer TOKEN"
```

## Example: Complete Debug Session

**Problem**: POST /api/users returns 422

**Step 1: Reproduce**
```bash
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "email": "john@example"}'

# Response:
# {"detail": [{"loc": ["body", "email"], "msg": "value is not a valid email"}]}
```

**Step 2: Identify Issue**
- Status code: 422 (validation error)
- Field: `email`
- Issue: Invalid email format

**Step 3: Fix Request**
```bash
curl -X POST http://localhost:8000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "email": "john@example.com"}'

# Response:
# {"id": 1, "name": "John", "email": "john@example.com"}
```

**Step 4: Verify**
```bash
# Check user was created
curl http://localhost:8000/api/users/1

# Response:
# {"id": 1, "name": "John", "email": "john@example.com"}
```

## Guidelines

- Start with simplest test (curl/httpie)
- Check server logs for exceptions
- Verify all headers are present
- Validate request body format
- Compare with working examples
- Isolate issue step-by-step
- Document findings for future reference

## Anti-Patterns to Avoid

❌ Guessing without checking logs
❌ Assuming client code is correct
❌ Not reading error messages carefully
❌ Skipping validation of request format
❌ Not testing with simple curl first
❌ Ignoring HTTP status codes
❌ Not checking API documentation

## Reference

- HTTP Status Codes: https://httpstatuses.com/
- curl Manual: https://curl.se/docs/manual.html
- REST API Best Practices: https://restfulapi.net/
