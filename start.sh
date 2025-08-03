#!/bin/bash

echo "========================================"
echo "Starting Omnify Blog Application"
echo "========================================"

echo ""
echo "Starting backend server..."
cd server && npm run dev &
BACKEND_PID=$!

echo ""
echo "Waiting 5 seconds for backend to start..."
sleep 5

echo ""
echo "Starting frontend server..."
cd ../client && npm start &
FRONTEND_PID=$!

echo ""
echo "========================================"
echo "Application is starting..."
echo "========================================"
echo ""
echo "The application will be available at:"
echo "- Frontend: http://localhost:3000"
echo "- Backend: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop both servers"
echo ""

# Wait for user to stop the servers
trap "echo 'Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait 