# API Documentation - Omnify Blog Application

## Base URL
```
http://localhost:5000/api (Development)
https://your-domain.com/api (Production)
```

## Authentication

All protected endpoints require a JWT token in the Authorization header:
```
Authorization: Bearer <your-jwt-token>
```

## Endpoints

### Authentication

#### Register User
- **URL:** `POST /auth/register`
- **Description:** Create a new user account
- **Body:**
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "password123"
  }
  ```
- **Response:**
  ```json
  {
    "message": "User registered successfully",
    "token": "jwt-token-here",
    "user": {
      "id": "user-id",
      "name": "John Doe",
      "email": "john@example.com",
      "avatar": ""
    }
  }
  ```

#### Login User
- **URL:** `POST /auth/login`
- **Description:** Authenticate user and get JWT token
- **Body:**
  ```json
  {
    "email": "john@example.com",
    "password": "password123"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Login successful",
    "token": "jwt-token-here",
    "user": {
      "id": "user-id",
      "name": "John Doe",
      "email": "john@example.com",
      "avatar": ""
    }
  }
  ```

#### Get Current User
- **URL:** `GET /auth/me`
- **Description:** Get current authenticated user information
- **Headers:** `Authorization: Bearer <token>`
- **Response:**
  ```json
  {
    "user": {
      "id": "user-id",
      "name": "John Doe",
      "email": "john@example.com",
      "avatar": ""
    }
  }
  ```

### Blogs

#### Get All Blogs
- **URL:** `GET /blogs`
- **Description:** Get paginated list of all published blogs
- **Query Parameters:**
  - `page` (optional): Page number (default: 1)
  - `limit` (optional): Items per page (default: 10)
  - `search` (optional): Search term for title/content
  - `tag` (optional): Filter by tag
- **Response:**
  ```json
  {
    "blogs": [
      {
        "_id": "blog-id",
        "title": "Blog Title",
        "content": "Blog content...",
        "excerpt": "Blog excerpt...",
        "author": {
          "_id": "user-id",
          "name": "John Doe",
          "avatar": ""
        },
        "tags": ["technology", "programming"],
        "featuredImage": "https://example.com/image.jpg",
        "readTime": 5,
        "status": "published",
        "createdAt": "2024-01-01T00:00:00.000Z",
        "updatedAt": "2024-01-01T00:00:00.000Z"
      }
    ],
    "pagination": {
      "currentPage": 1,
      "totalPages": 5,
      "totalBlogs": 50,
      "hasNextPage": true,
      "hasPrevPage": false
    }
  }
  ```

#### Get Single Blog
- **URL:** `GET /blogs/:id`
- **Description:** Get a specific blog by ID
- **Response:**
  ```json
  {
    "blog": {
      "_id": "blog-id",
      "title": "Blog Title",
      "content": "Blog content...",
      "excerpt": "Blog excerpt...",
      "author": {
        "_id": "user-id",
        "name": "John Doe",
        "avatar": ""
      },
      "tags": ["technology", "programming"],
      "featuredImage": "https://example.com/image.jpg",
      "readTime": 5,
      "status": "published",
      "createdAt": "2024-01-01T00:00:00.000Z",
      "updatedAt": "2024-01-01T00:00:00.000Z"
    }
  }
  ```

#### Create Blog
- **URL:** `POST /blogs`
- **Description:** Create a new blog post (requires authentication)
- **Headers:** `Authorization: Bearer <token>`
- **Body:**
  ```json
  {
    "title": "Blog Title",
    "content": "Blog content...",
    "excerpt": "Blog excerpt...",
    "tags": "technology, programming, web development",
    "featuredImage": "https://example.com/image.jpg"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Blog created successfully",
    "blog": {
      "_id": "blog-id",
      "title": "Blog Title",
      "content": "Blog content...",
      "excerpt": "Blog excerpt...",
      "author": {
        "_id": "user-id",
        "name": "John Doe",
        "avatar": ""
      },
      "tags": ["technology", "programming", "web development"],
      "featuredImage": "https://example.com/image.jpg",
      "readTime": 5,
      "status": "published",
      "createdAt": "2024-01-01T00:00:00.000Z",
      "updatedAt": "2024-01-01T00:00:00.000Z"
    }
  }
  ```

#### Update Blog
- **URL:** `PUT /blogs/:id`
- **Description:** Update an existing blog post (requires authentication, author only)
- **Headers:** `Authorization: Bearer <token>`
- **Body:**
  ```json
  {
    "title": "Updated Blog Title",
    "content": "Updated blog content...",
    "excerpt": "Updated blog excerpt...",
    "tags": "technology, programming, updated",
    "featuredImage": "https://example.com/updated-image.jpg"
  }
  ```
- **Response:**
  ```json
  {
    "message": "Blog updated successfully",
    "blog": {
      "_id": "blog-id",
      "title": "Updated Blog Title",
      "content": "Updated blog content...",
      "excerpt": "Updated blog excerpt...",
      "author": {
        "_id": "user-id",
        "name": "John Doe",
        "avatar": ""
      },
      "tags": ["technology", "programming", "updated"],
      "featuredImage": "https://example.com/updated-image.jpg",
      "readTime": 5,
      "status": "published",
      "createdAt": "2024-01-01T00:00:00.000Z",
      "updatedAt": "2024-01-01T00:00:00.000Z"
    }
  }
  ```

#### Delete Blog
- **URL:** `DELETE /blogs/:id`
- **Description:** Delete a blog post (requires authentication, author only)
- **Headers:** `Authorization: Bearer <token>`
- **Response:**
  ```json
  {
    "message": "Blog deleted successfully"
  }
  ```

#### Get User's Blogs
- **URL:** `GET /blogs/user/my-blogs`
- **Description:** Get all blogs by the authenticated user
- **Headers:** `Authorization: Bearer <token>`
- **Response:**
  ```json
  {
    "blogs": [
      {
        "_id": "blog-id",
        "title": "Blog Title",
        "content": "Blog content...",
        "excerpt": "Blog excerpt...",
        "author": {
          "_id": "user-id",
          "name": "John Doe",
          "avatar": ""
        },
        "tags": ["technology", "programming"],
        "featuredImage": "https://example.com/image.jpg",
        "readTime": 5,
        "status": "published",
        "createdAt": "2024-01-01T00:00:00.000Z",
        "updatedAt": "2024-01-01T00:00:00.000Z"
      }
    ]
  }
  ```

## Error Responses

### Validation Errors
```json
{
  "message": "Validation failed",
  "errors": [
    {
      "field": "email",
      "message": "Please enter a valid email"
    }
  ]
}
```

### Authentication Errors
```json
{
  "message": "Access denied. No token provided."
}
```

### Authorization Errors
```json
{
  "message": "Not authorized to update this blog"
}
```

### Not Found Errors
```json
{
  "message": "Blog not found"
}
```

### Server Errors
```json
{
  "message": "Server error"
}
```

## Data Models

### User Model
```javascript
{
  _id: ObjectId,
  name: String (required, 2-50 chars),
  email: String (required, unique, lowercase),
  password: String (required, min 6 chars, hashed),
  avatar: String (optional),
  createdAt: Date,
  updatedAt: Date
}
```

### Blog Model
```javascript
{
  _id: ObjectId,
  title: String (required, 3-200 chars),
  content: String (required, min 10 chars),
  excerpt: String (optional, max 300 chars),
  author: ObjectId (ref: User, required),
  tags: [String],
  featuredImage: String (optional, URL),
  status: String (enum: ['draft', 'published'], default: 'published'),
  readTime: Number (calculated),
  createdAt: Date,
  updatedAt: Date
}
```

## Rate Limiting

Currently, no rate limiting is implemented. Consider implementing rate limiting for production use.

## CORS Configuration

The API is configured to accept requests from:
- Development: `http://localhost:3000`
- Production: Configure based on your frontend domain

