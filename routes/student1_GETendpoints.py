from fastapi import APIRouter, HTTPException
from typing import List
from database import get_db_connection
from models.student1_models import NPC, NPCDetail
from queries.student1_queries import SELECT_ALL_NPCS, SELECT_NPC_DETAIL, SELECT_ALL_WORLDBUILDING

router = APIRouter()


# 1. FIXED: Changed List[NPC] to List[NPCDetail] to let the secrets through!
@router.get("/npcs", response_model=List[NPCDetail])
def get_npcs():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(SELECT_ALL_NPCS)
        results = cur.fetchall()
        return results
    except Exception as e:
        print(f"Database Error: {e}")
        raise HTTPException(status_code=500, detail="Could not fetch NPCs")
    finally:
        cur.close()
        conn.close()


@router.get("/npcs/{npc_id}", response_model=NPCDetail)
def get_npc_detail(npc_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        # We pass (npc_id,) as a tuple to match the %s in your query
        cur.execute(SELECT_NPC_DETAIL, (npc_id,))
        result = cur.fetchone()

        if not result:
            raise HTTPException(status_code=404, detail="NPC not found")
        return result
    except Exception as e:
        # Don't catch our own 404 error and turn it into a 500 error
        if isinstance(e, HTTPException):
            raise e
        print(f"Database Error: {e}")
        raise HTTPException(status_code=500, detail="Could not fetch NPC details")
    finally:
        cur.close()
        conn.close()


@router.get("/worldbuilding")
def get_worldbuilding_locations():
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")

    try:
        cur = conn.cursor()
        cur.execute(SELECT_ALL_WORLDBUILDING)
        locations = cur.fetchall()
        return locations
    except Exception as e:
        print(f"Database Error: {e}")
        raise HTTPException(status_code=500, detail="Could not fetch locations")
    finally:
        if conn:
            cur.close()
            conn.close()