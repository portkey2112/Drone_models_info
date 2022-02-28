-- MySQL dump 10.13  Distrib 8.0.28, for macos11 (x86_64)
--
-- Host: localhost    Database: drones_info
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `automation_features`
--

DROP TABLE IF EXISTS `automation_features`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `automation_features` (
  `auto_feat_ID` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`auto_feat_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `automation_features`
--

LOCK TABLES `automation_features` WRITE;
/*!40000 ALTER TABLE `automation_features` DISABLE KEYS */;
INSERT INTO `automation_features` VALUES (1,'GNSS navigation','Thanks to several positioning system available (GPS, Glonass, Galileo, Beidu, etc.), our UAVs perform GNSS-assisted missions.'),(2,'Waypoint flying','The most common operation performed with UAVs depends on 3D coordinates (longitude, latitude and altitude).'),(3,'Auto take-off & landing','Our systems can perform fully automated flights including take-off and landing.'),(9,'Altitude hold','This flight mode is designed for complex missions requiring altitude hold assistance.'),(10,'Boat mode [advanced]','This is an advanced feature that allows the pilot to initialize the solid state gyroscopes for safe flight even when the drone is resting on a moving boat or platform.'),(200,'dfdsfh','djhfdkshf'),(20000,'sjfdhfdskj','dshfkdshfdshkjfahdfhdk');
/*!40000 ALTER TABLE `automation_features` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `company_id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'DRDO'),(2,'Intel'),(3,'DJI'),(200,'dfdsfh'),(20000,'dfddsfh');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `country`
--

DROP TABLE IF EXISTS `country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `country` (
  `country_ID` int NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`country_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `country`
--

