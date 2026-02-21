import json
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.models.schemas import AnalysisResponse, AnalysisRequest, ClientContext
from app.core.security import get_client_context
from app.services.audio_processor import AudioProcessor
from app.services.intelligence import IntelligenceService
from app.utils.file_helpers import save_temp_file, delete_file

router = APIRouter()
audio_service = AudioProcessor()
intel_service = IntelligenceService()

@router.post("/analyze/audio", response_model=AnalysisResponse)
async def analyze_audio_endpoint(
    file: UploadFile = File(...),
    # FastAPI automatically runs the security check and injects the context here!
    client_context: ClientContext = Depends(get_client_context) 
):
    temp_path = await save_temp_file(file)
    try:
        # Phase 2: Process Audio (AssemblyAI)
        audio_result = await audio_service.process_audio(temp_path)
        
        # Phase 3: Generate Insights (Gemini)
        # We pass the automatically retrieved context straight to the LLM
        insights = await intel_service.analyze_conversation(
            transcript=audio_result["transcript_text"],
            language=audio_result["language"],
            context=client_context 
        )
        
        return {
            "status": "success",
            "input_type": "audio",
            "core_intelligence": insights["core_intelligence"],
            "advanced_analysis": insights["advanced_analysis"],
            "raw_transcript": audio_result["transcript_text"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        delete_file(temp_path)

@router.post("/analyze/text", response_model=AnalysisResponse)
async def analyze_text_endpoint(request: AnalysisRequest):
    try:
        # For text, we skip audio processing and go straight to Gemini
        insights = await intel_service.analyze_conversation(
            transcript=request.transcript,
            language="auto-detected",
            context=request.client_context
        )
        
        return {
            "status": "success",
            "input_type": "text",
            "core_intelligence": insights["core_intelligence"],
            "advanced_analysis": insights["advanced_analysis"],
            "raw_transcript": request.transcript
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))