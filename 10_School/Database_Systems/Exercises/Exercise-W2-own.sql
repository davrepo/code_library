-- Question 1:
SELECT name, record
FROM sports
ORDER BY name;

-- Question 2: ?? Compare to Solution?
SELECT sports.name
FROM sports
	LEFT JOIN results ON sports.id = results.sportid
WHERE results.result IS NOT NULL
GROUP BY sports.name
HAVING COUNT(*) >= 1;


select distinct name 
from Sports S join Results R on S.ID = R. sportID; 


-- Question 3:
SELECT COUNT(*)
FROM (
	SELECT peopleid, COUNT(*)
	FROM results
	GROUP BY peopleid
) AS tmp;


SELECT COUNT(DISTINCT results.peopleid)
FROM results

-- Question 4:
SELECT results.peopleid, people.name
FROM results
	JOIN people ON results.peopleid = people.id
GROUP BY results.peopleid, people.name
HAVING COUNT(*) >= 20;


select P.ID, P.name
from People P 
	join Results R on P.ID = R.peopleID
group by P.ID
having count(*) >= 20;


-- Question 5:
-- people.id, people.name, gender.description
SELECT DISTINCT people.id, people.name, gender.description
FROM people
	JOIN gender ON people.gender = gender.gender
	JOIN results ON people.id = results.peopleid
	JOIN sports ON sports.id = results.sportid
WHERE results.result = sports.record;

-- Question 6:
SELECT sports.name, COUNT(DISTINCT results.peopleID) as numatheletes
FROM results
	JOIN sports ON sports.id = results.sportid
WHERE results.result = sports.record
GROUP BY sports.id;


-- Question 7:
SELECT people.id, people.name, MAX(results.result) AS best, 
	(sports.record - MAX(results.result))::numeric(10,2) AS difference
FROM people
	JOIN results ON people.id = results.peopleid
	JOIN sports ON results.sportid = sports.id
WHERE sports.name = 'Triple Jump'
GROUP BY people.id, people.name, sports.record
HAVING COUNT(*) >= 20;


select P.ID, P.name, max(R.result) as best, 
	to_char(S.record-max(R.result), '0D99') as difference
from People P 
	join Results R on P.ID = R.peopleID 
	join Sports S on S.ID = R.sportID
where S.name = 'Triple Jump'
group by P.ID, P.name, S.record
having count(*) >= 20;


-- Question 8:
SELECT DISTINCT people.id, people.name, gender.description
FROM people
	JOIN gender ON people.gender = gender.gender
	JOIN results ON people.id = results.peopleid
	JOIN competitions ON competitions.id = results.competitionid
WHERE EXTRACT(YEAR FROM competitions.held) = 2009 AND competitions.place = 'Hvide Sande';


-- Question 9:
SELECT people.name, gender.description
FROM people
	JOIN gender ON people.gender = gender.gender
WHERE name LIKE '% J%sen'


-- Question 10:
SELECT people.name, sports.name, results.result, sports.record,
	CASE 
		WHEN results.result IS NOT NULL
		THEN TO_CHAR(100*results.result/sports.record, '990D99%')
		ELSE NULL
	END 
	AS percentage
FROM people
	JOIN results ON people.id = results.peopleid
	JOIN sports ON sports.id = results.sportid;


-- Question 11:
SELECT COUNT(DISTINCT results.peopleid)
FROM people
JOIN results ON people.id = results.peopleid
WHERE result IS NULL;


SELECT COUNT(DISTINCT results.peopleid)
FROM results
WHERE results.result IS NULL;


-- Question 12:
SELECT sports.id, sports.name, MAX(results.result) as maxres
FROM sports
	JOIN results ON sports.id = results.sportid
GROUP BY sports.id, sports.name
ORDER BY sports.id;


-- Question 13:
SELECT people.id, people.name, COUNT(*) AS num_records
FROM people
	JOIN results ON people.id = results.peopleid
	JOIN sports ON sports.id = results.sportid
WHERE results.result = sports.record
GROUP BY people.id, people.name
HAVING COUNT(DISTINCT sports.id) >= 2;


-- Question 14:
--- Self Select Local Maximum
--- Slow
select R.sportid, R.result
from Results R
where R.result = (
    select max(R1.result)
    from Results R1
    where R1.sportID = R.sportID
) ORDER BY R.sportid;

--- Fast
SELECT R.sportid, R.peopleid, R.result
FROM Results R
JOIN (
    SELECT sportID, MAX(result) AS max_result
    FROM Results
    GROUP BY sportID
) AS MR ON R.sportID = MR.sportID AND R.result = MR.max_result
ORDER BY R.sportid;

