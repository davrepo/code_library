SELECT * FROM accountrecords;
SELECT * FROM accounts;
SELECT * FROM bills;
SELECT * FROM people;

-- Slide 2: Show ID and name of all female (‘F’) customers who have 
--     an unpaid bill larger than the balance plus 
--     overdraft allowance on one of their accounts.
select distinct P.PID, P.pName
from People P
	join Accounts A on P.PID = A.PID
	join Bills B on P.PID = B.PID
where P.pGender = 'F'
  and not B.bIsPaid
  and B.bAmount > A.aBalance + A.aOver;

-- Slide 3: Show ID and name of all male (‘M’) customers who 
--     have an unpaid bill that is larger than their total balance 
--     (not including overdraft allowance), along with the ID of the bill.
select distinct P.PID, P.pName, B.BID, B.bAmount, sum(A.aBalance)
from People P
	join Accounts A on P.PID = A.PID
	join Bills B on P.PID = B.PID
where P.pGender = 'M'
  and not B.bIsPaid
group by P.PID, P.pName, B.BID, B.bAmount
having B.bAmount > sum(A.aBalance)
order by P.PID, B.BID;

-- Slide 5 (UNION): Show ID and name of people that are taller than 1.75
--     **OR** have an account with a negative balance
select P.PID, P.pName
from People P
where P.pHeight > 1.75
union
select P.PID, P.pName
from People P join Accounts A on P.PID = A.PID
where A.aBalance < 0;

-- Using ORDER BY to get ID order
select P.PID, P.pName
from (
	select P.PID, P.pName
	from People P
	where P.pHeight > 1.75
	union
	select P.PID, P.pName
	from People P join Accounts A on P.PID = A.PID
	where A.aBalance < 0) P
order by P.PID;

-- Union is the same as OR ... IN
select P.PID, P.pName
from People P
where P.pHeight > 1.75
or P.PID in (
	select P.PID
	from People P join Accounts A on P.PID = A.PID
	where A.aBalance < 0
);

-- Solution(own): there are people that do not have account, so need to use left join
SELECT DISTINCT people.pid, people.pname
FROM people
LEFT JOIN accounts ON people.pid = accounts.pid
WHERE people.pheight > 1.75
	OR accounts.abalance < 0


-- Slide 7 (INTERSECT): Show ID and name of people who are female and 
--     hold an account record with amount > 10000
select P.PID, P.pName
from People P
where P.pGender = 'F'
INTERSECT
select P.PID, P.pName
from People P
	join Accounts A on P.PID = A.PID
	join AccountRecords R on R.AID = A.AID
where R.rAmount > 10000;

-- Intersect is the same as AND ... IN
select P.PID, P.pName
from People P
where P.pGender = 'F'
AND P.PID IN (
	select P.PID
	from People P
		join Accounts A on P.PID = A.PID
		join AccountRecords R on R.AID = A.AID
	where R.rAmount > 10000
);

-- Solution(own)
SELECT DISTINCT people.pid, people.pName
FROM people
LEFT JOIN accounts ON people.pid = accounts.pid
JOIN accountrecords ON accounts.aid = accountrecords.aid
WHERE pgender = 'F' AND accountrecords.ramount > 10000;


-- Slide 9 (EXCEPT):
select P.PID, P.pName
from People P
where P.pName like 'B%'
except
select P.PID, P.pName
from People P join Bills B on P.PID = B.PID
where not B.bIsPaid;

-- Except is the same as AND ... NOT IN
select P.PID, P.pName
from People P
where P.pName like 'B%'
  and P.PID not in (
	select P.PID
	from People P
		join Bills B on P.PID = B.PID
	where not B.bIsPaid );

-- WRONG solution(own):
SELECT DISTINCT ON (people.pid) people.pid, people.pname, bispaid
FROM people
LEFT JOIN bills ON people.pid = bills.pid
WHERE people.pname LIKE 'B%' AND 
	(bills.bIsPaid = 'true' OR bills.bIsPaid IS NULL);
-- This is wrong because if a person has multiple bills,
-- and some of them is paid, and some of them is not paid, then this person will be selected
-- just because one of the bills is paid. 
-- To illustrate, see below
SELECT *
FROM people
JOIN bills on bills.pid = people.pid
WHERE people.pid = 4



SELECT * FROM actors;
SELECT * FROM plays;
SELECT * FROM movies;
SELECT * FROM roles;

-- Slide 12: (DIVISION) ID and name of actors who have performed in movies based on all plays
select A.AID, A.aName
from Actors A
	join Roles R on A.AID = R.AID
	join Movies M on R.MID = M.MID
group by A.AID, A.aName
-- Division
having count(distinct M.PID) = (
	select count(*)
	from Plays
);

-- Of female actors …
-- Plays by Shakespeare
-- Movies produced in 2009
select A.AID, A.aName
from Actors A 
    join Roles R on R.AID = A.AID
    join Movies M on M.MID = R.MID
    join Plays P on M.PID = P.PID
where A.aGender = 'F'
  and P.pAuthor = 'Shakespeare'
  and M.mYear = 2009
group by A.AID, A.aName
having count(distinct M.PID) = (
    select count(*)
    from Plays P
    where P.pAuthor = 'Shakespeare' );


-- Slide 13: (DOUBLE NEGATION)
-- ID and name of actors who have performed in all plays
-- In other words, there is no play that has a movie that has a role that I have not played
select A.AID, A.aName
from Actors A
where not exists (
    select *
    from Plays P
    where not exists (
        select *
        from Roles R join Movies M on R.MID = M.MID
        where R.AID = A.AID
          and M.PID = P.PID));

-- Of female actors …
-- Produced in 2009
-- Plays by Shakespeare
select *
from Actors A
where A.aGender = 'F'
  and not exists (
    select *
    from Plays P
    where P.pAuthor = 'Shakespeare'
      and P.PID in (
        select M.PID 
        from Movies M 
        where M.mYear = 2009 )
      and not exists (  
        select *
        from Movies M join Roles R on M.MID = R.MID
        where R.AID = A.AID
          and M.PID = P.PID
          and M.mYear = 2009 ) );


-- Slide 14:
-- ID and name of actors who have had two roles in a movie at least twice
select A.AID, A.aName
from Actors A 
	join Roles R on A.AID = R.AID
group by A.AID, A.aName
having count(distinct R.MID) > 1;


-- Slide 15: Double Grouping
-- ID and name of actors who have had two roles in a movie at least twice
SELECT A1.aid, A1.aname
FROM (
	SELECT actors.aid, actors.aname, roles.mid
	FROM actors
		JOIN roles ON roles.aid = actors.aid
	GROUP BY roles.mid, actors.aid
	HAVING COUNT(*) > 1
	) A1
GROUP BY A1.aid, A1.aname
HAVING COUNT(*) > 1;
