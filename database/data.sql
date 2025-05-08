-- Insert data into Person table
INSERT INTO Person (PersonID, Name, Address, Age, Occupation) VALUES
(1, 'John Smith', '123 Main St', 45, 'Businessman'),
(2, 'Emily Johnson', '456 Oak Ave', 32, 'Doctor'),
(3, 'Michael Brown', '789 Pine Rd', 38, 'Lawyer'),
(4, 'Sarah Davis', '321 Maple St', 29, 'Teacher'),
(5, 'David Wilson', '654 Elm St', 40, 'Chef'),
(6, 'Laura White', '987 Cedar Ln', 35, 'Journalist'),
(7, 'James Green', '159 Oak Dr', 50, 'Detective');

-- Insert data into Crime table
INSERT INTO Crime (CrimeID, Date, Location, Description, VictimID) VALUES
(1, '2025-05-01', 'Downtown Hotel Room 302', 'Victim found dead with blunt force trauma to the head', 1);

-- Insert data into Evidence table
INSERT INTO Evidence (EvidenceID, Description, LocationFound, CrimeID) VALUES
(1, 'Bloody knife', 'Hotel Room 302', 1),
(2, 'Footprint near window', 'Hotel Room 302', 1),
(3, 'Torn piece of fabric', 'Hotel Hallway', 1),
(4, 'Email draft exposing journalistic fraud', 'Victim''s laptop', 1),
(5, 'Ceremonial dagger (murder weapon)', 'Hotel Storage Room', 1),
(6, 'Angry email to victim', 'Michael''s Sent Folder', 1);

-- Insert data into Interviews table
INSERT INTO Interviews (InterviewID, PersonID, Statement, Date, InterviewerID) VALUES
(1, 2, 'I heard a loud noise around midnight.', '2025-05-02', 7),
(2, 3, 'I saw someone leaving the hotel late at night.', '2025-05-02', 7),
(3, 4, 'Michael seemed nervous when I interviewed him.', '2025-05-02', 7),
(4, 5, 'I was in the kitchen all night.', '2025-05-02', 7),
(5, 6, 'I was documenting hotel art pieces that night. Saw nothing suspicious.', '2025-05-02', 7),
(6, 7, 'Security footage shows someone matching Laura''s description accessing storage room at 23:45', '2025-05-03', 7);

-- Insert data into Alibis table
INSERT INTO Alibis (AlibiID, PersonID, Location, StartTime, EndTime, Witnesses) VALUES
(1, 2, 'Home', '2025-05-01 23:00:00', '2025-05-02 01:00:00', 'None'),
(2, 3, 'Hotel Lobby', '2025-05-01 22:30:00', '2025-05-01 23:30:00', 'Sarah Davis'),
(3, 4, 'Classroom', '2025-05-01 21:00:00', '2025-05-01 23:00:00', 'Students'),
(4, 5, 'Kitchen', '2025-05-01 20:00:00', '2025-05-02 00:00:00', 'Chef Staff'),
(5, 6, 'Documenting Hotel Art Collection', '2025-05-01 23:30:00', '2025-05-02 00:30:00', 'None');

-- Insert data into Relationships table
INSERT INTO Relationships (RelationshipID, Person1ID, Person2ID, RelationType) VALUES
(1, 1, 2, 'Friend'),
(2, 1, 3, 'Business Rival'),
(3, 2, 4, 'Colleague'),
(4, 3, 5, 'Acquaintance'),
(5, 6, 1, 'Reporter-Victim'),
(6, 6, 1, 'Investigation Subject'),
(7, 2, 1, 'Medical Consultant');

-- Insert data into PhoneRecords table
INSERT INTO PhoneRecords (CallID, CallerID, ReceiverID, Duration, Date) VALUES
(1, 3, 2, 5, '2025-05-01 22:00:00'),
(2, 2, 3, 3, '2025-05-01 22:05:00'),
(3, 5, 4, 10, '2025-05-01 21:30:00'),
(4, 6, 1, 2, '2025-05-01 23:50:00'),
(5, 6, 1, 72, '2025-05-01 23:48:00');
