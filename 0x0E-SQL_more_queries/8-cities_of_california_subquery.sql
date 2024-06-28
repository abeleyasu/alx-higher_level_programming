-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Query to select cities of California without using JOIN
SELECT * FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
