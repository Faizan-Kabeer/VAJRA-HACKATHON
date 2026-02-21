import assemblyai as aai
from app.core.config import settings

class AudioProcessor:
    def __init__(self):
        # Initialize settings using the API key from our config
        aai.settings.api_key = settings.ASSEMBLYAI_API_KEY
        self.transcriber = aai.Transcriber()

    async def process_audio(self, file_path: str) -> dict:
        """
        Transcribes audio, performs diarization, and detects language.
        """
        # Configure the transcription based on your notebook's successful parameters
        config = aai.TranscriptionConfig(
            language_detection=True,
            speaker_labels=True,
            # Utilizing the latest models for better accuracy
            speech_models=["universal-3-pro", "universal-2"] 
        )

        # Start the transcription process
        transcript = self.transcriber.transcribe(file_path, config)

        if transcript.error:
            raise Exception(f"AssemblyAI Error: {transcript.error}")

        # Extract the language code (e.g., 'en')
        detected_language = transcript.json_response.get("language_code", "unknown")

        # Format the interleaved utterances with speaker labels
        formatted_transcript = "\n".join(
            [f"Speaker {u.speaker}: {u.text}" for u in transcript.utterances]
        )

        return {
            "transcript_text": formatted_transcript,
            "language": detected_language,
            "raw_data": transcript.json_response # Stored for any future debugging
        }