-- This lies all entries in secret_table whose name is not NULL
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
