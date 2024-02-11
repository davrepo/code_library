-- (a)
SELECT COUNT(*)
FROM plants p
JOIN families f ON p.familyID = f.ID
WHERE f.name = 'Thespesia';

-- (b)
SELECT COUNT(*)
FROM people p
WHERE p.position = 'Planter' AND p.ID NOT IN (
    SELECT DISTINCT planterID
    FROM plantedin
);

-- (c)
SELECT ROUND(SUM(1.0 * fb.size * pi.percentage / 100), 2) as total_area
FROM plantedin pi
JOIN flowerbeds fb ON pi.flowerbedID = fb.ID
JOIN plants p ON pi.plantID = p.ID
JOIN families f ON p.familyID = f.ID
WHERE f.name = 'Vicia';

-- (d)
WITH OverfilledFlowerbeds AS (
    SELECT fb.ID, SUM(pi.percentage) AS total_percentage
    FROM flowerbeds fb
    JOIN plantedin pi ON fb.ID = pi.flowerbedID
    GROUP BY fb.ID
    HAVING SUM(pi.percentage) > 100
)
SELECT ID
FROM OverfilledFlowerbeds
WHERE total_percentage = (
    SELECT MAX(total_percentage)
    FROM OverfilledFlowerbeds
);

-- Create the view
DROP VIEW IF EXISTS OverfilledFlowerbeds;
CREATE VIEW OverfilledFlowerbeds AS (
    SELECT fb.ID, SUM(pi.percentage) AS total_percentage
    FROM flowerbeds fb
    JOIN plantedin pi ON fb.ID = pi.flowerbedID
    GROUP BY fb.ID
    HAVING SUM(pi.percentage) > 100
);

-- Use the view to find the most overfilled flowerbed(s)
SELECT ID
FROM OverfilledFlowerbeds
WHERE total_percentage = (
    SELECT MAX(total_percentage)
    FROM OverfilledFlowerbeds
);

-- (e)
select count(*)
from flowerbeds B
WHERE B.ID NOT IN (
	SELECT plantedin.flowerbedid
	FROM plantedin
	GROUP BY plantedin.flowerbedid
	HAVING SUM(plantedin.percentage) >= 100
);


-- (f)
SELECT COUNT(DISTINCT fb.ID)
FROM flowerbeds fb
JOIN plantedin pi ON fb.ID = pi.flowerbedID
JOIN plants p ON pi.plantID = p.ID
JOIN families f ON p.familyID = f.ID
JOIN types t ON f.typeID = t.ID
WHERE t.name = 'shrub' AND (SELECT SUM(pi2.percentage) FROM plantedin pi2 WHERE pi2.flowerbedID = fb.ID) < 100;

-- (g)
-- Create a view for planters who planted a plant of type 'flower' in the park 'Kongens Have'
DROP VIEW IF EXISTS PlantersInKongensHave;
CREATE VIEW PlantersInKongensHave AS
SELECT DISTINCT p.ID, p.name
FROM people p
JOIN plantedin pi ON p.ID = pi.planterID
JOIN plants pl ON pi.plantID = pl.ID
JOIN families f ON pl.familyID = f.ID
JOIN types t ON f.typeID = t.ID
JOIN flowerbeds fb ON pi.flowerbedID = fb.ID
JOIN parks pk ON fb.parkID = pk.ID
WHERE p.position = 'Planter' AND t.name = 'flower' AND pk.name = 'Kongens Have';

-- Calculate the total area planted by these planters without the previous restrictions
create view alldata
as
select E.ID, E.name, T.name as type, K.name as park, E.position, 1.0 * B.size * I.percentage / 100 as sqm
from people E
	join plantedin I on E.ID = I.planterID
	join flowerbeds B on B.ID = I.flowerbedID
	join parks K on K.ID = B.parkID
	join plants P on P.ID = I.plantID
	join families F on F.ID = P.familyID
	join types T on T.ID = F.typeID;

select A.ID, A.name, sum(A.sqm)
from alldata A
group by A.ID, A.name
having A.ID in (
	select A2.ID
	from alldata A2
	where A2.type = 'flower'
		and A2.park = 'Kongens Have'
		and A2.position = 'Planter'
)
order by sum(A.sqm) desc;
-- First 5 rows:
-- 154	"Frank Jansen"	72.82
-- 110	"Jan Lauridsen"	72.04999999999998
-- 48	"Johan Mikaelsen"	70.41999999999999
-- 142	"Mikael Lauritz"	67.52999999999999
-- 156	"Mikael Mikaelsen"	67.47



-- (h)