---- Final
-- Subquery
select distinct P.ID, P.name, P.height, R.result, S.name, 
	case (R.result = S.record) when true then 'Yes' else 'No' end as "record?"
from People P, Results R, Sports S
where P.ID = R.peopleID
  and S.ID = R.sportID
  -- IN subquery
  and (S.ID, R.result) IN (		
    select R1.sportID, max(R1.result)
    from Results R1
    group by R1.sportID
);

-- Group BY
SELECT DISTINCT P.id, P.name, P.height, R.result, S.name as sport_name,
	CASE (R.result = S.record) WHEN TRUE THEN 'Yes' ELSE 'No' END AS "record?"
FROM Results R
	JOIN (
		SELECT sportID, MAX(result) AS max_result
		FROM Results
		GROUP BY sportID
	) AS MR ON R.sportID = MR.sportID AND R.result = MR.max_result
	JOIN people P ON P.id = R.peopleid
	JOIN sports S ON S.id = R.sportid
ORDER BY S.name;


-- Question 15:
SELECT people.id, people.name, comp.competitionid
FROM people
LEFT JOIN (
	SELECT *
	FROM results
	JOIN competitions ON results.competitionid = competitions.id
) AS comp ON people.id = comp.peopleid
WHERE comp.competitionid IS NULL;


select P.ID, P.name
from People P
where not exists (
    select *
    from Results R
    where R.peopleID = P.ID
);


-- Question 16:
SELECT people.id, people.name
FROM people
	JOIN results ON results.peopleid = people.id
	JOIN competitions ON competitions.id = results.competitionid
WHERE EXTRACT(YEAR FROM competitions.held) = 2002 
	AND EXTRACT(MONTH FROM competitions.held) = 6
UNION
SELECT people.id, people.name
FROM people
	JOIN results ON results.peopleid = people.id
	JOIN sports ON sports.name = 'High Jump' AND results.result = sports.record


-- Question 17:
SELECT people.ID, people.name
FROM people
    JOIN results on results.peopleid = people.id
    JOIN sports on results.sportid = sports.id
WHERE results.result = sports.record
AND people.id IN (
    SELECT P.ID
    FROM People P
        JOIN Results R ON R.peopleID = P.ID
    GROUP BY P.ID
	-- DISTINCT is critical here
    HAVING COUNT(DISTINCT sportID) = 1);


-- Question 18:
SELECT COUNT(*)
FROM (
  SELECT people.id
  FROM people
    JOIN results ON results.peopleid = people.id
    JOIN competitions ON competitions.id = results.competitionid
  GROUP BY people.id
  HAVING COUNT(DISTINCT competitions.place) >= 10
) AS tmp;


--- very elegant solution
select count( P.ID ) as num
from People P
-- will return TRUE or FALSE
where 10 <= (
    select count(distinct C.place)
    from Results R 
        join Competitions C on R.competitionID = C.ID
    where R.peopleID = P.ID
);


-- Question 19: (DIVISION)
--- DIVISION ---
SELECT people.id
FROM people
	JOIN results ON results.peopleid = people.id
	JOIN sports ON sports.id = results.sportid
WHERE results.result = sports.record
GROUP BY people.id
HAVING COUNT(DISTINCT sports.id) = (SELECT COUNT(S.id) FROM sports S)


-- Question 20:
SELECT DISTINCT sports.id, sports.name, sports.record, results.result
FROM results
	JOIN sports ON sports.id = results.sportid
	JOIN (
		SELECT R.sportid, MIN(R.result) AS min_result
		FROM results R
		GROUP BY R.sportid
	) AS minR ON results.sportid = minR.sportid AND results.result = minR.min_result
WHERE sports.id IN (
	-- sportid with where held at every place
	SELECT S.id
	FROM sports S
		JOIN results R ON R.sportid = S.id
		JOIN competitions C ON R.competitionid = C.id
	GROUP BY S.id
	-- Division
	HAVING COUNT(DISTINCT C.place) = (
		SELECT COUNT(DISTINCT competitions.place)
		FROM competitions)
)


select 	S.ID, S.name, S.record, min(R.result)
from Sports S
    join Results R on S.ID = R.sportID
where not exists ( 
    select C.place 
    from Competitions C
    where not exists (
        select *
        from Results R1
        where R1.competitionID = C.ID
          and R1.sportID = S.ID))
group by S.ID, S.name, S.record;


