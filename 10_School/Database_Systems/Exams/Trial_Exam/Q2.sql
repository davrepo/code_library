SELECT COUNT(DISTINCT a.airport)
FROM airport a
JOIN country c ON a.country = c.country
JOIN flights f_dep ON a.airport = f_dep.dep
JOIN flights f_arr ON a.airport = f_arr.arr
WHERE c.region = 'EU';