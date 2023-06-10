drop table if exists SellsTo;
drop table if exists Adult;
drop table if exists Child;
drop table if exists Company;
drop table if exists Person;
drop table if exists Taxpayer;

CREATE TABLE Taxpayer (
    TID INT PRIMARY KEY
);

CREATE TABLE Person (
    PID INT PRIMARY KEY,
);

-- Adult entity is a category of Taxpayer, total, union
-- Adult entity is a specialization of Person, disjoint, total
CREATE TABLE Adult (
    PID INT PRIMARY KEY REFERENCES Person(PID)
    role VARCHAR NOT NULL,
    TID INT NOT NULL REFERENCES Taxpayer(TID)
);

CREATE TABLE Child (
    PID INT PRIMARY KEY REFERENCES Person(PID)
    age INT NOT NULL
);

CREATE TABLE Company (
    CID INT PRIMARY KEY,
    TID INT NOT NULL REFERENCES Taxpayer(TID)
);

CREATE TABLE SellsTo (
    day DATE,
    CID INT REFERENCES Company(CID),
    PID INT REFERENCES Child(PID),
    price INT NOT NULL,
    -- PaysFor 1..1 aggregation relation
    APID INT NOT NULL REFERENCES Adult(PID),
    PRIMARY KEY (day, CID, PID)
);