CREATE VIEW aircraft_group_count AS
SELECT ag, COUNT(*) AS members
FROM aircraft
GROUP BY ag;

SELECT MAX(members)
FROM aircraft_group_count;

