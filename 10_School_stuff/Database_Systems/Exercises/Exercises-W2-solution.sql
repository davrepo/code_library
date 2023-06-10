-- Query 1
select name, record 
from Sports
order by name;

-- Query 2
select distinct name 
from Sports S join Results R on S.ID = R. sportID; 

-- Query 3
select count(distinct R.peopleID)
from Results R; 

-- Query 4
select P.ID, P.name
from People P 
    join Results R on P.ID = R.peopleID
group by P.ID
having count(*) >= 20;

-- Query 5
select distinct P.ID, P.name, G.description
from People P 
	join Gender G on P.gender = G.gender
	join Results R on P.ID = R.peopleID 
	join Sports S on S.ID = R.sportID
where R.result = S.record;

-- Query 6
select S.name, count(distinct R.peopleID) as numathletes
from Results R 
    join Sports S on S.ID = R.sportID
where R.result = S.record
group by S.ID;

-- Query 7
select P.ID, P.name, max(R.result) as best, S.record-max(R.result) as difference
from People P 
	join Results R on P.ID = R.peopleID 
	join Sports S on S.ID = R.sportID
where S.name = 'Triple Jump'
group by P.ID, P.name, S.record
having count(*) >= 20;

select P.ID, P.name, max(R.result) as best, 
	to_char(S.record-max(R.result), '0D99') as difference
from People P 
	join Results R on P.ID = R.peopleID 
	join Sports S on S.ID = R.sportID
where S.name = 'Triple Jump'
group by P.ID, P.name, S.record
having count(*) >= 20;

-- Query 8
select distinct P.ID, P.name, G.description
from People P
	join Gender G on P.gender = G.gender
	join Results R on P.ID = R.peopleID
	join Competitions C on C.ID = R.competitionID
where C.place = 'Hvide Sande' and extract(year from C.held) = 2009;

-- Query 9
select P.name, G.description
from People P
	join Gender G on P.gender = G.gender
where P.name like '% J%sen';
	
-- Query 10
select P.name, S.name, 
	case when R.result is not null 
	then to_char(100*R.result/S.record, '990D99%') 
	else null 
	end as percentage
from People P 
	join Results R on P.ID = R.peopleID 
	join Sports S on S.ID = R.sportID;

-- Query 11
select count(distinct R.peopleID)
from Results R
where R.result is null;

-- Query 12
select S.ID, S.name, max(R.result) as maxres
from Sports S
    join Results R on S.ID = R.sportID
group by S.ID, S.name
order by S.ID;

-- Query 13
select P.ID, P.name, count(*)
from People P 
    join Results R on P.ID = R.peopleID
    join Sports S on S.ID = R.sportID
where R.result = S.record
group by P.ID, P.name
having count(distinct S.ID) > 1;

-- Query 14
select distinct P.ID, P.name, P.height, R.result, S.name, case (R.result = S.record) when true then 'Yes' else 'No' end as "record?"
from People P, Results R, Sports S
where P.ID = R.peopleID
  and S.ID = R.sportID
  and R.result = (
    select max(R1.result)
    from Results R1
    where R1.sportID = R.sportID
);

select distinct P.ID, P.name, P.height, R.result, S.name, case (R.result = S.record) when true then 'Yes' else 'No' end as "record?"
from People P, Results R, Sports S
where P.ID = R.peopleID
  and S.ID = R.sportID
  and (S.ID, R.result) in (
    select R1.sportID, max(R1.result)
    from Results R1
    group by R1.sportID
);

-- Query 15
select P.ID, P.name
from People P
where not exists (
    select *
    from Results R
    where R.peopleID = P.ID
);

-- Query 16
select P.ID, P.name
from People P 
    join Results R on P.ID = R.peopleID
    join Sports S on S.ID = R.sportID
where S.name = 'High Jump'
  and S.record = R.result
union
select P.ID, P.name
from People P 
    join Results R on P.ID = R.peopleID
    join Competitions C on C.ID = R.competitionID
where extract(year from C.held) = 2002 
  and extract(month from C.held) = 6;

-- Query 17
select P.ID, P.name
from People P
    join Results R on R.peopleID = P.ID
    join Sports S on R.sportID = S.ID
where R.result = S.record
and P.ID in (
    select P.ID
    from People P
        join Results R on R.peopleID = P.ID
    group by P.ID, P.name
    having count(distinct sportID) = 1);

-- Query 18
select count( P.ID ) as num
from People P
where 10 <= (
    select count(distinct C.place)
    from Results R 
        join Competitions C on R.competitionID = C.ID
    where R.peopleID = P.ID
);

-- Query 19: double negation
select P.ID, P.name
from People P
where not exists (
    select * 
    from Sports S
    where not exists (
        select *
        from Results R
        where R.sportID = S.ID
          and R.peopleID = P.ID
          and R.result = S.record));

-- Query 20: counting
select 	S.ID, S.name, S.record, min(R.result)
from Sports S 
	join Results R on S.ID = R.sportID
	join Competitions C on R.competitionID = C.ID
group by S.ID
having count(distinct C.place) = (
	select count(distinct C.place)
	from Competitions C
);

-- Query 20: double negation
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