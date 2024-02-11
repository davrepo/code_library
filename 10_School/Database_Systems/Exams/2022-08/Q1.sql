-- (a) There are 45 services which have category “Compute”. How many services have category “Analytics”?
SELECT COUNT(*)
FROM Service
JOIN Category ON Service.catid = Category.catid
WHERE Category.catname = 'Analytics';
-- 139


-- (b) How many composite services have no constituent basic service?
SELECT COUNT(*)
FROM CompositeService
LEFT JOIN Constitutes ON CompositeService.csid = Constitutes.csid
WHERE Constitutes.bsid IS NULL;
-- 20


-- (c)The cheapest basic services (with lowest BasicService.usage × Resource.price)
-- are the services with bsid = 35 and bsid = 299. Write a query to return the identifiers
-- of the most expensive basic services.
SELECT BasicService.bsid
FROM BasicService
JOIN Resource ON BasicService.rid = Resource.rid
WHERE BasicService.usage * Resource.price = (
  SELECT MAX(BasicService.usage * Resource.price)
  FROM BasicService
  JOIN Resource ON BasicService.rid = Resource.rid
);
-- 487, 500


-- (d) The resource with rid = 68 is an example of an over-consumed resource, as its total
-- usage by all basic services is 76, which exceeds its capacity of 62. How many resources
-- are over-consumed in this database?
SELECT COUNT(*)
FROM Resource
WHERE (
  SELECT SUM(BasicService.usage)
  FROM BasicService
  WHERE BasicService.rid = Resource.rid
) > Resource.capacity;
-- 5


-- (e) There are 28 clients which only subscribe to composite services (i.e., they subscribe
-- to some composite services, but no basic services). How many clients only subscribe
-- to basic services?
SELECT COUNT(*)
FROM Client
WHERE Client.cid NOT IN (
  SELECT DISTINCT Subscribes.cid
  FROM Subscribes
  JOIN CompositeService ON Subscribes.sid = CompositeService.csid
) AND Client.cid IN (
  SELECT DISTINCT Subscribes.cid
  FROM Subscribes
  JOIN BasicService ON Subscribes.sid = BasicService.bsid
);
-- 7


-- (f) There are 2 clients which directly (i.e., not via composite services) subscribe to all
-- basic services offered by the service provider. How many clients subscribe indirectly
-- (i.e., via composite services) to all basic services offered by the service provider?
SELECT COUNT(*)
FROM (
  SELECT c.cid
  FROM Client c
  JOIN Subscribes s ON c.cid = s.cid
  JOIN Constitutes con ON s.sid = con.csid
  GROUP BY c.cid
  HAVING COUNT(DISTINCT con.bsid) = (
    SELECT COUNT(*) FROM BasicService
  )
) AS temp_table;
-- 5


-- (g) The service provider wants to implement the following rule: clients which subscribe to
-- a composite service X should not subscribe to any of the basic services that constitute
-- the composite service X. This rule does not currently hold in the database. As an
-- example, the client with cid = 16 would violate the rule as it subscribes to composite
-- service with csid = 431 and its constituent basic service with bsid = 120 (as well
-- as two other pairs of composite and constituent basic services). How many distinct
-- clients in total would violate this rule?
SELECT COUNT(DISTINCT Client.cid)
FROM Client
JOIN Subscribes AS sub1 ON Client.cid = sub1.cid
JOIN Subscribes AS sub2 ON Client.cid = sub2.cid
JOIN Constitutes ON sub1.sid = Constitutes.csid AND sub2.sid = Constitutes.bsid;
-- 79


-- (h) Write a query that returns, for each client that subscribes to some service(s), the cid
-- of the client and the total monthly cost of all its subscriptions.
-- Note: This query should return one row, with two columns, for each client that has
-- some subscriptions. You are not asked to paste in the result for this query.
SELECT Client.cid, SUM(Resource.price * BasicService.usage) AS total_monthly_cost
FROM Client
JOIN Subscribes ON Client.cid = Subscribes.cid
JOIN Service ON Subscribes.sid = Service.sid
JOIN BasicService ON Service.sid = BasicService.bsid
JOIN Resource ON BasicService.rid = Resource.rid
GROUP BY Client.cid;


