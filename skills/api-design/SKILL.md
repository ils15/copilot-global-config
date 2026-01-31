---
name: api-design
description: "RESTful API design patterns - HTTP methods, status codes, pagination, filtering, error responses"
---

# API Design Skill

## HTTP Methods & Status Codes

### GET - Retrieve Data
```python
@router.get("/users")
async def list_users(
    skip: int = 0,
    limit: int = 100,
    sort: str = "created_at"
):
    """List users with pagination & filtering"""
    return {"status": 200, "data": users}

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    """Get specific user"""
    return {"status": 200, "data": user}
```
Status: 200 OK | 404 Not Found

### POST - Create Data
```python
@router.post("/users", status_code=201)
async def create_user(data: UserCreate):
    """Create new user"""
    return {"status": 201, "data": user}
```
Status: 201 Created | 400 Bad Request | 409 Conflict

### PATCH - Update Data
```python
@router.patch("/users/{user_id}")
async def update_user(user_id: int, data: UserUpdate):
    """Update partial user data"""
    return {"status": 200, "data": updated_user}
```
Status: 200 OK | 400 Bad Request | 404 Not Found

### DELETE - Remove Data
```python
@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    """Delete user"""
    return {"status": 204}
```
Status: 204 No Content | 404 Not Found

## Pagination Pattern
```python
class PaginationParams(BaseModel):
    skip: int = 0
    limit: int = 100
    
    @validator('limit')
    def limit_max(cls, v):
        return min(v, 1000)

@router.get("/users")
async def list_users(params: PaginationParams):
    items = await db.query(User).offset(params.skip).limit(params.limit)
    total = await db.query(User).count()
    return {
        "data": items,
        "pagination": {
            "total": total,
            "skip": params.skip,
            "limit": params.limit
        }
    }
```

## Error Response Format
```python
class ErrorResponse(BaseModel):
    error: str
    code: str
    details: Optional[Dict] = None

# Usage
raise HTTPException(
    status_code=400,
    detail={
        "error": "Validation failed",
        "code": "INVALID_EMAIL",
        "details": {"field": "email"}
    }
)
```

## Success Response Format
```python
class SuccessResponse(BaseModel):
    status: int
    data: Any
    meta: Optional[Dict] = None
```

## Versioning
Use URL versioning:
- `/api/v1/users` - Version 1
- `/api/v2/users` - Version 2 (new)

Support both during transition!

## Documentation
Use OpenAPI/Swagger:
```python
@router.get(
    "/users",
    summary="List all users",
    description="Returns paginated list of users with filtering",
    responses={200: {"model": ListUsersResponse}}
)
async def list_users(...):
```
