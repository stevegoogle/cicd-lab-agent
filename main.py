import os
import uvicorn
from google.adk.cli.fast_api import get_fast_api_app
# Even if we don't pass 'root_agent' directly, we must import it 
# so the ADK loader can find it in the directory scan.
from agent import root_agent 

# Get the absolute path of the directory containing main.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Pass the required keyword arguments
app = get_fast_api_app(agents_dir=current_dir, web=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
