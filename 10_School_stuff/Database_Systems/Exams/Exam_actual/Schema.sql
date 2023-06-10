DROP TABLE IF EXISTS Award;
CREATE TABLE Award (
  id INTEGER NOT NULL,
  contestId INTEGER DEFAULT NULL,
  description varchar(100) DEFAULT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Contest;
CREATE TABLE Contest (
  id INTEGER NOT NULL,
  edition varchar(10) DEFAULT NULL,
  name varchar(150) DEFAULT NULL,
  organizer varchar(50) DEFAULT NULL,
  year date DEFAULT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Dancer;
CREATE TABLE Dancer (
  id INTEGER NOT NULL,
  name varchar(150) DEFAULT NULL,
  email varchar(50) DEFAULT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS DancerAward;
CREATE TABLE DancerAward (
  dancerId INTEGER NOT NULL,
  awardId INTEGER NOT NULL,
  PRIMARY KEY (dancerId,awardId)
);

DROP TABLE IF EXISTS Rank;
CREATE TABLE Rank (
  dancerId INTEGER NOT NULL,
  contestId INTEGER NOT NULL,
  date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  level INTEGER DEFAULT NULL,
  rank INTEGER DEFAULT NULL,
  PRIMARY KEY (dancerId,contestId)
);
