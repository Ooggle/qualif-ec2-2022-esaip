CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS gallery (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userID TEXT NOT NULL,
    file_name TEXT NOT NULL,
    file_length TEXT NOT NULL,
    file_content TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES ("flag_is", "R2Lille{SQL1_4r3_3v3ryWh3R3}");