## Security Features

1. **Password Hashing:** Passwords are hashed using bcrypt
2. **JWT Authentication:** Secure token-based authentication
3. **Input Validation:** All inputs are validated using express-validator
4. **CORS Protection:** Cross-origin requests are properly configured
5. **Helmet Security:** Security headers are set using helmet

## Testing the API

### Using cURL

#### Register a user:
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "password123"
  }'
```

#### Login:
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "password123"
  }'
```

#### Create a blog (with token):
```bash
curl -X POST http://localhost:5000/api/blogs \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "title": "My First Blog",
    "content": "This is my first blog post content...",
    "tags": "technology, programming"
  }'
```

### Using Postman

1. Import the API endpoints into Postman
2. Set up environment variables for the base URL and token
3. Test all endpoints with proper authentication

## WebSocket Support

Currently, the API does not support WebSocket connections. Real-time features would require additional implementation.

## File Upload

Currently, the API does not support file uploads. Images are stored as URLs. Consider implementing file upload functionality for production use.

## Pagination

Blog listing supports pagination with the following parameters:
- `page`: Page number (default: 1)
- `limit`: Items per page (default: 10, max: 50)

## Search Functionality

Blog search supports:
- Full-text search in title and content
- Tag-based filtering
- Case-insensitive matching

## Performance Considerations

1. **Database Indexing:** Text indexes are created for search functionality
2. **Pagination:** Large datasets are paginated to improve performance
3. **Selective Population:** Only necessary fields are populated from related documents
4. **Caching:** Consider implementing Redis caching for production

## Monitoring

Consider implementing:
1. Request logging with Morgan
2. Error tracking with Sentry
3. Performance monitoring
4. Health check endpoints 