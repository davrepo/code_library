SELECT * FROM cities;
SELECT * FROM continents;
SELECT * FROM countries;
SELECT * FROM countries_continents;
SELECT * FROM countries_languages;
SELECT * FROM empires;

-- a) find number of countries in empires where empire is Iberian
select count(*)
from empires E
where E.Empire = 'Iberian';
-- output: 3

-- b) find country in countries_continents, 
-- where for countrycode there is >1 continent entry
SELECT countrycode 
FROM countries_continents 
GROUP BY countrycode 
HAVING COUNT(*) > 1;

SELECT COUNT(*) FROM countries_continents
WHERE countrycode IN (
    SELECT countrycode 
    FROM countries_continents 
    GROUP BY countrycode 
    HAVING COUNT(*) > 1
    )
AND continent = 'Europe';
-- output: 2

-- alternative solution, better:
select count(*)
from countries_continents
where percentage < 100 and continent = 'Europe';

-- c) In countries of North America with >1 mllion inhabitants, 
-- find number of people that speak Spanish
SELECT SUM(population) FROM countries_languages
WHERE countrycode IN (SELECT countrycode FROM countries WHERE continent = 'North America' AND population > 1000000);

SELECT SUM(population * countries_languages.percentage / 100)
FROM countries_continents
JOIN countries ON countries_continents.countrycode = countries.code
JOIN countries_languages ON countries.code = countries_languages.countrycode
WHERE countries_continents.Continent = 'Europe' AND countries.population > 1000000 AND countries_languages.language = 'Spanish';
-- output: 29634696

-- d) find number of languages spoken in all countries of "Danish Empire" in empire
SELECT COUNT(*) FROM (
SELECT language FROM countries_languages
WHERE countrycode IN (SELECT countrycode FROM empires WHERE empire = 'Benelux')
GROUP BY language
HAVING COUNT(DISTINCT countrycode) = (SELECT COUNT(*) FROM empires WHERE empire = 'Benelux')
) AS tmp;
-- output: 2

