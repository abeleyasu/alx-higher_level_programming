-- Task: 15. List the number of records with the same score

-- Listing the number of records with the same score in table second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
