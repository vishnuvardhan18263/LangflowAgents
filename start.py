from langflow.main import run


import subprocess

subprocess.run([
    "python", "-m", "langflow", "run",
    "--host", "0.0.0.0",
    "--port", "7860",
    "--flow-file", "/workspaces/LangflowAgents/QC Audit Agent - Granite Model.json"
])