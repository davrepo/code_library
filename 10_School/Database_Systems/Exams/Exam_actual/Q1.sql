-- Schema:
DROP TABLE IF EXISTS Award;
CREATE TABLE Award (
  id INTEGER NOT NULL,
  contestId INTEGER DEFAULT NULL,
  description varchar(100) DEFAULT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Contest;
CREATE TABLE Contest (
  id INTEGER NOT NULL,
  edition varchar(10) DEFAULT NULL,
  name varchar(150) DEFAULT NULL,
  organizer varchar(50) DEFAULT NULL,
  year date DEFAULT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Dancer;
CREATE TABLE Dancer (
  id INTEGER NOT NULL,
  name varchar(150) DEFAULT NULL,
  email varchar(50) DEFAULT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS DancerAward;
CREATE TABLE DancerAward (
  dancerId INTEGER NOT NULL,
  awardId INTEGER NOT NULL,
  PRIMARY KEY (dancerId,awardId)
);

DROP TABLE IF EXISTS Rank;
CREATE TABLE Rank (
  dancerId INTEGER NOT NULL,
  contestId INTEGER NOT NULL,
  date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  level INTEGER DEFAULT NULL,
  rank INTEGER DEFAULT NULL,
  PRIMARY KEY (dancerId,contestId)
);

-- (a)
-- How many records in DancerAward have an award that does not exist?

SELECT * FROM danceraward;
SELECT * FROM award;

SELECT count(*)
FROM danceraward DA
LEFT JOIN award A on DA.awardID = A.id
WHERE A.id is null;

-- (b)
-- How many dancers have an email address with hotmail.com?
SELECT * FROM dancer;

SELECT * 
FROM dancer
WHERE email like '%@hotmail.com';

SELECT count(*)
FROM dancer
WHERE email like '%@hotmail.com';

SELECT count(*)
FROM dancer
WHERE email = '%@hotmail.com';

-- (7)
-- How many distinct dancers have a rank and an award in some contest organized by “DR’?

select count(distinct rank.dancerId)
from rank
join danceraward DA on rank.dancerId = DA.dancerId
join Award A on DA.awardId = A.id
where 
rank.contestId in (
    select id
    from contest
    where organizer = 'DR'
);
-- 233

select count(distinct rank.dancerId)
from rank
join danceraward DA on rank.dancerId = DA.dancerId
join Award A on DA.awardId = A.id
where rank.contestId = A.contestId and
rank.contestId in (
    select id
    from contest
    where organizer = 'DR'
);
-- 11

-- (9)
-- How many pairs of contests have the same name?
select count(*)
from (
    select *
    from contest C1
    join contest C2 on C1.id > C2.id
    where C1.name = C2.name
) as X;
-- 5

-- (11)
-- How many distinct dancers have an award, but not a rank, in a contest?
-- both c and f are correct
select count(distinct dancerId)
from danceraward DA
join award A on DA.awardId = A.id
where not exists (
	select *
	from rank R
	where DA.dancerId = R.dancerId and A.contestId = R.contestId
);
-- 486

select count(distinct dancerId)
from (
	select danceraward.dancerId, rank.contestId as rank, award.contestId as awd
	from danceraward
	join award on danceraward.awardId = award.Id
	left join rank on award.contestId = rank.contestId and danceraward.dancerId = rank.dancerId
) a
where rank is null;
-- 486

-- (13)
-- How many records have a rank lower than the average rank of all records in the relation?
SELECT avg(rank)
FROM rank;

select *
from rank
where rank = null;

select *
from rank
where level = null;

select *
from rank
where level <= 1;

select count(*)
from rank
where rank < (select avg(rank) from rank);
-- 969

select count(rank)
from rank
where rank < (select avg(rank) from rank);

-- (g)
-- How many dancers have participated in all contests editions named “Dance Forever”?
-- there is no context named dancer forever that I have no participated in

select distinct(id)
from dancer D
where not exists (
	select *
	from contest C
	where name = 'Dance Forever'
	and not exists (
		select *
		from rank R
		where D.Id = R.dancerId
	)
);
-- 494

select count(dancerId)
from (
	select dancerId
	from rank
	where contestId in (
		select id
		from contest
		where name like 'Dance Forever'	
	)
	group by dancerId
) X;
-- 24


select count(*)
from (
	select dancerId
	from rank
	where contestId in (
		select id
		from contest
		where name like 'Dance Forever'
	)
	group by dancerId
	having count(contestId) = (
		select count(*)
		from contest
		where name = 'Dance Forever'
	)
) X;
-- 24

-- (17)
-- How many contest names are used by two different organizers?
select count(*)
from (
	select count(distinct organizer)
	from contest
	group by name
	having count(distinct organizer) = 2
) X;
-- 5 


select count(*)
from (
	select count(distinct organizer)
	from contest
	group by name
	having count(organizer) = 2
) X;
