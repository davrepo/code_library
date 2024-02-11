-- (a)
SELECT COUNT(*) 
FROM employees 
WHERE ename LIKE '%sdottir';

-- (b)
select count(distinct w.eid)
from audits a
	join works w on a.wid = w.wid
where a.rating < (
	select avg (rating) 
	from audits
);

-- (c)
select count(distinct w.pid)
from works w 
	join projects p on p.pid = w.pid
where p.tid not in (
	select ct.tid 
	from clients_types ct
	where ct.cid = w.cid
);
-- 151

-- (d)
SELECT COUNT(DISTINCT e.eid)
FROM employees e
WHERE EXISTS (
  SELECT 1
  FROM works w1
  JOIN works w2 ON w1.eid = w2.eid AND w1.cid = w2.cid AND w1.pid <> w2.pid
  JOIN projects p1 ON w1.pid = p1.pid
  JOIN projects p2 ON w2.pid = p2.pid
  WHERE e.eid = w1.eid AND p1.tid <> p2.tid
);

-- (e)
SELECT w.cid
FROM works w
GROUP BY w.cid, w.pid
HAVING COUNT(w.eid) = (
  SELECT MAX(employee_count)
  FROM (
    SELECT COUNT(eid) AS employee_count
    FROM works
    GROUP BY cid, pid
  ) AS subquery
);

-- (f)
SELECT MAX(total_hours) AS highest_total_hours
FROM (
  SELECT eid, SUM(hours) AS total_hours
  FROM works
  GROUP BY eid
) AS subquery;


-- (g)
SELECT COUNT(*) 
FROM (
  SELECT p.tid
  FROM projects p
  JOIN works w ON p.pid = w.pid
  GROUP BY p.tid
  HAVING COUNT(DISTINCT w.cid) = (
    SELECT COUNT(*)
    FROM clients
  )
) AS X;

-- (h)
select count(*)
from (
	select a.eid 
	from audits a
		join works w on w.wid = a.wid and w.eid <> a.eid
	group by a.eid
	having count(distinct w.eid) = (
		select count(*) - 1
		from employees
	) 
) X;
-- 1

