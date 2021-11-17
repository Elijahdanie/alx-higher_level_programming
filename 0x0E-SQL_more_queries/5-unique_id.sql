-- Creates a table with id column  with unique id
CREATE TABLE IF NOT EXISTS unique_id(
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256)
)
