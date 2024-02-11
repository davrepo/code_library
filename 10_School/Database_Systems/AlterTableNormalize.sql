-- rentals_pid(pid, pn)
-- rentals_hid(hid, hs, hz)
-- rentals_hz(hz, hc)
-- rentals_joinPreserve(pid, hid)
-- pid INT, hid INT, pn VARCHAR(50), s INT, hs VARCHAR(50), hz INT, hc VARCHAR(50)

CREATE TABLE rentals_pid(
    pid INT PRIMARY KEY,
    pn VARCHAR(50)
);

CREATE TABLE rentals_hid(
    hid INT PRIMARY KEY,
    hs VARCHAR(50),
    hz INT FOREIGN KEY REFERENCES rentals_hz(hz)
);

CREATE TABLE rentals_hz(
    hz INT PRIMARY KEY,
    hc VARCHAR(50)
);

CREATE TABLE rentals_joinPreserve(
    pid INT REFERENCES rentals_pid(pid),
    hid INT REFERENCES rentals_hid(hid)
    PRIMARY KEY(pid, hid)
);

-- Inserting data into the tables
INSERT INTO rentals_pid
SELECT DISTINCT pid, pn
FROM rentals;

INSERT INTO rentals_hz
SELECT DISTINCT hz, hc
FROM rentals;

INSERT INTO rentals_hid
SELECT DISTINCT hid, hs, hz
FROM rentals;

INSERT INTO rentals_joinPreserve
SELECT DISTINCT pid, hid
FROM rentals;

