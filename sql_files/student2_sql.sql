CREATE SCHEMA IF NOT EXISTS student2;
SET search_path TO student2;

DROP TABLE IF EXISTS character_sheet;
DROP TABLE IF EXISTS stats;


CREATE TABLE character_sheet (
  id SERIAL PRIMARY KEY
  ,name VARCHAR(100) NOT NULL
  ,race VARCHAR(20)
  ,class VARCHAR(20)
  ,level NUMERIC
  ,alignment VARCHAR(20)
  ,equipment TEXT
  ,backstory TEXT
);

CREATE TABLE stats (
  name VARCHAR(100) PRIMARY KEY
  ,strength NUMERIC
  ,dexterity NUMERIC
  ,constitution NUMERIC
  ,intelligence NUMERIC
  ,wisdom NUMERIC
  ,charisma NUMERIC
  ,perception NUMERIC
  ,armor_class NUMERIC
  ,hit_points NUMERIC
);

INSERT INTO character_sheet(name, race, class, level, alignment, equipment, backstory)
VALUES ('Braum Freljordson'
        ,'Dwarf'
        ,'Barbarian'
        ,4
        ,'Neutral good'
        ,'Battleaxe, 2x handaxe, 2x healing potion, backpack, bedroll, tinderbox, 10x torches, 9 days of rations, waterskin, 50 feet of hempen rope'
        ,'Braum was born in the mining settlement of Khazrun’s Rest, carved deep within the northern mountains. The village honored Dumathoin, the Keeper of Secrets Under the Mountain, and every dwarf there believed the earth’s riches were sacred gifts. Braum was an only child, raised by stern but loving parents. His father had once been an adventurer in his youth, roaming far from the mountains before returning home to mine and raise a family. From him, Braum inherited not only tales of glory, but also his twin axes — sturdy, well-balanced weapons. One of them hums faintly with dormant magic, though its true power has yet to awaken.
When he came of age, Braum followed his parents into the mines. Years underground made him an expert in stone and mineral; he can appraise gems at a glance and rarely loses his sense of direction in cave systems, even unfamiliar ones. He fought off spiders, goblins, drow and the occasional orc raid parties alongside his kin, and from those battles grew a deep hatred of orcs, goblins, and drow. His distrust extends to other elves as well — he watches them carefully and is easily provoked by their words or tone.
Then the mountain fell.
A devastating earthquake collapsed the cavern that housed Khazrun’s Rest. Braum survived, but most of the settlement — including his parents — perished beneath the rubble. After mourning their dead, the few survivors went their separate ways.
For seven winters now, Braum has wandered, taking on dangerous work — especially quests that pit him against powerful foes. In battle, his grief sharpens into fury. He laughs loudly, jokes crudely, and carries himself with the blunt humor typical of dwarves. He does not care for wealth, titles, or noble blood; he judges others solely by how they treat him.
Once, he wore the symbol of Dumathoin proudly around his neck. Now the amulet lies hidden beneath his clothes. Since the mountain took everything from him, his faith has begun to crack like fractured stone — though he has not yet cast it aside entirely.'
);

INSERT INTO stats(name, strength, dexterity, constitution, intelligence, wisdom, charisma, perception, armor_class, hit_points)
VALUES ('Braum Freljordson'
        ,18
        ,14
        ,19
        ,11
        ,12
        ,12
        ,13
        ,16
        ,59
);


INSERT INTO character_sheet(name, race, class, level, alignment, equipment, backstory)
VALUES ('Liron Modnar'
        ,'Drow'
        ,'Rogue'
        ,4
        ,'Neutral evil'
        ,'Rapier, shortbow, dagger, burglars pack, thieves tool, 2x health potions'
        ,'Liron groeide op in een drow samenleving waar trouw aan Lolth, geweld en onderdrukking de norm waren. Hij werd al vroeg door de priesters en matriarchen gevormd tot een wapen: efficiënt, meedogenloos en volledig overtuigd van de superioriteit van zijn volk. In zijn wereld was liegen, stelen en doden geen morele keuze, maar simpelweg hoe je overleefde en je plaats in de hiërarchie behield.
Zijn broer, Leonel, paste daar niet in. Tijdens een drow raid weigerde hij een wezen te doden uit medelijden. Binnen de gemeenschap werd dat niet gezien als goed, maar als zwakte. Vanaf dat moment werd Leonel steeds verder buitengesloten en met wantrouwen bekeken.
Uiteindelijk werd hij gearresteerd op verdenking van verraad en heresie tegen Lolth. Hij werd veroordeeld en geofferd in een tempel, tussen twee grote spinnenstandbeelden. Liron was aanwezig bij het ritueel en moest toekijken.
Die gebeurtenis liet iets in hem breken. Voor het eerst begon Liron te twijfelen aan de overtuigingen waarmee hij was opgegroeid en aan de wereld die hij altijd als absoluut had gezien.'
);

INSERT INTO stats(name, strength, dexterity, constitution, intelligence, wisdom, charisma, perception, armor_class, hit_points)
VALUES ('Liron Modnar'
        ,11
        ,20
        ,17
        ,12
        ,15
        ,18
        ,16
        ,15
        ,31
);

INSERT INTO character_sheet(name, race, class, level, alignment, equipment, backstory)
VALUES ('Arannis Moonshadow'
        ,'High Elf'
        ,'Wizard'
        ,4
        ,'Neutral good'
        ,'Spellbook, quarterstaff, component pouch, explorers pack'
        ,'Arannis Moonshadow grew up in an ancient elven city devoted
to knowledge and arcane study. From a young age he showed a strong talent for magic and spent most of his life studying
forgotten spells and magical artifacts. Now he travels the world in search of lost knowledge, ancient ruins, and powerful magic that could change the
fate of entire kingdoms.'
);

INSERT INTO stats(name, strength, dexterity, constitution, intelligence, wisdom, charisma, perception, armor_class, hit_points)
VALUES ('Arannis Moonshadow'
        ,10
        ,14
        ,12
        ,18
        ,13
        ,11
        ,14
        ,13
        ,42
);

INSERT INTO character_sheet(name, race, class, level, alignment, equipment, backstory)
VALUES ('Lyra Stormwind'
        ,'Human'
        ,'Ranger'
        ,4
        ,'Chaotic good'
        ,'Longbow, shortsword, explorers pack, leather armor'
        ,'Lyra grew up travelling between small villages and forests.
She learned to survive in the wilderness and became an experienced tracker.
She now travels with adventurers while searching for a mysterious creature that has been appearing near her homeland.'
);

INSERT INTO stats(name, strength, dexterity, constitution, intelligence, wisdom, charisma, perception, armor_class, hit_points)
VALUES ('Lyra Stormwind'
        ,13
        ,17
        ,14
        ,10
        ,15
        ,16
        ,16
        ,14
        ,37
);