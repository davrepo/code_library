drop table if exists Grades;
drop table if exists Takes;
drop table if exists Examiner;
drop table if exists Course;
drop table if exists Term;
drop table if exists Student;

CREATE TABLE Term (
    TID INT PRIMARY KEY,
    desc VARCHAR NOT NULL,
);

CREATE TABLE Student (
    SID INT PRIMARY KEY
    -- StartsIn relation
    TID INT NOT NULL REFERENCES Term(TID)
);

CREATE TABLE Course (
    CID INT PRIMARY KEY
);

CREATE TABLE Examiner (
    EID INT PRIMARY KEY
);

-- not regular Tertiary relation b/c
-- modified by Aggregation w/ option 2
create table Takes (
	-- using option 2
	TakesID integer primary key,
	SID integer not null references Student(SID),
	CID integer not null references Course(CID),
	TID integer not null references Term(TID),
	room varchar not null,
	unique (TID, CID) -- since Student is 1..1
);

create table Grades (
	TakesID integer references Takes(TakesID),
	EID integer references Examiner(EID),
	grade integer not null,
	primary key (TakesID, EID)
);

