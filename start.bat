@echo off
echo ========================================
echo Starting Omnify Blog Application
echo ========================================

echo.
echo Starting backend server...
start "Backend Server" cmd /k "cd server && npm run dev"

echo.
echo Waiting 5 seconds for backend to start...
timeout /t 5 /nobreak > nul

echo.
echo Starting frontend server...
start "Frontend Server" cmd /k "cd client && npm start"

echo.
echo ========================================
echo Application is starting...
echo ========================================
echo.
echo The application will be available at:
echo - Frontend: http://localhost:3000
echo - Backend: http://localhost:5000
echo.
echo Press any key to close this window...
pause > nul 