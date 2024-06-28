-- File: 9-cities_by_state_join.sql

USE hbtn_0d_usa;

SELECT cities.id, cities.name AS city_name, states.name AS state_name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
