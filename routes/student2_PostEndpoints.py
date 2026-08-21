from fastapi import APIRouter, HTTPException

from database import get_db_connection
from models.student2_models import CharacterCreate
from queries.student2_queries import create_character


router = APIRouter(
    prefix="/characters",
    tags=["Characters"]
)


@router.post("/")
def add_character(character_data: CharacterCreate):
    """
    Create a new character and its stats.
    """
    connection = get_db_connection()

    if connection is None:
        raise HTTPException(
            status_code=500,
            detail="Could not connect to database"
        )

    try:
        return create_character(
            connection,
            character_data.character,
            character_data.stats
        )

    finally:
        connection.close()