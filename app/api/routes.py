from fastapi import APIRouter, UploadFile, File, HTTPException
from app.nodes.orchestrator_flow import OrchestratorFlow

router = APIRouter()
flow = OrchestratorFlow()

@router.post("/analyze_audio")
async def analyze_audio(file: UploadFile = File(...)):
    try:
        file_location = f"temp/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())

        result = flow.run(file_location)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
