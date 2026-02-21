from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.api.routes import router as api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Backend API for Multimodal Conversation Intelligence"
)

# Include the routes defined in Phase 4
app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "online"}