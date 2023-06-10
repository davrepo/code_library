drop table if exists connect cascade;
drop table if exists friends cascade;
drop table if exists worlds cascade;
drop table if exists gods cascade;
drop table if exists superheros cascade;

CREATE TABLE Gods (
    gid INT PRIMARY KEY,
    name VARCHAR NOT NULL,
);

CREATE TABLE Wormholes (
    wormid INT PRIMARY KEY,
    gid INT NOT NULL REFERENCES Gods(gid),
    name VARCHAR NOT NULL,
);

CREATE TABLE Worlds (
    wid INT PRIMARY KEY,
    name VARCHAR NOT NULL,
);

CREATE TABLE Connect (
    wid1 INT REFERENCES Worlds(wid),
    wid2 INT REFERENCES Worlds(wid),
    wormid INT UNIQUE NOT NULL REFERENCES Wormholes(wormid),
    PRIMARY KEY (wid1, wid2)
);

CREATE TABLE Superheros (
    sid INT PRIMARY KEY,
    name VARCHAR NOT NULL,
    wid INT NOT NULL REFERENCES Worlds(wid)
);

CREATE TABLE FriendsWith (
    sid INT REFERENCES Superheros(sid),
    gid INT REFERENCES Gods(gid),
    PRIMARY KEY (sid, gid)
);