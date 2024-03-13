-- Cities of california
SELECT * FROM cities where state_id in (SELECT id FROM states WHERE name = "California") ORDER BY id;
