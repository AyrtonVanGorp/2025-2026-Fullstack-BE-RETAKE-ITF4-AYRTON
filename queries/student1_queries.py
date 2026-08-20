SELECT_ALL_NPCS = """
SELECT 
    n.id, 
    n.name, 
    n.surname, 
    n.status, 
    n.description,
    m.modal_title, 
    m.flavor_quote, 
    m.modal_content
FROM student1.npc n
LEFT JOIN student1.npc_modal m ON n.id = m.npc_id
ORDER BY n.id;
"""

SELECT_NPC_DETAIL = """
SELECT
    n.id, 
    n.name, 
    n.surname, 
    n.status, 
    n.description,
    m.modal_title, 
    m.flavor_quote, 
    m.modal_content
FROM student1.npc n
LEFT JOIN student1.npc_modal m ON n.id = m.npc_id
WHERE n.id = %s;
"""

INSERT_WORLDBUILDING = """
INSERT INTO student1.worldbuilding (title, subtitle, description, modal_content)
VALUES (%s, %s, %s, %s)
RETURNING id;
"""

SELECT_ALL_WORLDBUILDING = """
SELECT id, title, subtitle, description, modal_content
FROM student1.worldbuilding
ORDER BY id;
"""

INSERT_WORLDBUILDING = """
INSERT INTO student1.worldbuilding (title, subtitle, description, modal_content)
VALUES (%s, %s, %s, %s)
RETURNING id;
"""

SELECT_ALL_WORLDBUILDING = """
SELECT id, title, subtitle, description, modal_content
FROM student1.worldbuilding
ORDER BY id;
"""