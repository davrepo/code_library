-- all code below is for PostgreSQL
-- create a databse called WASP

CREATE DATABASE WASP;

-- For people, the database should keep track of their ID, name, address, phone number,
-- date of birth (DOB), and date of death (DOD). The default value of DOD is
-- (thankfully!) NULL.

CREATE TABLE People (
    ID serial PRIMARY KEY,
    Name varchar(100) NOT NULL,
    Address varchar(255) NOT NULL,
    Phone varchar(20) NOT NULL,
    DOB date NOT NULL,
    DOD date DEFAULT NULL
);

-- People are further divided into members of WASP and enemies; each person is a
-- member, an enemy, or possibly both. For members, the starting date of membership
-- is registered. Note that WASP members cannot leave the party, even in death! For
-- enemies, the reason is registered.

CREATE TABLE Member (
    ID INT PRIMARY KEY REFERENCES people(ID),
    Start_date date NOT NULL
);

CREATE TABLE Enemy (
    ID INT PRIMARY KEY REFERENCES people(ID),
    Reason varchar(255) NOT NULL,
    OpponentID INT REFERENCES Opponent(ID)
);

-- For each WASP member, a list of their assets is maintained, which could be used to
-- achieve the WASP agenda. Each asset of a person is identified with the name of the
-- asset, but text fields must also be maintained to a) describe the asset in more detail
-- and b) describe how the asset could potentially be used.
-- WEAK Entity

CREATE TABLE Assets (
    MemberID INT REFERENCES members(ID),
    Name varchar(100) NOT NULL,
    Detail varchar(255) NOT NULL,
    Uses varchar(255) NOT NULL,
    PRIMARY KEY (Name, MemberID)
);

-- Events and relationships between various people (e.g. accidents, business partnership,
-- marriage, mortal enemies, . . . ) are registered in a fairly flexible way. The WASP
-- party uses the general term ‘linkings’. Each linking is an entity that is assigned an
-- ID, name, type and a more detailed description. Multiple people may participate in
-- each linking, but the minimum number of people per linking is two, and each person
-- may participate in multiple linkings with different people.

CREATE TABLE Linking (
    ID serial PRIMARY KEY,
    Name varchar(100) NOT NULL,
    Type varchar(100) NOT NULL,
    Description varchar(255) NOT NULL
);

-- Each participation of a person in a linking is monitored by one member. The monitoring
-- member never changes.

CREATE TABLE Participate (
    LinkingID INT REFERENCES Linking(id),
    PersonID INT REFERENCES people(id),
    MemberID INT NOT NULL REFERENCES Member(ID),
    PRIMARY KEY (LinkingID, PersonID)
);

-- The WASP party has a list of roles, each with a unique ID and a unique title, as
-- well as a monthly salary. Members take turns filling the roles: each member may
-- fill multiple roles at any given time, and multiple members may fill the same role.
-- However, members may be appointed to each role only once. The start and end dates
-- of each appointment to a role are always known in advance and recorded.

CREATE TABLE Role (
    ID serial PRIMARY KEY,
    Title varchar(100) NOT NULL,
    Salary money NOT NULL
);

CREATE TABLE Serve_in (
    MemberID INT REFERENCES Member(ID),
    RoleID INT REFERENCES Role(ID),
    Start_date date NOT NULL,
    End_date date NOT NULL,
    PRIMARY KEY (MemberID, RoleID)
);

-- The WASP party keeps track of other political parties, both domestically and abroad.
-- For each party, the country and name are a unique identifier, but the party also has
-- an ID that serves as a primary key. For each such party, at each time (represented
-- by start and end dates), exactly one WASP member monitors the developments in
-- the external party.

CREATE TABLE Party (
    ID serial,
    MemberID INT NOT NULL REFERENCES Member(ID),
    Country varchar(100) NOT NULL,
    Name varchar(100) NOT NULL,
    Start_date date NOT NULL,
    End_date date NOT NULL,
    OpponentID INT REFERENCES Opponent(ID),
    PRIMARY KEY (ID, Start_date)
);

-- The WASP party has sponsors. Each sponsor has an ID, name, address, and industry
-- attribute. Each sponsor may give grants to a number of WASP members. For each
-- grant, the date the grant is awarded is registered, as well as the amount and a text
-- field called ‘payback’ that describes what the sponsor expects in return. Each sponsor
-- may give multiple grants to multiple members, and each member can receive multiple
-- grants from multiple sponsors. However, each grant is for a single person and each
-- sponsor can give multiple sponsorships to each member, but at most one per day.

CREATE TABLE Sponsor (
    ID serial PRIMARY KEY,
    Name varchar(100) NOT NULL,
    Address varchar(255) NOT NULL,
    Industry varchar(100) NOT NULL
);

CREATE TABLE Grant (
    SponsorID INT REFERENCES Sponsor(ID),
    MemberID INT REFERENCES Member(ID),
    Date date NOT NULL,
    Amount money NOT NULL,
    Payback varchar(255) NOT NULL,
    PRIMARY KEY (SponsorID, MemberID, Date)
);

-- Each grant may be reviewed by one member of WASP. The date of the review is
-- decided when the grant is registered, typically one year in the future. At review time,
-- the grant is assigned a numerical grade from 1 to 10, depending on how well the
-- WASP member executed the payback.

CREATE TABLE Reviews (
    SponsorID INT REFERENCES Sponsor(ID),
    MemberID INT REFERENCES Member(ID),
    MemberID_other INT NOT NULL REFERENCES Member(ID),
    Date date NOT NULL,
    Grade INT NOT NULL,
    FOREIGN KEY (SponsorID, MemberID) REFERENCES Grant(SponsorID, MemberID),
    PRIMARY KEY (SponsorID, MemberID)
);

-- All parties and all enemies are two categories of opponents; opponents have an ID.
-- Some WASP members may be assigned to oppose opponents. This opposition appointment
-- has a start date and an end date (the latter may be unknown in the case of
-- open-ended assignments).

CREATE TABLE Opponent (
    ID serial PRIMARY KEY,
);

CREATE TABLE Opposes (
    MemberID INT REFERENCES Member(ID),
    OpponentID INT REFERENCES Opponent(ID),
    Start_date date NOT NULL,
    End_date date DEFAULT NULL,
    PRIMARY KEY (MemberID, OpponentID)
);