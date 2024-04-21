-- Task: 11. List all records with a score >= 10

-- Listing all records with a score >= 10 from table second_table
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
