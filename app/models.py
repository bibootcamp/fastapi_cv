from pydantic import BaseModel
from enum import Enum

class QualificationResponse(BaseModel):
    """
    Represents a qualification response model.
    """
    id: int
    date: str
    awarding_body: str
    qualification: str
    grade: str | None

class AchievementResponse(BaseModel):
    """
    Represents an achievement response model.
    """
    id: int
    description: str

class Employment(BaseModel):
    """
    Represents an employment model.
    """
    id: int
    start_date: str
    end_date: str | None
    employer: str
    position: str
    achievements: list[AchievementResponse]

class EmploymentResponse(BaseModel):
    """
    Represents an employment response model.
    """
    id: int
    start_date: str
    end_date: str | None
    employer: str
    position: str

class SkillResponse(BaseModel):
    """
    Represents a skill response model.
    """
    id: int
    description: str

class ContactResponse(BaseModel):
    """
    Represents a contact response model.
    """
    id: int
    type: str
    value: str

class ContactType(Enum):
    """
    Represents the type of contact.
    """
    EMAIL = "email"
    MOBILE = "mobile"
    LINKEDIN = "linkedin"

class UnauthorizedResponse(BaseModel):
    """
    Represents an unauthorized response model.
    """
    error: str