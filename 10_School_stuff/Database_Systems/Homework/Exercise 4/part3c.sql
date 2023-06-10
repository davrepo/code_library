-- create normalized tables
-- projects_id(id, mid)
-- projects_pid(pid, pn)
-- projects_sid(sid, sn)
-- projects_id_pid_sid(id, pid, sid)
-- projects_mid(mid, mn)

-- Create normalized tables

-- Table for mid -> mn
CREATE TABLE projects_mid (
    mid INT PRIMARY KEY,
    mn VARCHAR(255)
);

-- Table for id -> mid, id -> mn
CREATE TABLE projects_id (
    id INT PRIMARY KEY,
    mid INT, 
    FOREIGN KEY (mid) REFERENCES projects_mid(mid)
);

-- Table for pid -> pn
CREATE TABLE projects_pid (
    pid INT PRIMARY KEY,
    pn VARCHAR(255)
);

-- Table for sid -> sn
CREATE TABLE projects_sid (
    sid INT PRIMARY KEY,
    sn VARCHAR(255)
);

-- Table for id, pid, sid
CREATE TABLE projects_id_pid_sid (
    id INT,
    pid INT,
    sid INT,
    PRIMARY KEY (id, pid, sid),
    FOREIGN KEY (id) REFERENCES projects_id(id),
    FOREIGN KEY (pid) REFERENCES projects_pid(pid),
    FOREIGN KEY (sid) REFERENCES projects_sid(sid)
);

-- Extract data from the original 'projects' table and insert it into the normalized tables

-- Insert data into projects_mid
INSERT INTO projects_mid (mid, mn)
SELECT DISTINCT mid, mn
FROM projects;

-- Insert data into projects_id
INSERT INTO projects_id (id, mid)
SELECT DISTINCT id, mid
FROM projects;

-- Insert data into projects_pid
INSERT INTO projects_pid (pid, pn)
SELECT DISTINCT pid, pn
FROM projects;

-- Insert data into projects_sid
INSERT INTO projects_sid (sid, sn)
SELECT DISTINCT sid, sn
FROM projects;

-- Insert data into projects_id_pid_sid
INSERT INTO projects_id_pid_sid (id, pid, sid)
SELECT DISTINCT id, pid, sid
FROM projects;

