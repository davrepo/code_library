WITH departing_flights AS (
  SELECT dep AS airport, COUNT(*) AS departures
  FROM flights
  GROUP BY dep
),
arriving_flights AS (
  SELECT arr AS airport, COUNT(*) AS arrivals
  FROM flights
  GROUP BY arr
),
airport_flights AS (
  SELECT COALESCE(d.airport, a.airport) AS airport, COALESCE(departures, 0) AS departures, COALESCE(arrivals, 0) AS arrivals
  FROM departing_flights d
  FULL OUTER JOIN arriving_flights a ON d.airport = a.airport
)
SELECT COUNT(*)
FROM airport_flights
WHERE arrivals > departures;