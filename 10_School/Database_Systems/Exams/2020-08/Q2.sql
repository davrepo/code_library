-- Trigger function
CREATE FUNCTION CheckRel() RETURNS TRIGGER
AS $$ BEGIN
    -- Check 1: No self-relationships
    IF (NEW.fromID = NEW.toID) THEN
        RAISE EXCEPTION 'Cannot relate to oneself';
    END IF;
    -- Check 2: Is the relationship bi-directional?
    IF (NOT EXISTS (SELECT * FROM Relationships R WHERE R.fromID = NEW.toID AND R.toID = NEW.fromID)) THEN
        RAISE EXCEPTION 'Relationship must be bi-directional';
    END IF;
    RETURN NEW;
END; $$ LANGUAGE plpgsql;

-- Trigger code
CREATE TRIGGER CheckRel
BEFORE INSERT ON Relationships
FOR EACH ROW EXECUTE PROCEDURE CheckRel();
