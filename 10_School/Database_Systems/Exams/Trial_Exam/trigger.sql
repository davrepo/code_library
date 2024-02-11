DROP TRIGGER IF EXISTS CheckDate ON flights;
DROP FUNCTION IF EXISTS CheckDate();

-- Trigger function
CREATE FUNCTION CheckDate() RETURNS TRIGGER AS $$
BEGIN
    -- Check: Is the operating time range OK?
    IF (NEW.END_OP < NEW.START_OP) THEN
        RAISE EXCEPTION 'Cannot operate for a negative duration';
        USING ERRCODE = '45000';
    END IF;
    RETURN NEW;
END; $$ LANGUAGE plpgsql;

-- Trigger code
CREATE TRIGGER CheckDate
BEFORE INSERT ON flights
FOR EACH ROW EXECUTE PROCEDURE CheckDate();
```

-- Test the trigger
INSERT INTO flights VALUES (500000, 'LH', 'LH001', 'HAM', 'FRA', 610, 720, '321', '2010-10-16', '2010-10-05', 'MO, TH, SA, SU');
INSERT INTO flights VALUES (500001, 'LH', 'LH001', 'HAM', 'FRA', 610, 720, '321', '2010-10-16', '2011-10-05', 'MO, TH, SA, SU');
INSERT INTO flights VALUES (500002, 'LH', 'LH001', 'HAM', 'FRA', 610, 720, '321', '2010-10-16', NULL, 'MO, TH, SA, SU');