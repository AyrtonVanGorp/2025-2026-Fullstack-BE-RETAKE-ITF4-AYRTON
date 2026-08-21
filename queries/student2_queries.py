from models.student2_models import CharacterSheet, Stats


def get_all_characters(connection):
    query = """
        SELECT
            c.id,
            c.name,
            c.race,
            c.class,
            c.level,
            c.alignment,
            c.equipment,
            c.backstory,
            s.strength,
            s.dexterity,
            s.constitution,
            s.intelligence,
            s.wisdom,
            s.charisma,
            s.perception,
            s.armor_class,
            s.hit_points
        FROM student2.character_sheet AS c
        LEFT JOIN student2.stats AS s
            ON c.name = s.name
        ORDER BY c.id;
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def get_character_by_name(connection, name):
    query = """
        SELECT
            c.id,
            c.name,
            c.race,
            c.class,
            c.level,
            c.alignment,
            c.equipment,
            c.backstory,
            s.strength,
            s.dexterity,
            s.constitution,
            s.intelligence,
            s.wisdom,
            s.charisma,
            s.perception,
            s.armor_class,
            s.hit_points
        FROM student2.character_sheet AS c
        LEFT JOIN student2.stats AS s
            ON c.name = s.name
        WHERE c.name = %s;
    """

    with connection.cursor() as cursor:
        cursor.execute(query, (name,))
        return cursor.fetchone()


def create_character(connection, character: CharacterSheet, stats: Stats):
    character_query = """
        INSERT INTO student2.character_sheet (
            name,
            race,
            class,
            level,
            alignment,
            equipment,
            backstory
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """

    stats_query = """
        INSERT INTO student2.stats (
            name,
            strength,
            dexterity,
            constitution,
            intelligence,
            wisdom,
            charisma,
            perception,
            armor_class,
            hit_points
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    try:
        with connection.cursor() as cursor:

            cursor.execute(
                character_query,
                (
                    character.name,
                    character.race,
                    character.class_name,
                    character.level,
                    character.alignment,
                    character.equipment,
                    character.backstory
                )
            )

            character_id = cursor.fetchone()["id"]

            cursor.execute(
                stats_query,
                (
                    stats.name,
                    stats.strength,
                    stats.dexterity,
                    stats.constitution,
                    stats.intelligence,
                    stats.wisdom,
                    stats.charisma,
                    stats.perception,
                    stats.armor_class,
                    stats.hit_points
                )
            )

        connection.commit()

        return {
            "id": character_id,
            "name": character.name,
            "message": "Character created successfully"
        }

    except Exception:
        connection.rollback()
        raise