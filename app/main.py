import os
import uvicorn
from google.adk.cli.fast_api import get_fast_api_app
from fastapi import FastAPI

AGENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Get the absolute path of the directory containing main.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Pass the required keyword arguments
app: FastAPI = get_fast_api_app(
    agents_dir=AGENT_DIR,
    web=True,
    #artifact_service_uri=artifact_service_uri,
    #allow_origins=allow_origins,
    #session_service_uri=session_service_uri,
    #otel_to_cloud=True,
)
app.title = "lab-agent"
app.description = "API for interacting with the Agent lab-agent"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
