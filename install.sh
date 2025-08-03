#!/bin/bash

echo "========================================"
echo "Installing Omnify Blog Application"
echo "========================================"

echo ""
echo "Installing backend dependencies..."
cd server
npm install
if [ $? -ne 0 ]; then
    echo "Error installing backend dependencies"
    exit 1
fi

echo ""
echo "Installing frontend dependencies..."
cd ../client
npm install
if [ $? -ne 0 ]; then
    echo "Error installing frontend dependencies"
    exit 1
fi

echo ""
echo "========================================"
echo "Installation completed successfully!"
echo "========================================"
echo ""
echo "To start the application:"
echo "1. Start MongoDB (if not already running)"
echo "2. Open a terminal and run: cd server && npm run dev"
echo "3. Open another terminal and run: cd client && npm start"
echo ""
echo "The application will be available at:"
echo "- Frontend: http://localhost:3000"
echo "- Backend: http://localhost:5000"
echo "" 