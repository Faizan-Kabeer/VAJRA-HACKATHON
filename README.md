🎙️ Conversation Intelligence API
=================================

An enterprise-ready, API-first backend system designed to analyze multimodal customer conversations (audio recordings or text transcripts). It leverages advanced AI to extract structured business insights, detect compliance violations, and generate risk scores based on configurable, client-specific business rules.

✨ Core Features
---------------

*   **Multimodal Input Handling:** Accept either raw audio files (.wav, .mp3) or text-based conversation transcripts.
    
*   **Auto-Language Detection & Diarization:** Automatically identifies the spoken language and separates speakers (Customer vs. Agent) using AssemblyAI's state-of-the-art models.
    
*   **Multi-Tenant Client Context:** Automatically injects specific business rules, policies, and risk triggers into the AI analysis based on the authenticated client's API key.
    
*   **Advanced Compliance & Risk Analysis:** Utilizes Google Gemini to flag policy violations, detect risky behaviors (e.g., scam attempts, unauthorized tools), and objectively score the call outcome.
    
*   **Strict Structured Output:** Guarantees a fully structured JSON response ready for enterprise database ingestion or frontend consumption.
    

🛠️ Tech Stack
--------------

*   **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Python)
    
*   **Audio Processing:** [AssemblyAI](https://www.assemblyai.com/) (universal-3-pro & universal-2 models)
    
*   **Intelligence Engine:** Google Gemini (gemini-2.5-flash via the new google-genai SDK)
    
*   **Data Validation & Serialization:** Pydantic
    

📂 Project Structure
--------------------

Plaintext

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   conversation-intelligence/  ├── app/  │   ├── api/  │   │   └── routes.py           # API endpoints (/analyze/audio, /analyze/text)  │   ├── core/  │   │   ├── config.py           # Environment variables & setting management  │   │   └── security.py         # API Key auth & Client Context mock database  │   ├── models/  │   │   └── schemas.py          # Pydantic models enforcing strict JSON structures  │   ├── services/  │   │   ├── audio_processor.py  # AssemblyAI transcription & diarization logic  │   │   └── intelligence.py     # Gemini Prompt Engineering & JSON enforcement  │   ├── utils/  │   │   └── file_helpers.py     # Safe temporary file management for audio uploads  │   └── main.py                 # FastAPI application instance & routing  ├── client.py                   # Automated Python script to test the API  ├── requirements.txt            # Project dependencies  └── README.md                   # Project documentation   `

⚙️ Setup & Installation
-----------------------

### 1\. Prerequisites

*   Python 3.9+ installed on your system.
    
*   API keys for AssemblyAI and Google Gemini.
    

### 2\. Create and Activate a Virtual Environment

It is highly recommended to run this project inside an isolated virtual environment to prevent package conflicts.

**Windows:**

DOS

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m venv venv  venv\Scripts\activate   `

**macOS / Linux:**

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python3 -m venv venv  source venv/bin/activate   `

### 3\. Install Dependencies

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

### 4\. Configure Environment Variables

The system relies on secure API keys to function. Create a file named .env in the root directory of the project:

Plaintext

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # External AI Services  ASSEMBLYAI_API_KEY=your_assemblyai_api_key_here  GEMINI_API_KEY=your_google_gemini_api_key_here  # Local API Security (Used for authenticating your clients)  MY_BACKEND_API_KEY=finance-corp-key-123   `

_(Note: Ensure .env is added to your .gitignore file)._

### 5\. Start the Server

Start the FastAPI backend using the Uvicorn server. We specify --port 8080 to prevent common Windows socket access errors (\[WinError 10013\]).

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   uvicorn app.main:app --reload --port 8080   `

If successful, the terminal will display: INFO: Application startup complete.

🚀 Usage & API Documentation
----------------------------

FastAPI automatically generates an interactive Swagger UI. Once the server is running, navigate to:

👉 [**http://127.0.0.1:8080/docs**](https://www.google.com/search?q=http://127.0.0.1:8080/docs)

### Example: Testing via Python Client

You can test the machine-to-machine integration using the provided client.py script. Ensure rec1.wav is in the same directory.

Python

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   import requests  import json  url = "http://127.0.0.1:8080/api/v1/analyze/audio"  # The server looks up this key to apply the correct Client Context business rules  headers = {      "X-API-Key": "finance-corp-key-123"   }  with open("rec1.wav", "rb") as audio_file:      files_payload = {"file": audio_file}      print("Uploading audio... Please wait.")      response = requests.post(url, files=files_payload, headers=headers)      response.raise_for_status()      print(json.dumps(response.json(), indent=2))   `

### Example: Testing via cURL

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   curl -X 'POST' \    'http://127.0.0.1:8080/api/v1/analyze/audio' \    -H 'accept: application/json' \    -H 'X-API-Key: finance-corp-key-123' \    -H 'Content-Type: multipart/form-data' \    -F 'file=@rec1.wav'   `

🧠 Design Decisions & Assumptions
---------------------------------

1.  **FastAPI for the Backend:** Chosen for its native asynchronous capabilities. Audio transcription and LLM generation are heavy I/O tasks; FastAPI's async/await ensures the server remains responsive to other requests while waiting for these third-party APIs.
    
2.  **Separation of Services:** Audio processing (audio\_processor.py) and Intelligence (intelligence.py) are decoupled into distinct service classes. This allows either provider (e.g., swapping AssemblyAI for OpenAI Whisper) to be changed in the future without rewriting the core API routes.
    
3.  **Dependency Injection for Client Context:** Instead of forcing clients to pass their business rules in every single API request, the system uses FastAPI's Depends to securely look up the client's configuration based on their X-API-Key. This mimics a secure, multi-tenant B2B architecture, preventing malicious injection of relaxed compliance rules.
    
4.  **Gemini Native JSON Mode:** We utilize the response\_mime\_type="application/json" configuration in the google-genai SDK. This forces the LLM to strictly adhere to the Pydantic schema, eliminating conversational filler and guaranteeing an enterprise-ready data structure.
    
5.  **Assumptions:** \* The system assumes uploaded audio files are of reasonable length (under ~30 minutes) for synchronous HTTP processing. For massive enterprise files, an asynchronous background task + webhook architecture would be required.
    
    *   It assumes the X-API-Key maps correctly to a valid ClientContext dictionary/database entry.