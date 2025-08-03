# Troubleshooting Guide

This guide helps you resolve common issues with the Omnify Blog Application.

## Common Issues

### 1. "Failed to fetch blogs" Error

**Symptoms:**
- Frontend shows "Failed to fetch blogs" error
- No blogs appear on the homepage
- Network errors in browser console

**Solutions:**

#### A. Check Django Backend
1. **Ensure Django server is running:**
   ```bash
   cd backend
   source venv/bin/activate  # Linux/macOS
   # or venv\Scripts\activate  # Windows
   python manage.py runserver
   ```

2. **Test API endpoints directly:**
   ```bash
   cd backend
   python test_api.py
   ```

3. **Check if blogs exist in database:**
   ```bash
   cd backend
   python manage.py shell
   ```
   ```python
   from blogs.models import Blog
   print(f"Total blogs: {Blog.objects.count()}")
   print(f"Published blogs: {Blog.objects.filter(status='published').count()}")
   ```

#### B. Check Frontend Configuration
1. **Verify API URL in frontend:**
   - Check `client/.env` file
   - Ensure `REACT_APP_API_URL=http://localhost:8000/api`

2. **Check browser console for CORS errors:**
   - Open browser developer tools (F12)
   - Look for CORS-related errors in Console tab

#### C. Database Issues
1. **Reset database and recreate sample data:**
   ```bash
   cd backend
   python manage.py flush  # Clear all data
   python setup.py  # Recreate sample data
   ```

2. **Check PostgreSQL connection:**
   ```bash
   # Test PostgreSQL connection
   psql -h localhost -U postgres -d omnify_blog
   ```

### 2. CORS Errors

**Symptoms:**
- Browser console shows CORS errors
- API calls fail with "Access-Control-Allow-Origin" errors

**Solutions:**

1. **Check Django CORS settings:**
   ```python
   # In backend/blog_project/settings.py
   CORS_ALLOWED_ORIGINS = [
       "http://localhost:3000",
       "http://127.0.0.1:3000",
   ]
   ```

2. **Ensure django-cors-headers is installed:**
   ```bash
   cd backend
   pip install django-cors-headers
   ```

3. **Restart Django server after changes**

### 3. Database Connection Issues

**Symptoms:**
- Django server fails to start
- Database connection errors

**Solutions:**

1. **Check PostgreSQL is running:**
   ```bash
   # Linux/macOS
   sudo systemctl status postgresql
   
   # Windows
   # Check Services app for PostgreSQL
   ```

2. **Verify database exists:**
   ```bash
   createdb omnify_blog
   ```

3. **Check .env file:**
   ```env
   DB_NAME=omnify_blog
   DB_USER=postgres
   DB_PASSWORD=your-password
   DB_HOST=localhost
   DB_PORT=5432
   ```

### 4. Authentication Issues

**Symptoms:**
- Login/register fails
- JWT token errors

**Solutions:**

1. **Check JWT settings:**
   ```python
   # In backend/blog_project/settings.py
   SIMPLE_JWT = {
       'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
       'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
   }
   ```

2. **Verify JWT_SECRET_KEY in .env:**
   ```env
   JWT_SECRET_KEY=your-jwt-secret-key-here
   ```

### 5. Migration Issues

**Symptoms:**
- Django shows migration errors
- Database schema issues

**Solutions:**

1. **Reset migrations:**
   ```bash
   cd backend
   rm -rf blogs/migrations/*
   rm -rf users/migrations/*
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Recreate superuser:**
   ```bash
   python manage.py createsuperuser
   ```

### 6. Frontend Build Issues

**Symptoms:**
- React app fails to start
- Build errors

**Solutions:**

1. **Clear node_modules and reinstall:**
   ```bash
   cd client
   rm -rf node_modules package-lock.json
   npm install
   ```

2. **Check Node.js version:**
   ```bash
   node --version  # Should be 16+ or 18+
   ```

3. **Clear browser cache and restart**

### 7. API Endpoint Issues

**Common API Issues:**

1. **Wrong endpoint URLs:**
   - Use `/blogs/` (with trailing slash) for list
   - Use `/blogs/create/` for creation
   - Use `/blogs/{slug}/` for detail

2. **Missing trailing slashes:**
   - Django URLs require trailing slashes
   - Frontend should include trailing slashes

3. **Authentication headers:**
   - Ensure `Authorization: Bearer <token>` header
   - Check token expiration

## Debugging Steps

### Step 1: Check Backend Status
```bash
cd backend
python manage.py runserver
# Should show: Django version X.X.X, using settings 'blog_project.settings'
```

### Step 2: Test API Endpoints
```bash
# Test blogs endpoint
curl http://localhost:8000/api/blogs/

# Test categories endpoint
curl http://localhost:8000/api/blogs/categories/

# Test tags endpoint
curl http://localhost:8000/api/blogs/tags/
```

### Step 3: Check Frontend
```bash
cd client
npm start
# Should open http://localhost:3000
```

### Step 4: Browser Debugging
1. Open browser developer tools (F12)
2. Go to Network tab
3. Refresh page
4. Look for failed API requests
5. Check Console tab for errors

### Step 5: Database Verification
```bash
cd backend
python manage.py shell
```
```python
from blogs.models import Blog, Category, Tag
from users.models import User

print(f"Users: {User.objects.count()}")
print(f"Categories: {Category.objects.count()}")
print(f"Tags: {Tag.objects.count()}")
print(f"Blogs: {Blog.objects.count()}")
print(f"Published blogs: {Blog.objects.filter(status='published').count()}")
```

## Environment Variables Checklist

### Backend (.env)
```env
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=omnify_blog
DB_USER=postgres
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=5432
JWT_SECRET_KEY=your-jwt-secret-key-here
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### Frontend (.env)
```env
REACT_APP_API_URL=http://localhost:8000/api
```

## Common Error Messages

### "ModuleNotFoundError: No module named 'django'"
**Solution:** Activate virtual environment
```bash
cd backend
source venv/bin/activate  # Linux/macOS
# or venv\Scripts\activate  # Windows
```

### "psycopg2.OperationalError: connection to server failed"
**Solution:** Check PostgreSQL is running and credentials are correct

### "CORS error: Access-Control-Allow-Origin"
**Solution:** Check CORS settings and restart Django server

### "Failed to fetch blogs"
**Solution:** Check API endpoints and network connectivity

## Getting Help

If you're still experiencing issues:

1. **Check the logs:**
   - Django server logs in terminal
   - Browser console logs
   - Network tab in browser dev tools

2. **Verify all services are running:**
   - PostgreSQL database
   - Django backend (port 8000)
   - React frontend (port 3000)

3. **Test with the provided test script:**
   ```bash
   cd backend
   python test_api.py
   ```

4. **Reset and recreate:**
   ```bash
   # Backend
   cd backend
   python manage.py flush
   python setup.py
   
   # Frontend
   cd client
   npm start
   ```

## Performance Tips

1. **Use Django Debug Toolbar** for development
2. **Enable database query logging** for debugging
3. **Use browser caching** for static files
4. **Optimize database queries** with select_related/prefetch_related

## Security Checklist

1. **Change default passwords** in production
2. **Use strong SECRET_KEY** values
3. **Set DEBUG=False** in production
4. **Configure proper CORS** for production domains
5. **Use HTTPS** in production
6. **Regular security updates** for dependencies 