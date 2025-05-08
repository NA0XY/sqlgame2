-- Create Person table
CREATE TABLE Person (
    PersonID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Address TEXT,
    Age INTEGER,
    Occupation TEXT
);

-- Create Crime table
CREATE TABLE Crime (
    CrimeID INTEGER PRIMARY KEY,
    Date TEXT,
    Location TEXT,
    Description TEXT,
    VictimID INTEGER,
    FOREIGN KEY (VictimID) REFERENCES Person(PersonID)
);

-- Create Evidence table
CREATE TABLE Evidence (
    EvidenceID INTEGER PRIMARY KEY,
    Description TEXT,
    LocationFound TEXT,
    CrimeID INTEGER,
    FOREIGN KEY (CrimeID) REFERENCES Crime(CrimeID)
);

-- Create Interviews table
CREATE TABLE Interviews (
    InterviewID INTEGER PRIMARY KEY,
    PersonID INTEGER,
    Statement TEXT,
    Date TEXT,
    InterviewerID INTEGER,
    FOREIGN KEY (PersonID) REFERENCES Person(PersonID),
    FOREIGN KEY (InterviewerID) REFERENCES Person(PersonID)
);

-- Create Alibis table
CREATE TABLE Alibis (
    AlibiID INTEGER PRIMARY KEY,
    PersonID INTEGER,
    Location TEXT,
    StartTime TEXT,
    EndTime TEXT,
    Witnesses TEXT,
    FOREIGN KEY (PersonID) REFERENCES Person(PersonID)
);

-- Create Relationships table
CREATE TABLE Relationships (
    RelationshipID INTEGER PRIMARY KEY,
    Person1ID INTEGER,
    Person2ID INTEGER,
    RelationType TEXT,
    FOREIGN KEY (Person1ID) REFERENCES Person(PersonID),
    FOREIGN KEY (Person2ID) REFERENCES Person(PersonID)
);

-- Create PhoneRecords table
CREATE TABLE PhoneRecords (
    CallID INTEGER PRIMARY KEY,
    CallerID INTEGER,
    ReceiverID INTEGER,
    Duration INTEGER,
    Date TEXT,
    FOREIGN KEY (CallerID) REFERENCES Person(PersonID),
    FOREIGN KEY (ReceiverID) REFERENCES Person(PersonID)
);
