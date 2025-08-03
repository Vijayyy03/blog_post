# Omnify Blog Application - Django Backend

A modern blog application built with Django REST Framework (DRF) and PostgreSQL, featuring user authentication, blog CRUD operations, comments, and a robust API.

## 🚀 Features

### Authentication & User Management
- **JWT Authentication**: Secure token-based authentication
- **User Registration & Login**: Email-based user accounts
- **Profile Management**: User profiles with avatars and social links
- **Password Management**: Secure password change functionality

### Blog Management
- **Rich Blog Posts**: Support for markdown content, featured images, and excerpts
- **Categories & Tags**: Organized content with categories and tags
- **Author Permissions**: Only authors can edit/delete their own posts
- **Draft System**: Save posts as drafts before publishing
- **SEO Optimization**: Meta titles and descriptions for better search visibility

### Advanced Features
- **Comments System**: Nested comments with approval system
- **Analytics**: View and like tracking for blog posts
- **Search & Filtering**: Advanced search with multiple filters
- **Pagination**: Efficient pagination for large datasets
- **Reading Time**: Automatic calculation of reading time

## 🛠 Tech Stack

### Backend
- **Django 4.2.7**: Web framework
- **Django REST Framework 3.14.0**: API framework
- **PostgreSQL**: Primary database
- **JWT Authentication**: Secure token-based auth
- **Django CORS Headers**: Cross-origin resource sharing
- **Pillow**: Image processing
- **Markdown**: Content formatting

### Frontend (React)
- **React 18**: Frontend framework
- **Tailwind CSS**: Styling
- **React Router**: Navigation
- **Axios**: HTTP client
- **React Hook Form**: Form handling
- **React Hot Toast**: Notifications

## 📋 Prerequisites

- Python 3.8+
- PostgreSQL 12+
- Node.js 16+ (for frontend)
- npm or yarn

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Omnify
```

### 2. Backend Setup

#### Install Python Dependencies
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Database Setup
1. **Install PostgreSQL** and create a database:
```sql
CREATE DATABASE omnify_blog;
CREATE USER omnify_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE omnify_blog TO omnify_user;
```

2. **Configure Environment Variables**:
Create a `.env` file in the `backend` directory:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings
DB_NAME=omnify_blog
DB_USER=omnify_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# JWT Settings
JWT_SECRET_KEY=your-jwt-secret-key-here

# CORS Settings
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

#### Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Create Superuser
```bash
python manage.py createsuperuser
```

#### Run the Development Server
```bash
python manage.py runserver
```

The backend will be available at `http://localhost:8000`

### 3. Frontend Setup

#### Install Dependencies
```bash
cd client
npm install
```

#### Configure Environment Variables
Create a `.env` file in the `client` directory:
```env
REACT_APP_API_URL=http://localhost:8000/api
```

#### Start the Development Server
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## 📚 API Documentation

### Base URL
```
http://localhost:8000/api
```

### Authentication Endpoints

#### Register User
```http
POST /auth/register
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123",
  "password2": "password123"
}
```

#### Login User
```http
POST /auth/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "password123"
}
```

#### Get Current User
```http
GET /auth/me
Authorization: Bearer <token>
```

### Blog Endpoints

#### List All Blogs
```http
GET /blogs/
```

**Query Parameters:**
- `page`: Page number (default: 1)
- `search`: Search term
- `tag`: Filter by tag
- `category`: Filter by category
- `author`: Filter by author ID

#### Get Single Blog
```http
GET /blogs/{slug}/
```

#### Create Blog
```http
POST /blogs/create/
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "My Blog Post",
  "content": "Blog content here...",
  "excerpt": "Brief summary",
  "featured_image": "https://example.com/image.jpg",
  "tags": ["technology", "programming"],
  "status": "published"
}
```

#### Update Blog
```http
PUT /blogs/{slug}/update/
Authorization: Bearer <token>
Content-Type: application/json

{
  "title": "Updated Title",
  "content": "Updated content..."
}
```

#### Delete Blog
```http
DELETE /blogs/{slug}/delete/
Authorization: Bearer <token>
```

#### User's Blogs
```http
GET /blogs/my-blogs/
Authorization: Bearer <token>
```

