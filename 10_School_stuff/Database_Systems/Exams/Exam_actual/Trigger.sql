DELIMITER $

CREATE PROCEDURE insertDA(theDancerID INTEGER, awardDescription VARCHAR(100))

BEGIN
    DECLARE theAwardID INTEGER;
    SELECT MIN(id) INTO theAwardID
    FROM Award
    WHERE description = awardDescription;
    INSERT INTO DancerAward(dancerID, awardID)
    VALUES (theDancerID, theAwardID);
END
$
DELIMITER ;

CALL insertDA(2, "Revelation of the Year");