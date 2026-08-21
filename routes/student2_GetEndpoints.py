from fastapi import APIRouter, HTTPException, Query

from database import get_db_connection
from queries.student2_queries import (
    get_all_characters,
    get_character_by_name
)


router = APIRouter(
    prefix="/characters",
    tags=["Characters"]
)


@router.get("/")
def read_characters():
    """
    Get all characters.
    """
    connection = get_db_connection()

    if connection is None:
        raise HTTPException(
            status_code=500,
            detail="Could not connect to database"
        )

    try:
        return get_all_characters(connection)

    finally:
        connection.close()


@router.get("/search")
def read_character(
        name: str = Query(
            ...,
            description="Name of the character"
        )
):
    """
    Get a character by name.
    """
    connection = get_db_connection()

    if connection is None:
        raise HTTPException(
            status_code=500,
            detail="Could not connect to database"
        )

    try:
        character = get_character_by_name(connection, name)

        if character is None:
            raise HTTPException(
                status_code=404,
                detail="Character not found"
            )

        return character

    finally:
        connection.close()