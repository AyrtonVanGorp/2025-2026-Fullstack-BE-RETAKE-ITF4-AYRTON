from pydantic import BaseModel
from typing import Optional

# 1. THE MODEL FOR TAKING DATA IN (The POST Request)
class NPCCreate(BaseModel):
    name: str
    surname: Optional[str] = None
    status: Optional[str] = "alive"
    description: Optional[str] = None
    modal_title: Optional[str] = None
    flavor_quote: Optional[str] = None
    modal_content: Optional[str] = None


# 2. THE BASE NPC MODEL (The one I accidentally deleted!)
class NPC(BaseModel):
    id: int
    name: str
    surname: str
    status: str
    description: str

    class Config:
        from_attributes = True


# 3. THE DETAILED NPC MODEL (For the GET Request)
class NPCDetail(NPC):
    modal_title: Optional[str] = None
    flavor_quote: Optional[str] = None
    modal_content: Optional[str] = None


# 4. WORLDBUILDING MODELS
class WorldBuildingCreate(BaseModel):
    title: str
    subtitle: Optional[str] = None
    description: str
    modal_content: Optional[str] = None

class WorldBuilding(WorldBuildingCreate):
    id: int

    class Config:
        from_attributes = True