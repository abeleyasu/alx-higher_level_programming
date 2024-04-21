-- Task: 16. List all records with a name value

-- Listing all records with a name value from table second_table
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
