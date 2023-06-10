drop table if exists connect cascade;
drop table if exists friends cascade;
drop table if exists worlds cascade;
drop table if exists gods cascade;
drop table if exists superheros cascade;

CREATE TABLE Gods (
    gid INT PRIMARY KEY,
    name VARCHAR NOT NULL,
);