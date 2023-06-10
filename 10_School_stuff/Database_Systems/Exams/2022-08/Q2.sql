-- Trigger function
CREATE FUNCTION CheckUsage() RETURNS TRIGGER
AS $$ BEGIN
    -- Check 1: usage value
    IF (NEW.usage <= 0) THEN
        RAISE EXCEPTION 'usage must be greater than 0';
    END IF;

    -- Check 2: usage cannot be greater than capacity
    IF (NEW.usage > (SELECT capacity FROM resource WHERE rid = NEW.rid)) THEN
        RAISE EXCEPTION 'usage cannot be greater than capacity';
    END IF;
    RETURN NEW;
END; $$ LANGUAGE plpgsql;

-- Trigger code
CREATE TRIGGER CheckUsage
AFTER UPDATE ON BasicService
FOR EACH ROW EXECUTE PROCEDURE CheckUsage();

-- Test the trigger
UPDATE BasicService SET usage = 0 WHERE bsid = 1;
UPDATE BasicService SET usage = 186 WHERE bsid = 1;
UPDATE BasicService SET usage = 233 WHERE bsid = 1;