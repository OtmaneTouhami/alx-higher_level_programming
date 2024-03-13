-- Cities of california
SELECT id, name FROM cities where state_id in (SELECT id FROM states WHERE name = "California")
