from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.redis_client import redis_client
from app.neo4j_client import neo4j_client

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await neo4j_client.connect()
    yield
    # Shutdown
    await redis_client.aclose()
    await neo4j_client.close()

app = FastAPI(
    title="BIRA API",
    description="Business Intelligence Research Agent API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Update for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "BIRA API is running"}