LOCK TABLES `country` WRITE;
/*!40000 ALTER TABLE `country` DISABLE KEYS */;
INSERT INTO `country` VALUES (1,'India'),(2,'Europe'),(3,'France'),(200,'dfdsfh');
/*!40000 ALTER TABLE `country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cv_algorithm`
--

DROP TABLE IF EXISTS `cv_algorithm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cv_algorithm` (
  `algo_ID` int NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`algo_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cv_algorithm`
--

LOCK TABLES `cv_algorithm` WRITE;
/*!40000 ALTER TABLE `cv_algorithm` DISABLE KEYS */;
INSERT INTO `cv_algorithm` VALUES (1,'Object detection'),(2,'counting'),(3,'segmentaion'),(4,'tracking'),(14,'autonomous driving'),(200,'dfdsfh');
/*!40000 ALTER TABLE `cv_algorithm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `domain`
--

DROP TABLE IF EXISTS `domain`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `domain` (
  `domain_ID` int NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`domain_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `domain`
--

LOCK TABLES `domain` WRITE;
/*!40000 ALTER TABLE `domain` DISABLE KEYS */;
INSERT INTO `domain` VALUES (1,'agriculture'),(2,'human health'),(3,'marine_health'),(9,'military'),(10,'1'),(200,'dfdsfh');
/*!40000 ALTER TABLE `domain` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drone_models`
--

DROP TABLE IF EXISTS `drone_models`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drone_models` (
  `ID` int NOT NULL,
  `Name` varchar(255) NOT NULL,
  `company_id` int NOT NULL,
  `height` int DEFAULT NULL,
  `users` varchar(255) DEFAULT NULL,
  `license` tinyint(1) DEFAULT NULL,
  `training` tinyint(1) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `weight_in_kg` float DEFAULT NULL,
  `country_of_operation_ID` int DEFAULT NULL,
  `domain_ID` int NOT NULL,
  `usecase` varchar(255) NOT NULL,
  `wingspan` float DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `company_id` (`company_id`),
  KEY `country_of_operation_ID` (`country_of_operation_ID`),
  KEY `domain_ID` (`domain_ID`),
  CONSTRAINT `drone_models_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company` (`company_id`),
  CONSTRAINT `drone_models_ibfk_2` FOREIGN KEY (`country_of_operation_ID`) REFERENCES `country` (`country_ID`),
  CONSTRAINT `drone_models_ibfk_3` FOREIGN KEY (`domain_ID`) REFERENCES `domain` (`domain_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drone_models`
--

LOCK TABLES `drone_models` WRITE;
/*!40000 ALTER TABLE `drone_models` DISABLE KEYS */;
INSERT INTO `drone_models` VALUES (1,'Ghatak',1,NULL,'indian_govt',1,1,NULL,NULL,1,9,'stealth combat (military)',NULL),(200,'dfdsfh',1,1,'sfdds',0,0,0,0,1,1,'werr',0);
/*!40000 ALTER TABLE `drone_models` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pair_drone_automation_feature`
--

DROP TABLE IF EXISTS `pair_drone_automation_feature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pair_drone_automation_feature` (
  `drone_ID` int NOT NULL,
  `auto_feat_ID` int NOT NULL,
  KEY `auto_feat_ID` (`auto_feat_ID`),
  CONSTRAINT `pair_drone_automation_feature_ibfk_1` FOREIGN KEY (`auto_feat_ID`) REFERENCES `automation_features` (`auto_feat_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pair_drone_automation_feature`
--

LOCK TABLES `pair_drone_automation_feature` WRITE;
/*!40000 ALTER TABLE `pair_drone_automation_feature` DISABLE KEYS */;
INSERT INTO `pair_drone_automation_feature` VALUES (1,2),(1,3),(1,9),(1,10),(1,1),(200,1),(200,1),(200,1);
/*!40000 ALTER TABLE `pair_drone_automation_feature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pair_drone_country`
--

DROP TABLE IF EXISTS `pair_drone_country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pair_drone_country` (
  `drone_id` int NOT NULL,
  `country_id` int NOT NULL,
  KEY `country_id` (`country_id`),
  CONSTRAINT `pair_drone_country_ibfk_1` FOREIGN KEY (`country_id`) REFERENCES `country` (`country_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pair_drone_country`
--

LOCK TABLES `pair_drone_country` WRITE;
/*!40000 ALTER TABLE `pair_drone_country` DISABLE KEYS */;
INSERT INTO `pair_drone_country` VALUES (1,1),(200,1);
/*!40000 ALTER TABLE `pair_drone_country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pair_drone_cv_algo`
--

DROP TABLE IF EXISTS `pair_drone_cv_algo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pair_drone_cv_algo` (
  `drone_ID` int NOT NULL,
  `cv_algo_ID` int NOT NULL,
  KEY `cv_algo_ID` (`cv_algo_ID`),
  CONSTRAINT `pair_drone_cv_algo_ibfk_1` FOREIGN KEY (`cv_algo_ID`) REFERENCES `cv_algorithm` (`algo_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pair_drone_cv_algo`
--

LOCK TABLES `pair_drone_cv_algo` WRITE;
/*!40000 ALTER TABLE `pair_drone_cv_algo` DISABLE KEYS */;
INSERT INTO `pair_drone_cv_algo` VALUES (1,3),(1,4),(1,14),(200,1);
/*!40000 ALTER TABLE `pair_drone_cv_algo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pair_drone_security_feature`
--

DROP TABLE IF EXISTS `pair_drone_security_feature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pair_drone_security_feature` (
  `drone_ID` int NOT NULL,
  `sec_feat_ID` int NOT NULL,
  KEY `sec_feat_ID` (`sec_feat_ID`),
  CONSTRAINT `pair_drone_security_feature_ibfk_1` FOREIGN KEY (`sec_feat_ID`) REFERENCES `security_features` (`sec_feat_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pair_drone_security_feature`
--

LOCK TABLES `pair_drone_security_feature` WRITE;
/*!40000 ALTER TABLE `pair_drone_security_feature` DISABLE KEYS */;
INSERT INTO `pair_drone_security_feature` VALUES (1,3),(1,5),(1,6),(1,8),(1,9),(1,11);
/*!40000 ALTER TABLE `pair_drone_security_feature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample`
--

DROP TABLE IF EXISTS `sample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sample` (
  `col1` int NOT NULL,
  `col2` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample`
--

LOCK TABLES `sample` WRITE;
/*!40000 ALTER TABLE `sample` DISABLE KEYS */;
INSERT INTO `sample` VALUES (1,1),(2,2),(3,NULL),(22,22),(22,12),(22,10),(22,220);
/*!40000 ALTER TABLE `sample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `security_features`
--

DROP TABLE IF EXISTS `security_features`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `security_features` (
  `sec_feat_ID` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `decription` text NOT NULL,
  PRIMARY KEY (`sec_feat_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `security_features`
--

LOCK TABLES `security_features` WRITE;
/*!40000 ALTER TABLE `security_features` DISABLE KEYS */;
INSERT INTO `security_features` VALUES (1,'Encryption','Discretion and data protection can be necessary. In such case, it is possible to benefit from encrypted data like for the video link.'),(2,'Nextgen GNSS','Thanks to GNSS receivers integrating latest positioning systems like Galileo, our systems have reliable, high speed and strong satellite link. This ensures quality positioning information at all time.'),(3,'Alerts','A range of alerts helps the pilot by warning him about important matters like altitude limits, battery level, etc.'),(5,'Emergency landing spots','In case the UAV is far away and an emergency landing is necessary, it lands to a known and safe location, as defined prior to departure.'),(6,'Geofencing','Airspace is divided and shared. Geofencing enforces the respect of this by setting a virtual cage in which the system is allowed to fly. Indeed, it keeps the system from exiting the specific operational airspace.'),(8,'Emergency failsafe recovery','In case battery drops to a critical limit or contact is lost with the UAV, emergency failsafe procedures will be executed. They allow to ensure system integrity automatically like by performing automatic emergency landings.'),(9,'Flight data logging','For post-flight analysis purposes, system data are stored internally, on a microSD card. Logged in high frequency, these data contains relevant information including position, height, speed, voltage, attitude, flight mode, current, temperature, pilot inputs, IMU values, etc. Thanks to this, it is possible to make and verify hypothesis.'),(11,'Redundant flight control ','For safety enhancement, our UAVs can be equipped with a second independent flight control board.');
/*!40000 ALTER TABLE `security_features` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-23 14:58:33
