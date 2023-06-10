create table E2 (
	E2ID int primary key
);

create table E1 (
	E1ID int primary key,
	E2ID int not null references E2(E2ID)
);

create table E3 (
	E3ID int primary key,
	E1ID int not null references E1(E1ID)
);

create table E4 (
	E4ID int primary key
);

create table E5 (
	E5ID int primary key
);

-- R3 is normally not implemented
-- normally implemented as a foreign key in E4
create table R3 (
	E4ID int primary key references E4(E4ID),
	E5ID int not null references E5(E5ID)
);

create table R2 (
	E1ID int references E1(E1ID),
	E4ID int references R3(E4ID),
	primary key (E1ID, E4ID)
);

