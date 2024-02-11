-- drop statements (optional)

drop table if exists Programmer;
drop table if exists Yoda;
drop table if exists Anakin;
drop table if exists Skill;
drop table if exists Mantra;
drop table if exists Masters;
drop table if exists Observes;

-- entity tables

create table Programmer (
    PID serial primary key,
);

-- Yoda and Anakin are subclasses of Programmer
create table Yoda (
	PID integer primary key references Programmer (PID),
    JediLevel integer not null
);

create table Anakin (
	PID integer primary key references Programmer (PID),
    AngerLevel integer not null
    -- add Yoda PID as foreign key with constraint NOT NULL
    YodaPID integer references Yoda (PID) not null
);

create table Skill (
	SID serial primary key
);

-- Mantra is weak entity of Yoda
create table Mantra (
    PID integer references Yoda (PID),
    Mantra varchar not null,
    primary key (PID, Mantra)
);

-- Entity Yoda has a many-to-many relationship with Skill named Masters, Yoda has 1..N Skill, Skill has 0..M Yoda
-- DDL cannot enfore 1..N
create table Masters (
    PID int references Yoda (PID),
    SID int references Skill (SID),
    SkillLevel integer not null,
    primary key (PID, SID)
);

-- Masters is a aggregation, Anakin has Observes relation with Masters. 
-- Anakin has 0..N Masters, Masters has 0..M Anakin
-- use option 1, Relationship Key
create table Observes (
    SkillID int,
    YodaID int,
    FOREIGN KEY (SkillID, YodaID) REFERENCES Masters (SID, PID),
    AnakinID int references Anakin (PID),
    primary key (SkillID, YodaID, AnakinID)
);