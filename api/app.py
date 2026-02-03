"""FastAPI application for UltraskateDashboard"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import events, performances

app = FastAPI(
    title="UltraskateDashboard API",
    description="API for skateboard race event tracking and analysis",
    version="0.1.0",
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(events.router)
app.include_router(performances.router)


@app.get("/")
async def root():
    """Root endpoint - API health check"""
    return {
        "message": "UltraskateDashboard API",
        "version": "0.1.0",
        "status": "online",
    }


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}
