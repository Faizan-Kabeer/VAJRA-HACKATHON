import json
from google import genai
from google.genai import types
from app.core.config import settings
from app.models.schemas import ClientContext

class IntelligenceService:
    def __init__(self):
        # The new SDK uses a Client object
        self.client = genai.Client(api_key=settings.GEMINI_API_KEY)
        self.model_name = 'gemini-3-flash-preview'

    async def analyze_conversation(
        self, 
        transcript: str, 
        language: str, 
        context: ClientContext
    ) -> dict:
        """
        Synthesizes core intelligence and advanced business analysis.
        """
        
        prompt = f"""
        You are an AI Business Analyst. Analyze the transcript below based on the provided CLIENT CONTEXT.
        
        ### CLIENT CONTEXT
        - Business Domain: {context.domain}
        - Relevant Products: {", ".join(context.products)}
        - Internal Policies: {", ".join(context.policies)}
        - Risk Triggers: {", ".join(context.risk_triggers)}
        
        ### TRANSCRIPT ({language})
        {transcript}
        
        ### TASK
        1. Summarize the call.
        2. Identify customer intents and key topics.
        3. Perform Advanced Analysis: 
           - Detect any policy violations by the agent.
           - Identify risk triggers.
           - Assign a Risk Score (0-100) and determine the call outcome.
        
        ### OUTPUT FORMAT
        You must respond ONLY with a JSON object that matches this structure:
        {{
            "core_intelligence": {{
                "summary": "string",
                "detected_languages": ["string"],
                "overall_sentiment": "string",
                "primary_intents": ["string"],
                "key_topics": ["string"]
            }},
            "advanced_analysis": {{
                "compliance_violations": ["string"],
                "risk_score": 0,
                "risk_flags": ["string"],
                "call_outcome": "Resolved | Escalated | Dropped | Unresolved",
                "agent_quality_score": 0
            }}
        }}
        """

        try:
            # The new generation method and JSON config syntax
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )
            
            analysis_data = json.loads(response.text)
            return analysis_data

        except Exception as e:
            raise Exception(f"Intelligence Engine Error: {str(e)}")