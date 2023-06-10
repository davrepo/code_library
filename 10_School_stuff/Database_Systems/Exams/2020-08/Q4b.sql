drop table if exists Audit;
drop table if exists Client;
drop table if exists Shrink;
drop table if exists Office;
drop table if exists Manager;

create table Manager (
    MID INT primary key
);

create table Office (
    OID INT primary key,
    -- Runs relation
    MID INT not null REFERENCES Manager(MID)
);

create table Shrink (
    SID INT primary key
    -- Hires relation
    OID INT not null REFERENCES Office(OID)
    since DATE not null
);

create table Client (
    CID INT primary key
    -- Treats relation
    SID INT not null REFERENCES Shrink(SID)
);

-- Aggregation, where Manager has Audit relation with Treats
create table Audit (
	CID INT REFERENCES Client(CID),
    MID INT REFERENCES Manager(MID),
	primary key (CID, MID)
);