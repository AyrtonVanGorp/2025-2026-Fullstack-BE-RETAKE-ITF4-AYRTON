CREATE SCHEMA IF NOT EXISTS student1;
SET search_path TO student1;

DROP TABLE IF EXISTS npc_modal;
DROP TABLE IF EXISTS worldbuilding;
DROP TABLE IF EXISTS npcs;


CREATE TABLE npc (
    id SERIAL PRIMARY KEY
    ,name VARCHAR(100) NOT NULL
    ,surname VARCHAR(100)
    ,status VARCHAR(20)
    ,description TEXT

);

CREATE TABLE worldbuilding (
    id SERIAL PRIMARY KEY
    ,title VARCHAR(100) NOT NULL
    ,subtitle VARCHAR(100)
    ,description text
);

CREATE TABLE npc_modal (
    id SERIAL PRIMARY KEY
    ,npc_id INTEGER REFERENCES npc(id) ON DELETE CASCADE
    ,modal_title VARCHAR(100)
    ,flavor_quote TEXT
    ,modal_content TEXT
);

INSERT INTO npc(name, surname, status, description)
VALUES ('Lissandra'
        ,'Vale'
        , 'alive'
        ,'A beautiful young lady and daughter of Edric Vale. She volunteers in a soup kitchen in the poorest parts of the city. The party first met her in this very kitchen, where she served them some of the most delicious soup the party has ever tasted.'
);

INSERT INTO npc(name, surname, status, description)
VALUES ('Marice'
        ,'Holden'
        ,'deceased'
        ,$$A politician running for mayor that strives for equality and is against corruption. Marice was Edric's rival in the elections. He hasn't interacted much with the party, since his only encounter with them led to his death. He was brutally murdered by an unknown assassin while talking with the party.$$
);

INSERT INTO npc(name, surname, status, description)
VALUES ('Edric'
        ,'Vale'
        ,'alive'
        ,$$He is a politician the party met during their travels. He wants to ensure the city is safe and the laws are followed. If this safety is also granted to the lower classes of the city isn't really clear.$$
);

INSERT INTO npc_modal(npc_id, modal_title, flavor_quote, modal_content)
VALUES ((SELECT id FROM npc WHERE name = 'Marice' AND surname = 'Holden')
        , 'Assassination report'
        , $$"Hey mister Holden, I found some information about Edric..." ~Silas Ashenblood"$$
        ,$$After that sentence was said, a crossbow bolt flew straight through mister Holden's head.$$
);

INSERT INTO npc_modal(npc_id, modal_title, flavor_quote, modal_content)
VALUES ((SELECT id FROM npc WHERE name = 'Edric' AND surname = 'Vale')
        ,'View Secrets'
        ,$$"Knowledge is the only currency that never devalues in this city."$$
        ,$$The box is empty and has sentimental value to Edric, but he kept this from the party.$$
);

INSERT INTO npc_modal(npc_id, modal_title, flavor_quote)
VALUES((SELECT id FROM npc WHERE name = 'Lissandra' AND surname = 'Vale')
        ,'Visit Kitchen'
        ,$$"We've got to have each other's backs in these parts of the city."$$
);

INSERT INTO worldbuilding(title, subtitle, description)
VALUES ('The City'
        ,'Populace'
        ,$$This is the first city the players have visited as a party. It consists mostly of humans (50%), with elves (20%) following after. The rest (30%) is made up of various races ranging from dwarves to orcs and goblins. These races, however, do not fit in perfectly with the humans, as there is a fair share of xenophobia coming from the human populace.$$
);

INSERT INTO worldbuilding(title, description)
VALUES ('The High Plaza'
        ,$$Built upon ancient white stone and powered by the Great River, The City is a monument to ingenuity. Clockwork waterwheels drive the workshops of master alchemists. This part of the metropolis is where the richest reside in their beautiful mansions of marble.$$
);


INSERT INTO worldbuilding(title, description)
VALUES ('The Outskirts'
        ,$$But beauty has a price. Beneath the High Plaza lies a labyrinth of timber tenements where survival is the only science that matters. The outskirts are filled with criminals gathered in organizations and gangs. The real danger isn't the criminality however, it's the corruption spreading through the guard corps.$$
);

