CREATE TABLE Teachers (
    TID INT PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE Students (
    SID INT PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE Censors (
    CID INT PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE Tutor (
    -- keys
    fromyear INT,
    SID INT REFERENCES Students(SID),
    -- 1..1 Teacher cardinality
    TID INT NOT NULL REFERENCES Teachers(TID),
    -- 1..1 Censors cardinality, Aggregation
    CID INT NOT NULL REFERENCES Censors(CID),
    PRIMARY KEY (SID, fromyear)
);

CREATE TABLE Lectures (
    LID INT PRIMARY KEY,
    subject VARCHAR NOT NULL
);

CREATE TABLE Attend (
    SID INT REFERENCES Students(SID),
    LID INT REFERENCES Lectures(LID),
    PRIMARY KEY (SID, LID)
);



