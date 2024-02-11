SELECT * FROM accountrecords;
SELECT * FROM accounts;
SELECT * FROM bills;
SELECT * FROM people;

-- Exercise 1 (Create View)
-- Create AllAccountRecords (view) by joining Accounts and AccountRecords. 
-- Show all columns, except AccountRecords.AID. 
-- Accounts with no entry in AccountRecords should be shown with NULLs

DROP VIEW IF EXISTS AllAccountRecords;

CREATE VIEW AllAccountRecords (
	PID,
	AID,
	aDate,
	aBalance,
	aOver,
	RID,
	rDate,
	rType,
	rAmount,
	rBalance)
AS
SELECT  
	A.PID, 
	A.AID, 
	A.aDate, 
	A.aBalance, 
	A.aOver,
	R.RID,  
	R.rDate, 
	R.rType,
	R.rAmount, 
	R.rBalance
FROM Accounts A
     LEFT OUTER JOIN AccountRecords R ON A.AID = R.AID;

------------------------------------------------------------------------------------------------------------
-- 2. CheckBills (Trigger)
------------------------------------------------------------------------------------------------------------

DROP TRIGGER IF EXISTS CheckBills ON Bills;
DROP FUNCTION IF EXISTS CheckBills();

-- Create a trigger CheckBills on Bills that enforces a) the rule that bills cannot have a negative
-- amount, and b) that the due date must be in the future.
-- May not delete Bills
-- May only update bIsPaid
CREATE FUNCTION CheckBills() 
RETURNS TRIGGER 
AS 
$$
BEGIN
	-- May not delete Bills
	IF (TG_OP = 'DELETE') THEN
		RAISE EXCEPTION 'Function CheckBills: Cannot Delete from Bills!' USING ERRCODE = '45000';
	END IF;

	-- May only update bIsPaid, this checks for changes to other attributes and rejects
	IF (TG_OP = 'UPDATE) THEN
		RAISE EXCEPTION 'Function CheckBills: Cannot Update Bills, except for bIsPaid!' USING ERRCODE = '45000';
    END IF;

	-- Here we must be inserting, check the amount
	IF( NEW.bAmount < 0 ) THEN
		RAISE EXCEPTION 'Function CheckBills: Amount must be non-negative!' USING ERRCODE = '45000';
	END IF;

	-- Check the due date, which must be no earlier than tomorrow
	IF( NEW.bDueDate <= CURRENT_DATE ) THEN
		RAISE EXCEPTION 'Function CheckBills: Date must be tomorrow or later!' USING ERRCODE = '45000';
	END IF;

	-- After trigger, so return value is ignored
	RETURN NEW;
END;
$$ 
LANGUAGE plpgsql;

-- Since we are not updating the new record, the trigger may be either BEFORE or AFTER
CREATE TRIGGER CheckBills 
-- Note UPDATE OF... where blsPaid is the only attribute that may be updated
BEFORE INSERT OR DELETE OR UPDATE OF BID, PID, bDueDate, bAmount 
ON Bills 
FOR EACH ROW EXECUTE PROCEDURE CheckBills();

------------------------------------------------------------------------------------------------------------
-- 3. CheckRecord (Trigger)
------------------------------------------------------------------------------------------------------------

DROP TRIGGER IF EXISTS CheckRecord ON AccountRecords;
DROP FUNCTION IF EXISTS CheckRecord();

CREATE FUNCTION CheckRecord() 
RETURNS TRIGGER 
AS 
$$
BEGIN
	IF (TG_OP = 'DELETE') OR (TG_OP = 'UPDATE') THEN
		RAISE EXCEPTION 'Function CheckRecord: Cannot Update or Delete from AccountRecords!' USING ERRCODE = '45000';
	END IF;

	-- a) check for sufficient funds
	IF( -NEW.rAmount > ( SELECT A.aOver + A.aBalance FROM Accounts A WHERE A.AID = NEW.AID ) ) THEN
		RAISE EXCEPTION 'Function CheckRecord: Amount must be available in account!' USING ERRCODE = '45000';
	END IF;

	-- b) update the balance on the account.
	UPDATE Accounts 
		SET 	aBalance = aBalance + NEW.rAmount,
			aDate = CURRENT_DATE
	WHERE AID = NEW.AID;

	-- Insert the account record.
	NEW.rBalance := ( SELECT A.aBalance FROM Accounts A WHERE A.AID = NEW.AID );
	NEW.rDate := CURRENT_DATE;

	-- Must return NEW as otherwise the insertion does not happen
	RETURN NEW;
END;
$$ 
LANGUAGE plpgsql;

-- Since we plan to update the new record, the trigger must be BEFORE
CREATE TRIGGER CheckRecord 
BEFORE INSERT OR UPDATE OR DELETE 
ON AccountRecords 
FOR EACH ROW EXECUTE PROCEDURE CheckRecord();


