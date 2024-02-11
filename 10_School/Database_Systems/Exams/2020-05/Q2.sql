create function CheckTD() returns TRIGGER 
as $$ BEGIN
    -- Check 1: is the gender the same for both?
    IF ((select T.genderID
            from Teams T
            where T.ID = NEW.teamID) <> (select D.genderID
                                            from Divisions D
                                            where D.ID = NEW.divisionID)) THEN
        RAISE EXCEPTION 'Team and division must have same gender';
    END IF;
    -- Check 2: is the team already in a division=
    IF (EXISTS ( SELECT *
                FROM TeamsInDivisions TD
                WHERE TD.teamID = NEW.teamID)) THEN
        RAISE EXCEPTION 'Cannot have a team in two division';
    END IF;
    RETURN NEW;
END; $$ LANGUAGE plpgsql;

-- Trigger code
CREATE TRIGGER CheckTD
BEFORE INSERT ON TeamsInDivisions
FOR EACH ROW EXECUTE PROCEDURE CheckTD();
