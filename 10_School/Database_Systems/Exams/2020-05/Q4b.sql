drop table if exists observes;
drop table if exists masters;
drop table if exists mantras;
drop table if exists anakins;
drop table if exists yodas;
drop table if exists programmers;
drop table if exists skills;

create table Programmer (
    PID INT primary key
);

create table Yoda (
    PID INT PRIMARY KEY REFERENCES Programmer(PID),
    JediLevel INT NOT NULL
);

create table Anakin (
    PID INT PRIMARY KEY REFERENCES Programmer(PID),
    AngerLevel INT NOT NULL
    -- Trains relation
    YodaPID INT NOT NULL REFERENCES Yoda(PID)
);

-- Weak entity, Speaks relation
create table Mantra (
    Mantra VARCHAR, 
    YodaID INT REFERENCES Yoda(PID),
    PRIMARY KEY (Mantra, YodaID)
);

create table Skill (
    SID INT PRIMARY KEY
);

create table Masters (
    PID INT REFERENCES Yoda(PID),
    SID INT REFERENCES Skill(SID),
    SkillLevel INT NOT NULL,
    PRIMARY KEY (PID, SID)
);

-- Aggregation, option 1, use existing keys
create table Observes (
    AnakinID INT REFERENCES Anakin(PID),
    YodaID INT,
    SID INT,
    FOREIGN KEY (YodaID, SID) REFERENCES Masters(PID, SID),
    PRIMARY KEY (AnakinID, YodaID, SID)
);