------------------------------------------------------------------------------------------------------------
-- 4. Transfer (Procedure)
------------------------------------------------------------------------------------------------------------
-- Create a procedure Transfer, which takes three parameters, iToAID, iFromAID, and iAmount
-- transfers the amount between the two accounts in a single transaction. 
-- If the amount is not available in the iFromAID account, then the operation should be aborted
-- No return value.
-- Ensure that the transfer is non-negative.

DROP FUNCTION IF EXISTS Transfer( IN iToAID INT, IN iFromAID INT, IN iAmount INT );

CREATE FUNCTION Transfer( IN iToAID INT, IN iFromAID INT, IN iAmount INT  ) 
RETURNS VOID 
AS 
$$
BEGIN
	-- Not strictly needed according to project description, but makes sense nevertheless
	IF ( iAmount < 0 ) THEN
		RAISE EXCEPTION 'Function Transfer: Cannot transfer negative amount!' USING ERRCODE = '45000';
	END IF;

	-- Deposit into the TO account
	INSERT INTO AccountRecords (AID, rAmount, rDate, rType) 
	VALUES (iToAID, iAmount, CURRENT_DATE, 'T');

	-- Withdraw from the FROM account
	INSERT INTO AccountRecords (AID, rAmount, rDate, rType) 
	VALUES (iFromAID, -iAmount, CURRENT_DATE, 'T');
END;
$$ 
LANGUAGE plpgsql;


-- ??? My Solution is different, I used Procedure

CREATE OR REPLACE PROCEDURE Transfer(IN iToAID, IN iFromAID, IN iAmount)
AS
$$
BEGIN
	IF ( iAmount < 0 ) THEN
		RAISE EXCEPTION 'Procedure Transfer: Cannot transfer negative amount!' USING ERRCODE = '45000';
	END IF;
	
	IF ( iAmount > (SELECT accounts.ablanace FROM accounts WHERE accounts.aid = iFromAID) ) THEN
		RAISE EXCEPTION 'Procedure Transfer: insufficient funds' USING ERRCODE = '45000';
	END IF;
	
	UPDATE accounts
	SET abalance = abalance - iAmount
	WHERE aid = iFromAID;
	
	UPDATE accounts
	SET abalance = abalance + iAmount
	WHERE aid = iToAID;
	
	COMMIT;
END;
$$
LANGUAGE plpgsql

CALL Transfer(1, 2, 500)


------------------------------------------------------------------------------------------------------------
-- 5. DebtorStatus (View)
------------------------------------------------------------------------------------------------------------

DROP VIEW IF EXISTS DebtorStatus;

CREATE VIEW DebtorStatus
AS
SELECT P.PID, P.pName, SUM(A.aBalance) AS TotalBalance, SUM(A.aOver) AS TotalOverdraft
FROM People P
INNER JOIN Accounts A ON A.PID = P.PID
GROUP BY P.PID, P.pName
HAVING SUM(A.aBalance) < 0;


------------------------------------------------------------------------------------------------------------
-- 6. NewPerson (Trigger)
------------------------------------------------------------------------------------------------------------

DROP TRIGGER IF EXISTS NewPerson ON People;
DROP FUNCTION IF EXISTS NewPerson();

CREATE FUNCTION NewPerson() 
RETURNS TRIGGER 
AS 
$$
BEGIN
	-- Add the account
	INSERT INTO Accounts (PID, aDate, aBalance, aOver)
	VALUES (NEW.PID, CURRENT_DATE, 0, 10000);

	-- After trigger, so return value is ignored
	RETURN NEW;
END;
$$ 
LANGUAGE plpgsql;

-- Since we wish to create an account for the person, the person must be already there, so trigger must be AFTER
CREATE TRIGGER NewPerson 
AFTER INSERT 
ON People 
FOR EACH ROW EXECUTE PROCEDURE NewPerson();


------------------------------------------------------------------------------------------------------------
-- 7. InsertPerson (Function)
------------------------------------------------------------------------------------------------------------

DROP FUNCTION IF EXISTS InsertPerson( IN iName VARCHAR(50), IN iGender CHAR(1), IN iHeight FLOAT, IN iAmount INTEGER );

CREATE FUNCTION InsertPerson(
	IN iName VARCHAR(50),
	IN iGender CHAR(1),
	IN iHeight FLOAT,
	IN iAmount INTEGER)
RETURNS VOID 
AS 
$$
DECLARE
	newPID INTEGER;
	newAID INTEGER;
BEGIN
	-- Insert the person
	INSERT INTO People (pName, pGender, pHeight)
	VALUES (iName, iGender, iHeight);

	-- Since the trigger NewPerson creates an account, this is the lastval()
	newAID := lastval();

	-- Add the money to the account
	INSERT INTO AccountRecords (AID, rDate, rType, rAmount)
	VALUES (newAID, CURRENT_DATE, 'T', iAmount);

	RETURN;
