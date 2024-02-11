-- Question 1:
-- The person relation contains 51,052 entries with a registered gender. 
-- How many records are there with gender ’f’?

-- where gender is not null
SELECT COUNT(*) FROM person WHERE gender IS NOT NULL;
SELECT COUNT(*) FROM person WHERE gender = 'f';

-- Question 2:
-- Use involved, JOIN movie and person, to find the number of movies where the average of person.height > 195
SELECT COUNT(*) FROM (
    SELECT involved.movieid
    FROM involved
    JOIN person ON involved.personid = person.id
    GROUP BY involved.movieid
    HAVING AVG(person.height) > 195
) tmp;

-- Question 3:
-- movie_genre table, has colume movieid and genre. 
-- in each movieid, there are multiple genres
-- select movieid, genre from movie_genre where there are duplicate genre in each movieid
-- find movieid with highest number of genre duplicates
SELECT movieid, genre, COUNT(*) AS count
FROM movie_genre
GROUP BY movieid, genre
HAVING COUNT(*) > 1
ORDER BY count DESC
LIMIT 1

-- Question 4:
-- involved has columns, peronid (int), movieid (int), role (char)
-- find personid of 'Roger Spottiswoode'
-- find movies that 'Roger Spottiswoode' directed
-- find all distinct actors in those movies
-- find the number of distinct actors
SELECT COUNT(DISTINCT personid) FROM (
    SELECT personid FROM involved
    WHERE movieid IN (
        SELECT movieid FROM involved
        WHERE personid = (
            SELECT id FROM person
            WHERE name = 'Roger Spottiswoode' 
        ) AND role = 'director'
    )
    AND role = 'actor'
) tmp;

-- Question 5:
-- movie has columns, id (int)
-- involved has columns, peronid (int), movieid (int), role (char)
-- find movies where year is 2002 not in involved
SELECT COUNT(*) FROM movie
WHERE id NOT IN (
    SELECT movieid FROM involved
) AND year = 2011;

-- Question 6: (603)
-- select personid, movieid, role from involved where role = 'director'
-- then find matching personid, movieid, role from involved where role = 'actor'
-- count the number of peronid repeats, where there is only one repeat
-- Trial - tested output (603)
SELECT COUNT(*) FROM (
	SELECT personid, COUNT(*) AS appearances
	FROM (
		SELECT personid, movieid FROM involved
		WHERE role = 'director'
		INTERSECT
		SELECT personid, movieid FROM involved
		WHERE role = 'actor'
	) tmp
	GROUP BY personid
	HAVING COUNT(*) = 1
) tmp;

-- final code:
SELECT personid, COUNT(*) AS appearances
FROM (
    SELECT personid, movieid FROM involved
    WHERE role = 'director'
    INTERSECT
    SELECT personid, movieid FROM involved
    WHERE role = 'actor'
) tmp
GROUP BY personid
ORDER BY appearances DESC
LIMIT 1;

-- Question 7:
-- movie has column id (int), year (int)
-- involved has columns, peronid (int), movieid (int), role (char)
-- roles has columns, id (int), role (char)
-- Of all the movies produced in 2002, how many have entries registered in involved 
-- for all roles defined in the roles relation.
-- Use Relational devision

-- Test code (282)
SELECT COUNT(*)
FROM (
    SELECT id
    FROM movie
    WHERE year = 2002
    AND id IN (
        SELECT movieid
        FROM involved
        GROUP BY movieid
        HAVING COUNT(DISTINCT role) = (SELECT COUNT(*) FROM role)
    )
) AS tmp;

-- Final code
SELECT COUNT(*)
FROM (
    SELECT id
    FROM movie
    WHERE year = 2011
    AND id IN (
        SELECT movieid
        FROM involved
        GROUP BY movieid
        HAVING COUNT(DISTINCT role) = (SELECT COUNT(*) FROM role)
    )
) AS tmp;

-- Question 8:
-- movie_genre has columns id (int), movieid (int), genre (char)
-- genre has columns id (int), genre (char), category (char)
-- involved has columns, peronid (int), movieid (int), role (char)
-- How many people have played a role in movies of all genres in category 'Newsworthy'? (156)

-- Test code (156)
SELECT DISTINCT involved.personid as num_people, COUNT(movie_genre.genre)
FROM involved
JOIN movie_genre ON involved.movieid = movie_genre.movieid
AND movie_genre.genre IN (
    SELECT genre
    FROM genre
    WHERE category = 'Newsworthy'
)
GROUP BY involved.personid
HAVING COUNT(DISTINCT movie_genre.genre) = (
    SELECT COUNT(*) FROM genre WHERE category = 'Newsworthy'
);

-- Final code
SELECT COUNT(*)
FROM (
	SELECT DISTINCT involved.personid as num_people, COUNT(movie_genre.genre)
	FROM involved
	JOIN movie_genre ON involved.movieid = movie_genre.movieid
	AND movie_genre.genre IN (
		SELECT genre
		FROM genre
		WHERE category = 'Popular'
	)
	GROUP BY involved.personid
	HAVING COUNT(DISTINCT movie_genre.genre) = (
		SELECT COUNT(*) FROM genre WHERE category = 'Popular'
	)
) AS tmp;
