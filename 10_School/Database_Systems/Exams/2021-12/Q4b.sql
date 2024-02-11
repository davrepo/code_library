CREATE TABLE Tours (
    TID INT PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE Cities (
    CID INT PRIMARY KEY,
    name VARCHAR NOT NULL
); 

CREATE TABLE Racers (
    RID INT PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE Legs (
    LID INT PRIMARY KEY,
    name VARCHAR NOT NULL
    -- end_at relation 1..1 
    End_CID INT NOT NULL REFERENCES Cities(CID)
    -- start_at relation 0..1
    Start_CID INT REFERENCES Cities(CID)
);

-- weak entities
CREATE TABLE Stretches (
    LID INT REFERENCES Legs(LID),
    name VARCHAR NOT NULL,
    PRIMARY KEY (LID, name)
);

CREATE TABLE Consist_off (
    consistID INT PRIMARY KEY,
    TID INT NOT NULL REFERENCES Tours(TID),
    LID INT NOT NULL REFERENCES Legs(LID),
    sequence INT NOT NULL,
    UNIQUE (TID, LID)
);

CREATE TABLE race_in (
    RID INT REFERENCES Racers(RID),
    consistID INT REFERENCES Consist_off(consistID),
    rank INT NOT NULL,
    PRIMARY KEY (RID, consistID)
);


