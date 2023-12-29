/* schema.sql */

DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS comment;

CREATE TABLE IF NOT EXISTS post (
        id INTEGER NOT NULL, 
        title VARCHAR(100), 
        content TEXT, 
        created_at DATETIME DEFAULT (CURRENT_TIMESTAMP), 
        PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS comment (
        id INTEGER NOT NULL, 
        content TEXT,
        created_at DATETIME DEFAULT (CURRENT_TIMESTAMP),
        post_id INTEGER,
        PRIMARY KEY (id), 
        FOREIGN KEY(post_id) REFERENCES post (id)
);
