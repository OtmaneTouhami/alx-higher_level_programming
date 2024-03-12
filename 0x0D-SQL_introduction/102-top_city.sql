-- top 3
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month IN ("JULY", "August ") GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
