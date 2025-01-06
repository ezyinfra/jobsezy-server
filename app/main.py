from fastapi import FastAPI, APIRouter
from app.routers import jobs_route
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel



# Create FastAPI app instance
app = FastAPI(title="jobsezy-backend")

api_router = APIRouter()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific origins like ['http://localhost:3000']
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@api_router.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

#router
app.include_router(api_router)
app.include_router(jobs_route.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
