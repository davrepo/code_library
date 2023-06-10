-- (a)
SELECT COUNT(*)
FROM employees
WHERE EXTRACT(year FROM birthday) = 1954;

-- (b)
SELECT EXTRACT(year FROM E.birthday)
FROM employees E
JOIN dept_manager DM ON E.emp_no = DM.emp_no
JOIN departments D ON DM.dept_no = D.dept_no
WHERE D.name = 'Finance' AND DM.to_date IS NULL;

-- (c)
SELECT COUNT(*)
FROM (
    SELECT DE.dept_no
    FROM dept_emp DE
    WHERE DE.to_date IS NULL
    GROUP BY DE.dept_no
    HAVING COUNT(DE.emp_no) > 50000
) AS Subquery;

-- (d)
SELECT DE.emp_no
FROM dept_emp DE
WHERE DE.to_date IS NOT NULL
GROUP BY DE.emp_no
HAVING SUM(DE.to_date - DE.from_date) = (
  SELECT MAX(SUM_TIME)
  FROM (
    SELECT emp_no, SUM(to_date - from_date) AS SUM_TIME
    FROM dept_emp
    WHERE to_date IS NOT NULL
    GROUP BY emp_no
  ) AS TEMP
);


-- (e)
SELECT COUNT(DISTINCT DE.emp_no) 
FROM dept_emp DE
JOIN departments D ON DE.dept_no = D.dept_no
WHERE D.name = 'Development' AND DE.emp_no NOT IN (
  SELECT DISTINCT T.emp_no
  FROM titles T
  WHERE T.title LIKE '%Engineer'
);


-- (f) 
SELECT COUNT(DISTINCT T.title)
FROM titles T
JOIN dept_emp DE ON T.emp_no = DE.emp_no
JOIN departments D ON DE.dept_no = D.dept_no
WHERE D.name = 'Development' AND DE.to_date IS NULL AND T.to_date IS NULL;

-- (g)
SELECT COUNT(*)
FROM (
SELECT T.emp_no
FROM titles T
WHERE T.title LIKE '%Engineer'
GROUP BY T.emp_no
HAVING COUNT(DISTINCT T.title) = (SELECT COUNT(DISTINCT title) FROM titles WHERE title LIKE '%Engineer')
) AS Subquery;

-- (h)
SELECT T.emp_no
FROM titles T
JOIN dept_emp DE ON T.emp_no = DE.emp_no
JOIN departments D ON DE.dept_no = D.dept_no
JOIN salaries S ON T.emp_no = S.emp_no
WHERE T.title = 'Senior Engineer' AND D.name = 'Development' AND T.to_date IS NULL AND DE.to_date IS NULL AND S.to_date IS NULL
AND S.salary = (
  SELECT MAX(S2.salary)
  FROM titles T2
  JOIN dept_emp DE2 ON T2.emp_no = DE2.emp_no
  JOIN departments D2 ON DE2.dept_no = D2.dept_no
  JOIN salaries S2 ON T2.emp_no = S2.emp_no
  WHERE T2.title = 'Senior Engineer' AND D2.name = 'Development' AND T2.to_date IS NULL AND DE2.to_date IS NULL AND S2.to_date IS NULL
);