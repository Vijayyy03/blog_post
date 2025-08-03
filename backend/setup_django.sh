#!/bin/bash

echo "========================================"
echo "Setting up Django Blog Backend"
echo "========================================"

echo ""
echo "Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Error creating virtual environment"
    exit 1
fi

echo ""
echo "Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Error activating virtual environment"
    exit 1
fi

echo ""
echo "Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error installing dependencies"
    exit 1
fi

echo ""
echo "Creating .env file..."
if [ ! -f .env ]; then
    cat > .env << EOF
SECRET_KEY=django-insecure-your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=omnify_blog
DB_USER=postgres
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432
JWT_SECRET_KEY=your-jwt-secret-key-here
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
EOF
    echo ".env file created. Please update with your database credentials."
else
    echo ".env file already exists."
fi

echo ""
echo "Running migrations..."
python manage.py makemigrations
if [ $? -ne 0 ]; then
    echo "Error creating migrations"
    exit 1
fi

python manage.py migrate
if [ $? -ne 0 ]; then
    echo "Error running migrations"
    exit 1
fi

echo ""
echo "Creating superuser..."
python manage.py createsuperuser --email admin@omnify.com --name "Admin User" --noinput
if [ $? -ne 0 ]; then
    echo "Error creating superuser. You can create one manually later."
fi

echo ""
echo "Creating sample data..."
python setup.py
if [ $? -ne 0 ]; then
    echo "Error creating sample data"
    exit 1
fi

echo ""
echo "========================================"
echo "Django Backend Setup Complete!"
echo "========================================"
echo ""
echo "To start the server:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Run server: python manage.py runserver"
echo ""
echo "The backend will be available at:"
echo "- Backend: http://localhost:8000"
echo "- Admin: http://localhost:8000/admin"
echo "- API: http://localhost:8000/api"
echo ""
echo "Default superuser credentials:"
echo "- Email: admin@omnify.com"
echo "- Password: admin123"
echo "" 