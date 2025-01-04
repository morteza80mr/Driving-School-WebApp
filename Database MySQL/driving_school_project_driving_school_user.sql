CREATE DATABASE  IF NOT EXISTS `driving_school_project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `driving_school_project`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: driving_school_project
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `driving_school_user`
--

DROP TABLE IF EXISTS `driving_school_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `driving_school_user` (
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `username` varchar(10) NOT NULL,
  `first_name_user` varchar(60) NOT NULL,
  `family_name_user` varchar(120) NOT NULL,
  `National_ID_user` varchar(10) NOT NULL,
  `User_role` varchar(1) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `driving_school_user`
--

LOCK TABLES `driving_school_user` WRITE;
/*!40000 ALTER TABLE `driving_school_user` DISABLE KEYS */;
INSERT INTO `driving_school_user` VALUES ('pbkdf2_sha256$320000$VixGiFM9OD03VLwV1RG26o$ywVUezd86GZu3LlhIEB/h7uYPflTQhLmO1O3ZjtShFQ=','2022-07-09 08:49:45.198014',0,'','','',0,1,'2022-06-06 12:13:40.000000','0','علی','جابری','0','M'),('pbkdf2_sha256$320000$ne7DW3M1fuTkrz7u0bTsEy$7jlrKr2X2wX5xGykg9j4qR8Wp/xqR6wGHGJJPLR7RQA=','2022-07-09 08:51:06.826877',0,'','','',0,1,'2022-06-06 12:38:03.745467','1','زهرا','نمکدار','1','R'),('pbkdf2_sha256$320000$urbS0cRoplIyt8MXYZBhXk$+gKbQ8OE++IrYPEf783LqJ/xpt4fZRiT5t/kD61IyAw=','2022-07-09 08:52:08.310052',0,'','','',0,1,'2022-06-06 12:46:08.222691','2','علی','شفیعی','2','C'),('pbkdf2_sha256$320000$UoIdUFFp13U7KwGAKl5NtS$UY1EgrAUUZS5LJoNB/rIBRuwhcscK0BsdxuRhAJvSW0=','2022-07-09 09:23:38.631427',0,'','','',0,1,'2022-06-06 12:46:35.255224','3','محمد','قهرمانی','3','T'),('pbkdf2_sha256$320000$PXxe5hY8UeyQj8LW75ykNz$G0aWoKnZ/Qq5Fcdh12jnlpwUnezfaz28aeu4SW5VBtA=','2022-07-09 09:22:45.315043',0,'','','',0,1,'2022-06-06 13:00:35.122214','4','جواد','هنردوست','4','S'),('pbkdf2_sha256$320000$mnbNjB7Rw77T2mRzPg7ZIp$LeKbPJsHo2iYjsZlmTnW6bk7ekPcxjkb9UCFO1xYlYM=','2022-07-09 08:51:39.811966',0,'','','',0,1,'2022-06-06 20:06:48.934554','5','آرین','طلایی','5','F'),('pbkdf2_sha256$320000$MzIqHdwBT3w8fzRezmOQk1$gVCW7evpxveI8afoyE0Aj0S6m+SJtyTKnFV6jKVaZhU=','2022-07-09 09:23:08.172725',1,'','','admin@domain.com',1,1,'2022-06-06 11:52:53.038866','admin','','','','');
/*!40000 ALTER TABLE `driving_school_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-10  0:20:10
