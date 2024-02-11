-- (a)
SELECT COUNT(*)
FROM Tests
JOIN Variants ON Tests.variantID = Variants.ID
WHERE Variants.name = 'omicron';

-- (b)
SELECT COUNT(*)
FROM Variants
WHERE NOT EXISTS (
    SELECT 1
    FROM Tests
    WHERE Tests.variantID = Variants.ID
);

-- (c)
SELECT COUNT(DISTINCT Tests.variantID)
FROM Tests
JOIN Testers ON Tests.testerID = Testers.ID
JOIN Kits ON Tests.kitID = Kits.ID
JOIN Variants ON Tests.variantID = Variants.ID
JOIN Risks ON Variants.riskID = Risks.ID
WHERE Testers.name = 'Kent Lauridsen'
    AND Kits.producer = 'JJ'
    AND Risks.level = 'extreme'
    AND EXTRACT(YEAR FROM Tests.time) = 2021;

-- (d)
SELECT COUNT(*)
FROM Variants
LEFT JOIN (
    SELECT DISTINCT variantID
    FROM Detects
    WHERE accuracy > 50
) AS AccurateDetects ON Variants.ID = AccurateDetects.variantID
WHERE AccurateDetects.variantID IS NULL;


-- (e)
SELECT MIN(avg_accuracy)
FROM (
    SELECT variantID, AVG(accuracy) AS avg_accuracy
    FROM Detects
    GROUP BY variantID
    HAVING COUNT(kitID) > 1
) subquery;

-- (f)
SELECT testerID
FROM (
    SELECT testerID, COUNT(*) AS test_count
    FROM Tests
    JOIN Kits ON Tests.kitID = Kits.ID
    WHERE Kits.producer = 'JJ'
    GROUP BY testerID
) AS TestCounts
WHERE test_count = (
    SELECT MAX(test_count)
    FROM (
        SELECT COUNT(*) AS test_count
        FROM Tests
        JOIN Kits ON Tests.kitID = Kits.ID
        WHERE Kits.producer = 'JJ'
        GROUP BY testerID
    ) AS MaxTestCount
);

-- (g)
SELECT COUNT(*)
FROM (
    SELECT T.testerID
    FROM Tests T
    JOIN Variants V ON T.variantID = V.ID
    JOIN Risks R ON V.riskID = R.ID
    WHERE R.level = 'mild'
    GROUP BY T.testerID
    HAVING COUNT(DISTINCT V.ID) = (
        SELECT COUNT(*)
        FROM Variants
        JOIN Risks ON Variants.riskID = Risks.ID
        WHERE Risks.level = 'mild'
    )
) AS MildVariantTesters;


-- (h)
SELECT MAX(Tests.time)
FROM Tests
JOIN Variants ON Tests.variantID = Variants.ID
JOIN Risks ON Variants.riskID = Risks.ID
JOIN Detects ON Tests.kitID = Detects.kitID AND Tests.variantID = Detects.variantID
WHERE Risks.level = 'extreme'
    AND Detects.accuracy < 10;


