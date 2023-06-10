-- (a)
SELECT COUNT(*)
FROM clubs C
JOIN cities CT ON C.cityID = CT.ID
WHERE CT.name = 'London';

-- (b)
SELECT COUNT(DISTINCT playerID)
FROM signedwith SW
WHERE SW.clubID NOT IN (SELECT ID FROM clubs);

-- (c)
SELECT COUNT(*)
FROM (
  SELECT awayID, COUNT(*) as away_wins
  FROM matches
  WHERE awaywin = true
  GROUP BY awayID
  HAVING COUNT(*) = 260
) AS clubs_with_most_away_wins;

-- (d)
SELECT SUM(awaygoals)
FROM matches M
JOIN signedwith SW ON M.awayID = SW.clubID AND M.seasonID = SW.seasonID
JOIN players P ON SW.playerID = P.ID
WHERE P.name = 'Steven Gerrard';

-- (e)
SELECT P.name
FROM players P
JOIN signedwith SW ON P.ID = SW.playerID
GROUP BY P.ID, P.name
HAVING COUNT(DISTINCT SW.clubID) = (
  SELECT MAX(club_count)
  FROM (
    SELECT COUNT(DISTINCT clubID) as club_count
    FROM signedwith
    GROUP BY playerID
  ) AS club_counts
);

-- (f)
SELECT COUNT(*)
FROM players P
WHERE P.ID NOT IN (
  SELECT DISTINCT SW.playerID
  FROM signedwith SW
  JOIN clubs C ON SW.clubID = C.ID
  JOIN cities CT ON C.cityID = CT.ID
  WHERE CT.name = 'London'
);

-- (g)
SELECT COUNT(*) FROM (
  SELECT M.awayID, M.seasonID
  FROM matches M
  JOIN clubs home_club ON M.homeID = home_club.ID
  JOIN cities home_city ON home_club.cityID = home_city.ID
  JOIN clubs away_club ON M.awayID = away_club.ID
  JOIN cities away_city ON away_club.cityID = away_city.ID
  WHERE home_city.name = 'London'
  AND away_city.name <> 'London'
  AND M.awaywin = TRUE
  GROUP BY M.awayID, M.seasonID
  HAVING COUNT(DISTINCT M.homeID) = (
    SELECT COUNT(*)
    FROM clubs C
    JOIN cities T ON C.cityID = T.ID
    WHERE T.name = 'London'
  )
) AS non_london_clubs;


-- (h)
SELECT C.name AS club_name, SUM(points) AS total_points
FROM (
  SELECT M.homeID AS clubID, 
         CASE 
           WHEN M.homegoals > M.awaygoals THEN 3
           WHEN M.homegoals = M.awaygoals THEN 1
           ELSE 0
         END AS points,
         M.seasonID
  FROM matches M
  UNION ALL
  SELECT M.awayID AS clubID, 
         CASE 
           WHEN M.awaygoals > M.homegoals THEN 3
           WHEN M.awaygoals = M.homegoals THEN 1
           ELSE 0
         END AS points,
         M.seasonID
  FROM matches M
) AS match_points
JOIN clubs C ON match_points.clubID = C.ID
WHERE match_points.seasonID = 2035
GROUP BY C.name
ORDER BY total_points DESC;
