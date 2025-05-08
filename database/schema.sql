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
-- Table structure for table `alibis`
--

DROP TABLE IF EXISTS `alibis`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alibis` (
  `AlibiID` int NOT NULL,
  `PersonID` int DEFAULT NULL,
  `Location` varchar(255) DEFAULT NULL,
  `StartTime` datetime DEFAULT NULL,
  `EndTime` datetime DEFAULT NULL,
  `Witnesses` text,
  PRIMARY KEY (`AlibiID`),
  KEY `PersonID` (`PersonID`),
  CONSTRAINT `alibis_ibfk_1` FOREIGN KEY (`PersonID`) REFERENCES `person` (`PersonID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `crime`
--

DROP TABLE IF EXISTS `crime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `crime` (
  `CrimeID` int NOT NULL,
  `Date` date DEFAULT NULL,
  `Location` varchar(255) DEFAULT NULL,
  `Description` text,
  `VictimID` int DEFAULT NULL,
  PRIMARY KEY (`CrimeID`),
  KEY `VictimID` (`VictimID`),
  CONSTRAINT `crime_ibfk_1` FOREIGN KEY (`VictimID`) REFERENCES `person` (`PersonID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `evidence`
--

DROP TABLE IF EXISTS `evidence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `evidence` (
  `EvidenceID` int NOT NULL,
  `Description` text,
  `LocationFound` varchar(255) DEFAULT NULL,
  `CrimeID` int DEFAULT NULL,
  PRIMARY KEY (`EvidenceID`),
  KEY `CrimeID` (`CrimeID`),
  CONSTRAINT `evidence_ibfk_1` FOREIGN KEY (`CrimeID`) REFERENCES `crime` (`CrimeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `interviews`
--

DROP TABLE IF EXISTS `interviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interviews` (
  `InterviewID` int NOT NULL,
  `PersonID` int DEFAULT NULL,
  `Statement` text,
  `Date` date DEFAULT NULL,
  `InterviewerID` int DEFAULT NULL,
  PRIMARY KEY (`InterviewID`),
  KEY `PersonID` (`PersonID`),
  KEY `InterviewerID` (`InterviewerID`),
  CONSTRAINT `interviews_ibfk_1` FOREIGN KEY (`PersonID`) REFERENCES `person` (`PersonID`),
  CONSTRAINT `interviews_ibfk_2` FOREIGN KEY (`InterviewerID`) REFERENCES `person` (`PersonID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `PersonID` int NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Age` int DEFAULT NULL,
  `Occupation` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`PersonID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `phonerecords`
--

DROP TABLE IF EXISTS `phonerecords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phonerecords` (
  `CallID` int NOT NULL,
  `CallerID` int DEFAULT NULL,
  `ReceiverID` int DEFAULT NULL,
  `Duration` int DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  PRIMARY KEY (`CallID`),
  KEY `CallerID` (`CallerID`),
  KEY `ReceiverID` (`ReceiverID`),
  CONSTRAINT `phonerecords_ibfk_1` FOREIGN KEY (`CallerID`) REFERENCES `person` (`PersonID`),
  CONSTRAINT `phonerecords_ibfk_2` FOREIGN KEY (`ReceiverID`) REFERENCES `person` (`PersonID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `relationships`
--

DROP TABLE IF EXISTS `relationships`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `relationships` (
  `RelationshipID` int NOT NULL,
  `Person1ID` int DEFAULT NULL,
  `Person2ID` int DEFAULT NULL,
  `RelationType` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`RelationshipID`),
  KEY `Person1ID` (`Person1ID`),
  KEY `Person2ID` (`Person2ID`),
  CONSTRAINT `relationships_ibfk_1` FOREIGN KEY (`Person1ID`) REFERENCES `person` (`PersonID`),
  CONSTRAINT `relationships_ibfk_2` FOREIGN KEY (`Person2ID`) REFERENCES `person` (`PersonID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-08 13:22:50
