from typing import Union
from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import APIKeyHeader
from .data import employment_data, qualification_data, skill_data, contact_data
from .models import QualificationResponse, EmploymentResponse, AchievementResponse, SkillResponse, ContactResponse
import os
from fastapi.templating import Jinja2Templates
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

description = """Ash's API provides programmatic access to my professional qualifications, employment history, achievements, and skills. 

Most endpoints are publicly accessible, allowing you to retrieve structured information about my background.
You can use the following endpoints:
- `/qualifications`: Get all qualifications.
- `/employment`: Get all employment data.
- `/employment/{employment_id}/achievements`: Get achievements for a specific employment.
- `/skills`: Get all skills.
- `/contact`: Get contact information **(requires API key)**.

The `/qualifications`, `/employment`, `/skills` endpoints are publicly accessible and do not require authentication. You can access them without any API key.
"""

app = FastAPI(
    title="Ash's API",
    description=description,
    summary="Collection of endpoints to gather my details."
)

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))
header_scheme = APIKeyHeader(name="x-key")

@app.get("/", response_model=str, include_in_schema=False)
def hello_world(request: Request):
    """Return a hello world message."""
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@app.get("/qualifications", response_model=list[QualificationResponse])
def qualifications():
    """Get all qualifications."""
    return qualification_data

@app.get("/employment", response_model=list[EmploymentResponse])
def employment():
    """Get all employment data."""
    return_data = []
    for employer in employment_data:
        return_data.append(EmploymentResponse(
            id=employer.id,
            start_date=employer.start_date,
            end_date=employer.end_date,
            employer=employer.employer,
            position=employer.position
        ))
    return return_data

@app.get("/employment/{employment_id}/achievements", response_model=Union[list[AchievementResponse],None])
def employment_achievements(employment_id: int):
    """Get achievements for a specific employment."""
    return_data = [x for x in employment_data if x.id == employment_id]
    if return_data:
        return return_data[0].achievements    
    return None

@app.get("/skills", response_model=list[SkillResponse])
def skills():
    """Get all skills."""
    return skill_data

@app.get("/contact", response_model=list[ContactResponse])
async def contact(key: str = Depends(header_scheme)):
    """Get contact information."""
    if key != os.getenv("API_KEY"):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return contact_data