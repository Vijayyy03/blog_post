@echo off
echo ========================================
echo Setting up Django Blog Backend
echo ========================================

echo.
echo Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo Error creating virtual environment
    pause
    exit /b 1
)

echo.
echo Activating virtual environment...
call venv\Scripts\activate
if %errorlevel% neq 0 (
    echo Error activating virtual environment
    pause
    exit /b 1
)

echo.
echo Installing dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing dependencies
    pause
    exit /b 1
)

echo.
echo Creating .env file...
if not exist .env (
    echo SECRET_KEY=django-insecure-your-secret-key-here > .env
    echo DEBUG=True >> .env
    echo ALLOWED_HOSTS=localhost,127.0.0.1 >> .env
    echo DB_NAME=omnify_blog >> .env
    echo DB_USER=postgres >> .env
    echo DB_PASSWORD= >> .env
    echo DB_HOST=localhost >> .env
    echo DB_PORT=5432 >> .env
    echo JWT_SECRET_KEY=your-jwt-secret-key-here >> .env
    echo CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000 >> .env
    echo .env file created. Please update with your database credentials.
) else (
    echo .env file already exists.
)

echo.
echo Running migrations...
python manage.py makemigrations
if %errorlevel% neq 0 (
    echo Error creating migrations
    pause
    exit /b 1
)

python manage.py migrate
if %errorlevel% neq 0 (
    echo Error running migrations
    pause
    exit /b 1
)

echo.
echo Creating superuser...
python manage.py createsuperuser --email admin@omnify.com --name "Admin User" --noinput
if %errorlevel% neq 0 (
    echo Error creating superuser. You can create one manually later.
)

echo.
echo Creating sample data...
python setup.py
if %errorlevel% neq 0 (
    echo Error creating sample data
    pause
    exit /b 1
)

echo.
echo ========================================
echo Django Backend Setup Complete!
echo ========================================
echo.
echo To start the server:
echo 1. Activate virtual environment: venv\Scripts\activate
echo 2. Run server: python manage.py runserver
echo.
echo The backend will be available at:
echo - Backend: http://localhost:8000
echo - Admin: http://localhost:8000/admin
echo - API: http://localhost:8000/api
echo.
echo Default superuser credentials:
echo - Email: admin@omnify.com
echo - Password: admin123
echo.
pause 