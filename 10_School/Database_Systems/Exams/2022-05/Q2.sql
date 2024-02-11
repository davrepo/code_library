DROP TRIGGER IF EXISTS CheckAudit ON Audits;
DROP FUNCTION IF EXISTS CheckAudit();

-- Trigger function
CREATE FUNCTION CheckAudit() RETURNS TRIGGER 
AS $$ BEGIN
    -- Check 1: Is the rating between 1 and 10
    IF (NEW.rating < 0 OR NEW.rating > 10) THEN
        RAISE EXCEPTION 'Rating must be between 1 and 10';
    END IF;
    -- Check 2: Is the auditor the same as worker?
    IF (EXISTS (SELECT * FROM Works w WHERE w.eid = NEW.eid AND w.wid = NEW.wid)) THEN
        RAISE EXCEPTION 'Auditor cannot be the same as worker';
    END IF;
    RETURN NEW;
END; $$ LANGUAGE plpgsql;

-- Trigger code
CREATE TRIGGER CheckAudit
BEFORE INSERT ON Audits
FOR EACH ROW EXECUTE PROCEDURE CheckAudit();

-- Test data
INSERT INTO Works (wid, pid, cid, eid, hours) VALUES (30000, 44, 34, 295, 8);
INSERT INTO Audits (wid, eid, rating) VALUES (30000, 295, 10);
INSERT INTO Works (wid, pid, cid, eid, hours) VALUES (30001, 44, 33, 295, 8);
INSERT INTO Audits (wid, eid, rating) VALUES (30001, 294, 5);