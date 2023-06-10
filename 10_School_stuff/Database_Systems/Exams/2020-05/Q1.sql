-- (a)
SELECT COUNT(*)
FROM Places
WHERE name LIKE '%lev';

-- (b)
SELECT ID
FROM Places
WHERE population = (
    SELECT MAX(population)
    FROM Places
);

-- (c)
SELECT COUNT(*)
FROM (
    SELECT teamID
    FROM TeamsInDivisions
    GROUP BY teamID
    HAVING COUNT(divisionID) > 1
) AS multiple_divisions;

-- (d)
SELECT COUNT(distinct T.ID)
FROM TeamsInDivisions TID
JOIN Teams T ON TID.teamID = T.ID
JOIN Divisions D ON TID.divisionID = D.ID
WHERE T.genderID <> D.genderID;

-- (e)
SELECT P.ID
FROM Places P
JOIN Clubs C ON P.ID = C.placeID
JOIN Teams T ON C.ID = T.clubID
JOIN Genders G ON T.genderID = G.ID
WHERE G.gender = 'M'
GROUP BY P.ID
HAVING COUNT(T.ID) = (
    SELECT MAX(team_count)
    FROM (
        SELECT P.ID AS place_id, COUNT(T.ID) AS team_count
        FROM Places P
        JOIN Clubs C ON P.ID = C.placeID
        JOIN Teams T ON C.ID = T.clubID
        JOIN Genders G ON T.genderID = G.ID
        WHERE G.gender = 'M'
        GROUP BY P.ID
    ) AS subquery
);


-- (f)
SELECT COUNT(*)
FROM (
    SELECT P.ID
    FROM Places P
    JOIN Clubs C ON P.ID = C.placeID
    JOIN Teams T ON C.ID = T.clubID
    GROUP BY P.ID
    HAVING COUNT(DISTINCT T.genderID) = (SELECT COUNT(*) FROM Genders)
) AS all_gender_places;

-- (g)
SELECT COUNT(*)
FROM (
    SELECT C.ID
    FROM Clubs C
    JOIN Teams T ON C.ID = T.clubID
    JOIN TeamsInDivisions TID ON T.ID = TID.teamID
    JOIN Divisions D ON TID.divisionID = D.ID
    JOIN Genders G ON D.genderID = G.ID
    WHERE G.gender = 'M'
    GROUP BY C.ID
    HAVING COUNT(DISTINCT D.ID) = (
        SELECT COUNT(*)
        FROM Divisions D2
        JOIN Genders G2 ON D2.genderID = G2.ID
        WHERE G2.gender = 'M'
    )
) AS all_m_division_clubs;

-- (h) - Own solution wrong, here so exam solution
-- supporting view
drop view if exists TeamsWithPoints;
create view TeamsWithPoints
as 
select ID, sum(points) as points
from (
	select T.ID, sum(S.homepoints) as points
	from Teams T
		join Matches M on T.ID = hometeamID
		join Sets S on M.ID = S.matchID
	group by T.ID
	union all
	select T.ID, sum(S.awaypoints) as points
	from Teams T
		join Matches M on T.ID = awayteamID
		join Sets S on M.ID = S.matchID
	group by T.ID
) X
group by ID;

-- 268
select *
from TeamsWithPoints 
where ID = 0;

-- 1637
select max(points)
from TeamsWithPoints;
