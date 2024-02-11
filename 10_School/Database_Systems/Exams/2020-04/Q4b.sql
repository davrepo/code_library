drop table if exists Cure;
drop table if exists Patient;
drop table if exists Doctor;
drop table if exists AuditingCompany;
drop table if exists AccountHolder;

create table Patient (
    PID INT PRIMARY KEY,
);

create table AccountHolder (
    AID INT PRIMARY KEY
);

-- Categorical relation, Total
create table Doctor (
    DID INT PRIMARY KEY,
    AID INT NOT NULL REFERENCES AccountHolder(AID)
);

-- Categorical relation, Total
create table AuditingCompany (
    ACID INT PRIMARY KEY,
    AID INT NOT NULL REFERENCES AccountHolder(AID)
);

-- relationship table (only 1 due to 1..1 constraints)
-- so no Review and Audit table

-- Cure relation
create table Cure (
    DID INT REFERENCES Doctor(DID),
    PID INT REFERENCES Patient(PID),
    -- Audit aggregation relation (1..1) on Cure
    ACID INT NOT NULL REFERENCES AuditingCompany(ACID),
    -- Review aggregation on Audit aggregation (1..1)
    ReviewID INT NOT NULL REFERENCES Doctor(DID),
    PRIMARY KEY (DID, PID)
);


