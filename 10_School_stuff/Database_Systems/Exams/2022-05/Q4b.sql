create table Mythologies (
	MID int primary key,
	mname varchar not null
);

create table EconomicTheories (
	MID int primary key references Mythologies(MID),
	author varchar not null
);

create table Religions (
	MID int primary key references Mythologies(MID),
	origincountry varchar not null
);

create table Servants (
	SID int primary key,
	sname varchar not null,
);

create table People (
	PID int primary key,
	pname varchar not null
	MID int not null references Religions(MID)
);

create table Serve (
	MID int not null references Mythologies (MID),
	SID int not null references Servants (SID),
	price int not null,
	primary key (MID, SID)
);

create table Attack (
	PID int references People (PID),
	MID int,
	SID int,
	primary key (PID, MID, SID),
	foreign key (MID, SID) references Serve (MID, SID)
);
