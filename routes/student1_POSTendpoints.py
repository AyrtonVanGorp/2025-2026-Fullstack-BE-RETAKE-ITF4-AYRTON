from fastapi import APIRouter, HTTPException
from database import get_db_connection

# 1. FIXED: Imported NPCCreate!
from models.student1_models import WorldBuilding, WorldBuildingCreate, NPCCreate
from queries.student1_queries import INSERT_WORLDBUILDING

router = APIRouter()


@router.post("/worldbuilding", response_model=WorldBuilding)
def create_location(location: WorldBuildingCreate):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        # ADDED location.modal_content here!
        cur.execute(INSERT_WORLDBUILDING,
                    (location.title, location.subtitle, location.description, location.modal_content))

        new_row = cur.fetchone()
        conn.commit()
        return {**location.model_dump(), "id": new_row['id']}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Could not create location: {str(e)}")
    finally:
        cur.close()
        conn.close()


@router.delete("/npcs/{npc_id}")
def delete_npc(npc_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        # 1. Delete the secrets first to prevent Foreign Key errors
        cur.execute("DELETE FROM student1.npc_modal WHERE npc_id = %s;", (npc_id,))

        # 2. Delete the core NPC
        cur.execute("DELETE FROM student1.npc WHERE id = %s;", (npc_id,))

        conn.commit()
        return {"message": "Soul permanently erased."}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()


@router.post("/npcs")
def create_npc(npc: NPCCreate):
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        # Insert the core NPC and immediately grab the new ID
        cur.execute("""
                    INSERT INTO student1.npc (name, surname, status, description)
                    VALUES (%s, %s, %s, %s) RETURNING id;
                    """, (npc.name, npc.surname, npc.status, npc.description))

        new_row = cur.fetchone()
        new_npc_id = new_row['id']

        # If they provided ANY modal data, insert it into the second table
        if npc.modal_content or npc.modal_title or npc.flavor_quote:
            cur.execute("""
                        INSERT INTO student1.npc_modal (npc_id, modal_title, flavor_quote, modal_content)
                        VALUES (%s, %s, %s, %s);
                        """, (new_npc_id, npc.modal_title, npc.flavor_quote, npc.modal_content))

        conn.commit()
        return {"message": "NPC and Secrets successfully archived"}

    except Exception as e:
        conn.rollback()
        print(f"CRITICAL DATABASE ERROR: {repr(e)}")
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cur.close()
        conn.close()


# --- FIXED: Moved this OUT of the 'finally' block above ---
@router.delete("/worldbuilding/{location_id}")
def delete_location(location_id: int):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        # We only have one table to delete from here!
        cur.execute("DELETE FROM student1.worldbuilding WHERE id = %s;", (location_id,))

        conn.commit()
        return {"message": "Location permanently erased."}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()