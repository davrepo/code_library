CREATE TABLE LogExtremeTests (
    testerID INT,
    siteID INT,
    time TIMESTAMP,
    PRIMARY KEY (testerID, siteID, time),
    FOREIGN KEY (testerID, siteID, time) REFERENCES Tests(testerID, siteID, time)
);

DROP TRIGGER IF EXISTS FlagExtremeTests ON Tests;
DROP FUNCTION IF EXISTS FlagExtremeTests();

CREATE FUNCTION FlagExtremeTests() RETURNS TRIGGER AS $$
    BEGIN
        IF EXISTS (
            SELECT *
            FROM Variants V
                JOIN Risks R ON V.riskID = R.ID
            WHERE V.id = NEW.variantID AND R.level = 'extreme' THEN
            INSERT INTO LogExtremeTests VALUES (NEW.testerID, NEW.siteID, NEW.time);
        END IF;
        RETURN NEW;
END; $$ LANGUAGE plpgsql;

CREATE TRIGGER FlagExtremeTests
    AFTER INSERT ON Tests
    FOR EACH ROW EXECUTE PROCEDURE FlagExtremeTests();

INSERT INTO Tests VALUES (1, 1, 1, 1, CURRENT_TIMESTAMP);