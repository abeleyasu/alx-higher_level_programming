-- Import the provided table dump into the hbtn_0c_0 database
USE hbtn_0c_0;
SOURCE '/home/user/Desktop/Download/cities.sql';

-- Calculate the average temperature by city and order the result by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp
FROM cities
GROUP BY city
ORDER BY avg_temp DESC;
