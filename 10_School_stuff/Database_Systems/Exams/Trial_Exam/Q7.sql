WITH nl_airports AS (
  SELECT airport
  FROM airport
  WHERE country = 'NL'
),
nl_flight_departures AS (
  SELECT DISTINCT al, dep
  FROM flights f
  JOIN airport a ON f.dep = a.airport
  WHERE a.country = 'NL'
)

SELECT COUNT(DISTINCT al)
FROM nl_flight_departures
GROUP BY al
HAVING COUNT(DISTINCT dep) = (SELECT COUNT(*) FROM nl_airports);