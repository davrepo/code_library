SELECT COUNT(*)
FROM flights f
JOIN airport a ON f.dep = a.airport
JOIN country c ON a.country = c.country
JOIN aircraft ac ON f.actype = ac.actype
WHERE c.region = 'AS' AND ac.capacity > 300;