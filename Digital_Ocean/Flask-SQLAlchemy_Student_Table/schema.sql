/* schema.sql */

DROP TABLE IF EXISTS student;

CREATE TABLE student (
        id INTEGER NOT NULL, 
        firstname VARCHAR(100) NOT NULL, 
        lastname VARCHAR(100) NOT NULL, 
        email VARCHAR(80) NOT NULL, 
        age INTEGER, 
        created_at DATETIME DEFAULT (CURRENT_TIMESTAMP), 
        bio TEXT, 
        PRIMARY KEY (id), 
        UNIQUE (email)
);

