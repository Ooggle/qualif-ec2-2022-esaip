CREATE TABLE IF NOT EXISTS report (
    session TEXT NOT NULL UNIQUE,
    url TEXT NOT NULL
);