END;
$$ 
LANGUAGE plpgsql;


------------------------------------------------------------------------------------------------------------
-- 8. PayOneBill (Function)
------------------------------------------------------------------------------------------------------------

DROP FUNCTION IF EXISTS PayOneBill( IN iBID INTEGER );
CREATE FUNCTION PayOneBill( IN iBID INTEGER ) 
RETURNS VOID 
AS $$
DECLARE
	MostFundedAccountID INT;
	AmountToPay INT;
BEGIN
	-- Check whether the bill is unpaid!
	IF NOT EXISTS( 	SELECT * 
			FROM Bills B
			WHERE B.BID = iBID
			  AND NOT B.bIsPaid ) THEN
		RAISE EXCEPTION 'Function PayOneBill: Bill is either non-existent or already paid!' USING ERRCODE = '45000';
	END IF;

	-- Check for existence of at least one account
	IF NOT EXISTS( 	SELECT * 
			FROM Accounts A 
				JOIN Bills B ON B.PID = A.PID
			WHERE B.BID = iBID ) THEN
		RAISE EXCEPTION 'Function PayOneBill: No account found!' USING ERRCODE = '45000';
	END IF;

	-- Find the account to pay from
	SELECT	MAX( A.AID )
	INTO	MostFundedAccountID	
	FROM 	Accounts A
		JOIN Bills B on A.PID = B.PID
	WHERE 	B.BID = iBID
	  AND	A.aBalance + A.aOver = ( 
			SELECT MAX( A2.aBalance + A2.aOver )
			FROM Accounts A2
			WHERE A2.PID = B.PID
		);

	-- Find the amount to pay
	SELECT	-B.bAmount
	INTO	AmountToPay	
	FROM 	Bills B
	WHERE 	B.BID = iBID;

	-- Make the payment
	-- CheckRecord trigger handles if there is insufficient funding.
	INSERT INTO AccountRecords (AID, rType, rAmount)
	VALUES (MostFundedAccountID, 'L', AmountToPay);
	
	-- Bill has been paid, need to update it.
	UPDATE 	Bills
	SET 	bIsPaid = true
	WHERE 	BID = iBID;


	RETURN;
END;
$$ 
LANGUAGE plpgsql;


------------------------------------------------------------------------------------------------------------
-- 9. LoanMoney (Procedure)
------------------------------------------------------------------------------------------------------------

DROP FUNCTION IF EXISTS LoanMoney( IN iAID INT, IN iAmount INT, IN iDueDate DATE  );

CREATE FUNCTION LoanMoney( IN iAID INT, IN iAmount INT, IN iDueDate DATE ) 
RETURNS VOID 
AS 
$$
DECLARE 
	tPID INT;
BEGIN
	-- Insert the loan into the account
	INSERT INTO AccountRecords(AID, rDate, rAmount, rType)
	VALUES(iAID, CURRENT_DATE, iAmount, 'L');
	
	-- Find the person which owns the account
	SELECT PID INTO tPID FROM Accounts WHERE AID = iAID;

	-- Insert a bill to match the loan
	-- Errors on amount and due date will be caught here
	INSERT INTO Bills(PID, bDueDate, bAmount, bIsPaid)
	VALUES( tPID, iDueDate, iAmount, FALSE );
END;
$$ 
LANGUAGE plpgsql;


------------------------------------------------------------------------------------------------------------
-- 10. FinancialStatus (View)
------------------------------------------------------------------------------------------------------------

DROP VIEW IF EXISTS FinancialStatus;
DROP VIEW IF EXISTS FS1;
DROP VIEW IF EXISTS FS2;

-- First helper view: Sum up all accounts of each person
-- The view has one entry for each person that has any accounts

CREATE VIEW FS1 (PID, totalBalances)
AS 
SELECT PID, SUM(aBalance) AS totalBalances
FROM Accounts 
GROUP BY PID;

-- Second helper view: Sum up all unpaid bills of each person
-- The view has one entry for each person that has any unpaid bills

CREATE VIEW FS2 (PID, totalUnPaid)
AS 
SELECT PID, SUM(bAmount) AS totalUnPaid
FROM Bills 
WHERE NOT bIsPaid  
GROUP BY PID;

-- The final view outer joins three tables/views with the same key: PID
CREATE VIEW FinancialStatus (
	PID, 
	pName, 
	pTotalBalances,
	pTotalUnPaid)
AS
SELECT 
	P.PID, 
	P.pName, 
	COALESCE(A.totalBalances, 0) as pTotalBalances,
	COALESCE(B.TotalUnPaid, 0) AS pTotalUnPaid
FROM 
	People P 
	JOIN FS1 A ON A.PID = P.PID
	LEFT OUTER JOIN FS2 B ON B.PID = P.PID;