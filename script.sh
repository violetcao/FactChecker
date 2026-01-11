# run the backend
pwd
cd backend
uvicorn main:app --reload &
cd ..
# run the frontend
cd frontend/factchecker
npm run dev




