"""
FastAPI Backend for SRE Incident Commander
Provides REST API endpoints for incident analysis
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any, Optional
import uvicorn

from simple_crew import SimpleIncidentAnalysisCrew
from llm_config import health_check
from mock_data_loader import get_sample_incident_data


# Pydantic models for request/response
class IncidentRequest(BaseModel):
    alert: str
    logs: str
    metrics: str


class IncidentResponse(BaseModel):
    status: str
    incident_id: Optional[str] = None
    analysis: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


# Initialize FastAPI app
app = FastAPI(
    title="SRE Incident Commander",
    description="AI-powered incident analysis and response system",
    version="1.0.0"
)

# Configure CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the incident analysis crew
incident_crew = SimpleIncidentAnalysisCrew()


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "SRE Incident Commander API",
        "version": "1.0.0",
        "status": "operational"
    }


@app.get("/health")
async def health():
    """Health check endpoint"""
    llm_health = health_check()
    
    return {
        "api_status": "healthy",
        "llm_status": llm_health["status"],
        "llm_model": llm_health.get("model", "unknown"),
        "timestamp": "2024-12-22T10:35:00Z"
    }


@app.post("/analyze-incident", response_model=IncidentResponse)
async def analyze_incident(request: IncidentRequest):
    """
    Analyze an incident using the CrewAI multi-agent system
    
    Args:
        request: Incident data including alert, logs, and metrics
        
    Returns:
        Complete incident analysis results
    """
    try:
        # Prepare incident data for analysis
        incident_data = {
            "alert": request.alert,
            "logs": request.logs,
            "metrics": request.metrics
        }
        
        # Run the incident analysis crew
        analysis_result = incident_crew.analyze_incident(incident_data)
        
        if analysis_result.get("status") == "failed":
            raise HTTPException(
                status_code=500,
                detail=f"Incident analysis failed: {analysis_result.get('error', 'Unknown error')}"
            )
        
        return IncidentResponse(
            status="success",
            incident_id=analysis_result.get("incident_id"),
            analysis=analysis_result
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )


@app.get("/sample-incident")
async def get_sample_incident():
    """Get sample incident data for testing"""
    try:
        sample_data = get_sample_incident_data()
        return {
            "status": "success",
            "data": sample_data,
            "description": "Sample incident data for testing the analysis endpoint"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to load sample data: {str(e)}"
        )


@app.post("/analyze-sample")
async def analyze_sample_incident():
    """Analyze a sample incident for demo purposes"""
    try:
        # Get sample incident data
        sample_data = get_sample_incident_data()
        
        # Convert to request format
        request = IncidentRequest(
            alert=str(sample_data.get("alert", "")),
            logs=str(sample_data.get("logs", "")),
            metrics=str(sample_data.get("metrics", ""))
        )
        
        # Analyze the sample incident
        return await analyze_incident(request)
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to analyze sample incident: {str(e)}"
        )


if __name__ == "__main__":
    # Run the server
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
        log_level="info"
    )