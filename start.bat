@echo off
echo Starting BIRA Backend and Frontend...

cd backend
start cmd /k ".\venv\Scripts\python.exe -m uvicorn app.main:app --reload --port 8000"

cd ..\frontend
start cmd /k "npm run dev"

echo Both services started!
