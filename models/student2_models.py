from typing import Optional

from pydantic import BaseModel, Field


class CharacterSheet(BaseModel):
    id: Optional[int] = None
    name: str
    race: Optional[str] = None
    class_name: Optional[str] = Field(
        default=None,
        alias="class"
    )
    level: Optional[float] = None
    alignment: Optional[str] = None
    equipment: Optional[str] = None
    backstory: Optional[str] = None


class Stats(BaseModel):
    name: str
    strength: Optional[float] = None
    dexterity: Optional[float] = None
    constitution: Optional[float] = None
    intelligence: Optional[float] = None
    wisdom: Optional[float] = None
    charisma: Optional[float] = None
    perception: Optional[float] = None
    armor_class: Optional[float] = None
    hit_points: Optional[float] = None


class CharacterCreate(BaseModel):
    character: CharacterSheet
    stats: Stats