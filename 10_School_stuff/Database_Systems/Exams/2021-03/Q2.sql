CREATE FUNCTION CheckYear() RETURNS TRIGGER
AS $$ BEGIN
    -- Check 1: Is the injection now?
    IF (NEW.injectionyear <> date_part('year', CURRENT_DATE)) THEN
        RAISE EXCEPTION 'Injection must be now';
    END IF;
    -- Check 2: Is the person born?
    IF (NEW.injectionyear < (SELECT P.birthyear
                            FROM people P
                            WHERE P.ID = NEW.peoID)) THEN
        RAISE EXCEPTION 'Person must be born'
    END IF;
    RETURN NEW;
END; $$ LANGUAGE plpgsql;

CREATE TRIGGER CheckYear
BEFORE INSERT ON injections
FOR EACH ROW EXECUTE PROCEDURE CheckYear();