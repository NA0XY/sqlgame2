-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: sql_murder_mystery
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `alibis`
--

LOCK TABLES `alibis` WRITE;
/*!40000 ALTER TABLE `alibis` DISABLE KEYS */;
INSERT INTO `alibis` VALUES (1,2,'Home','2025-05-01 23:00:00','2025-05-02 01:00:00','None'),(2,3,'Hotel Lobby','2025-05-01 22:30:00','2025-05-01 23:30:00','Sarah Davis'),(3,4,'Classroom','2025-05-01 21:00:00','2025-05-01 23:00:00','Students'),(4,5,'Kitchen','2025-05-01 20:00:00','2025-05-02 00:00:00','Chef Staff'),(5,6,'Documenting Hotel Art Collection','2025-05-01 23:45:00','2025-05-02 00:15:00','None');
/*!40000 ALTER TABLE `alibis` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `crime`
--

LOCK TABLES `crime` WRITE;
/*!40000 ALTER TABLE `crime` DISABLE KEYS */;
INSERT INTO `crime` VALUES (1,'2025-05-01','Downtown Hotel Room 302','Victim found dead with blunt force trauma to the head',1);
/*!40000 ALTER TABLE `crime` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `evidence`
--

LOCK TABLES `evidence` WRITE;
/*!40000 ALTER TABLE `evidence` DISABLE KEYS */;
INSERT INTO `evidence` VALUES (1,'Bloody knife','Hotel Room 302',1),(2,'Footprint near window','Hotel Room 302',1),(3,'Torn piece of fabric','Hotel Hallway',1),(4,'Email draft exposing journalistic fraud','Laura White\'s laptop',1),(5,'Ceremonial dagger (murder weapon)','Hotel Storage Room',1),(6,'Angry email to victim','Michael\'s Sent Folder',1);
/*!40000 ALTER TABLE `evidence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `interviews`
--

LOCK TABLES `interviews` WRITE;
/*!40000 ALTER TABLE `interviews` DISABLE KEYS */;
INSERT INTO `interviews` VALUES (1,2,'I heard a loud noise around midnight.','2025-05-02',7),(2,3,'I saw someone leaving the hotel late at night.','2025-05-02',7),(3,4,'Michael seemed nervous when I interviewed him.','2025-05-02',7),(4,5,'I was in the kitchen all night.','2025-05-02',7),(5,6,'I was documenting hotel art pieces that night. Saw nothing suspicious.','2025-05-02',7),(6,7,'Security footage shows someone matching Laura\'s description accessing storage room at 23:45','2025-05-03',7);
/*!40000 ALTER TABLE `interviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (1,'John Smith','123 Main St',45,'Businessman'),(2,'Emily Johnson','456 Oak Ave',32,'Doctor'),(3,'Michael Brown','789 Pine Rd',38,'Lawyer'),(4,'Sarah Davis','321 Maple St',29,'Teacher'),(5,'David Wilson','654 Elm St',40,'Chef'),(6,'Laura White','987 Cedar Ln',35,'Journalist'),(7,'James Green','159 Oak Dr',50,'Detective');
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `phonerecords`
--

LOCK TABLES `phonerecords` WRITE;
/*!40000 ALTER TABLE `phonerecords` DISABLE KEYS */;
INSERT INTO `phonerecords` VALUES (1,3,2,5,'2025-05-01 22:00:00'),(2,2,3,3,'2025-05-01 22:05:00'),(3,5,4,10,'2025-05-01 21:30:00'),(4,6,1,2,'2025-05-01 23:50:00'),(5,6,1,72,'2025-05-01 23:48:00');
/*!40000 ALTER TABLE `phonerecords` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `relationships`
--

LOCK TABLES `relationships` WRITE;
/*!40000 ALTER TABLE `relationships` DISABLE KEYS */;
INSERT INTO `relationships` VALUES (1,1,2,'Friend'),(2,1,3,'Business Rival'),(3,2,4,'Colleague'),(4,3,5,'Acquaintance'),(5,6,1,'Reporter-Victim'),(6,6,1,'Investigation Subject'),(7,2,1,'Medical Consultant');
/*!40000 ALTER TABLE `relationships` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-08 13:23:12
