-- (a)
SELECT COUNT(*)
FROM Cars C
JOIN Models M ON C.modelID = M.ID
JOIN Makers MK ON M.makerID = MK.ID
WHERE MK.name = 'VOLVO';

-- (b)
SELECT COUNT(DISTINCT MK.ID)
FROM Sales S
JOIN Cars C ON S.carID = C.ID
JOIN Models M ON C.modelID = M.ID
JOIN Makers MK ON M.makerID = MK.ID
WHERE S.personID = 45;

-- (c)
SELECT makerID
FROM Models
GROUP BY makerID
HAVING COUNT(*) = (
  SELECT MAX(model_count)
  FROM (
    SELECT makerID, COUNT(*) AS model_count
    FROM Models
    GROUP BY makerID
  ) AS Subquery1
);

-- (d) --- WRONG
-- How many cars have been sold < 2 times  
-- (some have never been sold, must be included)
select count(*)
from cars C
where C.ID not in (
	select S.carID 
	from sales S
	group by S.carID
	having count(*) >= 2
);


-- (e)
SELECT C.licence
FROM Cars C
JOIN Sales S ON C.ID = S.carID
GROUP BY C.ID, C.licence
HAVING COUNT(*) = (
  SELECT MAX(sale_count)
  FROM (
    SELECT carID, COUNT(*) AS sale_count
    FROM Sales
    GROUP BY carID
  ) AS Subquery3
);

-- (f)
SELECT COUNT(DISTINCT personID)
FROM Sellers S1
WHERE NOT EXISTS (
  SELECT 1
  FROM Sellers S2
  WHERE S1.saleID = S2.saleID AND S1.personID <> S2.personID
);

SELECT COUNT(*)
FROM (
  SELECT S1.personID
  FROM Sellers S1
  LEFT JOIN Sellers S2 ON S1.saleID = S2.saleID AND S1.personID <> S2.personID
  WHERE S2.personID IS NULL
  GROUP BY S1.personID
) AS Subquery5;

-- (g)
SELECT COUNT(*)
FROM (
  SELECT S.personID
  FROM Sales S
  JOIN Cars C ON S.carID = C.ID
  JOIN Models M ON C.modelID = M.ID
  JOIN Makers MK ON M.makerID = MK.ID
  WHERE MK.name = 'VOLVO'
  GROUP BY S.personID
  HAVING COUNT(DISTINCT M.ID) = (
    SELECT COUNT(*)
    FROM Models
    WHERE makerID = (
      SELECT ID
      FROM Makers
      WHERE name = 'VOLVO'
    )
  )
) AS Subquery4;

-- (h) --- WRONG
SELECT COUNT(*)
FROM Cars C
JOIN Models M ON C.modelID = M.ID
JOIN Sales S ON C.ID = S.carID
WHERE C.prodyear < M.firstyear
   OR (M.lastyear IS NOT NULL AND C.prodyear > M.lastyear)
   OR S.saleyear < C.prodyear;

