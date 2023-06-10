-- (a)
SELECT COUNT(DISTINCT toID)
FROM Relationships;

-- (b)
SELECT COUNT(*) / 2
FROM Relationships R1
JOIN Relationships R2 ON R1.fromID = R2.toID AND R1.toID = R2.fromID;

-- (c)
SELECT COUNT(*) - COUNT(Ro.fromID)
FROM Relationships R
LEFT JOIN Roles Ro ON R.fromID = Ro.fromID AND R.toID = Ro.toID;

-- (d)
SELECT postID
FROM Comments
GROUP BY postID
HAVING COUNT(*) = (
SELECT MAX(comment_count)
FROM (
    SELECT postID, COUNT(*) AS comment_count
    FROM Comments
    GROUP BY postID
) AS Subquery);

-- (e)
-- Find all posts that have more than 2 comments, 
-- then subtract that number to get posts with 2 or fewer comments. 
SELECT COUNT(*)
FROM Posts
WHERE ID NOT IN (
    SELECT postID
    FROM Comments
    GROUP BY postID
    HAVING COUNT(ID) > 2
);

-- (f)
-- 90 different users who have commented on the post of their spouse.
-- How many diff municipalities have at least one user who has commented
-- on the post of their spouse?

-- 90
select count(distinct R.fromID)
from Roles R  
	join Comments C on R.toID = C.posterID and R.fromID = C.userID
where R.role = 'Spouse';

-- 33
select count(distinct Z.municipalityID)
from Zips Z
	join Users U on Z.zip = U.zip
	join Roles R on U.ID = R.fromID 
	join Comments C on R.toID = C.posterID and R.fromID = C.userID
where R.role = 'Spouse';

-- (g)
-- there are 3 diffrent roles in the database. 
-- There are 83 users who have a relationship (`fromID') 
-- to some other users with all the roles in the database.
-- How many users have some other user related to them (`toID') with
-- all the roles in the database?

-- 83
select count(distinct fromID)
from (
	select R.fromID, R.toID
	from Roles R
	group by R.fromID, R.toID
	having count(role) = (select count(distinct role) from Roles)
) X;

-- 86
select count(distinct toID)
from (
	select R.fromID, R.toID
	from Roles R
	group by R.fromID, R.toID
	having count(role) = (select count(distinct role) from Roles)
) X;

-- (h)
-- How many users have posted a post which has at least one like,
-- but no comments?

-- 206 = simplest student version, probably the most readable!
select count(distinct posterid)
from posts p
where p.id in (select postid from likes)
and p.id not in (select postid from comments)

-- 206 = readable version
select count(distinct posterID)
from (
	select P.ID, P.posterID
	from Posts P join Likes L on L.postID = P.ID
	except
	select P.ID, P.posterID
	from Posts P join Comments C on P.ID = C.postID
) X;