### Comment Endpoints

#### List Comments
```http
GET /blogs/{slug}/comments/
```

#### Create Comment
```http
POST /blogs/{slug}/comments/create/
Authorization: Bearer <token>
Content-Type: application/json

{
  "content": "Great post!",
  "parent": null
}
```

### Special Endpoints

#### Featured Blogs
```http
GET /blogs/featured/
```

#### Popular Blogs
```http
GET /blogs/popular/
```

#### Like Blog
```http
POST /blogs/{slug}/like/
Authorization: Bearer <token>
```

## 🗄 Database Schema

### User Model
```python
class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')
    bio = models.TextField(max_length=500, blank=True)
    website = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
```

### Blog Model
```python
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.TextField(max_length=500, blank=True)
    featured_image = models.ImageField(upload_to='blog_images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(choices=STATUS_CHOICES, default='published')
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
```

### Comment Model
```python
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True)
    content = models.TextField()
    is_approved = models.BooleanField(default=True)
```

## 🔧 Configuration

### Django Settings
Key settings in `blog_project/settings.py`:

```python
# Custom User Model
AUTH_USER_MODEL = 'users.User'

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
}
```

### CORS Configuration
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://your-frontend-domain.com",
]
```

## 🚀 Deployment

### Backend Deployment (Render/Railway)

1. **Prepare for Deployment**:
```bash
# Install production dependencies
pip install gunicorn whitenoise

# Collect static files
python manage.py collectstatic

# Set environment variables
DEBUG=False
SECRET_KEY=your-production-secret-key
DATABASE_URL=your-postgresql-url
```

2. **Deploy to Render**:
   - Connect your GitHub repository
   - Set build command: `pip install -r requirements.txt`
   - Set start command: `gunicorn blog_project.wsgi:application`
   - Add environment variables

3. **Deploy to Railway**:
   - Connect your GitHub repository
   - Railway will auto-detect Django
   - Add environment variables in Railway dashboard

### Frontend Deployment (Vercel/Netlify)

1. **Update API URL**:
```javascript
const API_URL = process.env.REACT_APP_API_URL || 'https://your-backend-url.com/api';
```

2. **Deploy to Vercel**:
   - Connect your GitHub repository
   - Vercel will auto-detect React
   - Set environment variables in Vercel dashboard

3. **Deploy to Netlify**:
   - Connect your GitHub repository
   - Set build command: `npm run build`
   - Set publish directory: `build`
   - Add environment variables in Netlify dashboard

## 🔒 Security Features

- **JWT Authentication**: Secure token-based authentication
- **CORS Protection**: Configured for production domains
- **SQL Injection Protection**: Django ORM protection
- **XSS Protection**: Django's built-in protection
- **CSRF Protection**: Enabled for all forms
- **Password Validation**: Strong password requirements
- **Rate Limiting**: Configurable rate limiting
- **Input Validation**: Comprehensive validation on all endpoints

## 📊 Performance Optimizations

- **Database Indexing**: Optimized queries with proper indexes
- **Select Related**: Efficient database queries
- **Pagination**: Prevents large dataset loading
- **Caching**: Redis caching for frequently accessed data
- **Static Files**: CDN-ready static file serving
- **Image Optimization**: Automatic image processing

## 🧪 Testing

### Run Tests
```bash
python manage.py test
```

### API Testing
Use tools like Postman or curl to test endpoints:

```bash
# Test blog listing
curl http://localhost:8000/api/blogs/

# Test authentication
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'
```

## 📝 Environment Variables

### Required Variables
```env
SECRET_KEY=your-secret-key
DEBUG=True/False
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DB_NAME=omnify_blog
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# JWT
JWT_SECRET_KEY=your-jwt-secret

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

### Optional Variables
```env
# Email (for password reset)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password

# Production
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Check the documentation
- Review the API documentation

## 🔄 Updates and Maintenance

### Regular Maintenance Tasks
- Update dependencies regularly
- Monitor database performance
- Review and update security settings
- Backup database regularly
- Monitor error logs

### Version Updates
- Test thoroughly before updating
- Update requirements.txt
- Run migrations
- Test all endpoints
- Update documentation

---

**Built with ❤️ using Django REST Framework and React** 