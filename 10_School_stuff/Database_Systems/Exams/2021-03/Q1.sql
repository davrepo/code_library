-- (a)
SELECT COUNT(*)
FROM Vaccines V
JOIN Diseases D ON V.disID = D.ID
WHERE D.name = 'Coronavirus';

-- (b)
SELECT COUNT(DISTINCT peoID)
FROM Injections I
JOIN Vaccines V ON I.vacID = V.ID
JOIN Diseases D ON V.disID = D.ID
JOIN Categories C ON D.catID = C.ID
WHERE D.curable = TRUE AND C.name = 'Bone diseases';

-- (c)
SELECT V1.ID
FROM Vaccines V1
JOIN Diseases D1 ON V1.disID = D1.ID
WHERE D1.name = 'Coronavirus' AND V1.effectyears >= ALL (
  SELECT V2.effectyears
  FROM Vaccines V2
  JOIN Diseases D2 ON V2.disID = D2.ID
  WHERE D2.name = 'Coronavirus'
);

-- (d)
-- ****** NOT IN ******
select count(*)
from diseases D
where D.ID not in (
	select V.disID 
	from vaccines V
	group by V.disID
	having count(*) >= 5
);

-- (e)
SELECT COUNT(DISTINCT I.peoID) AS num_people
FROM Injections I
JOIN Vaccines V ON I.vacID = V.ID
JOIN Diseases D ON V.disID = D.ID
WHERE D.name = 'Coronavirus' AND I.injectionyear + V.effectyears >= 2021;

-- (f)
select ((select count(*) from injections) 
	 /  (select count(*) from people)) as X;

-- (g)
SELECT COUNT(*) 
FROM (
  SELECT I.peoID
  FROM Injections I
  JOIN Vaccines V ON I.vacID = V.ID
  JOIN Diseases D ON V.disID = D.ID
  JOIN Categories C ON D.catID = C.ID
  GROUP BY I.peoID
  HAVING COUNT(DISTINCT C.ID) = (SELECT COUNT(*) FROM Categories)
) AS Subquery;

-- (h)
drop view if exists q1h_b;
drop view if exists q1h_a;

create view q1h_a
as
select P.ID as PID, D.ID as DID, P.birthyear, count(distinct V.ID) as vacnum
from people P
	join injections I on P.ID = I.peoID
	join vaccines V on I.vacID = V.ID
	join diseases D on V.disID = D.ID
	join categories C on C.ID = D.catID
where C.name = 'Immune diseases'
	and D.curable = true
group by P.ID, D.ID;

create view q1h_b
as
select Q.PID, Q.birthyear
from q1h_a Q
where Q.vacnum = (select max(Q1.vacnum) from q1h_a Q1);

select Q.PID
from q1h_b Q
where Q.birthyear = (select min(Q1.birthyear) from q1h_b Q1);
-- 422
