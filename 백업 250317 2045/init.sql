CREATE DATABASE  IF NOT EXISTS `erp_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `erp_db`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: erp_db
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
-- Table structure for table `accountbook`
--

DROP TABLE IF EXISTS `accountbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accountbook` (
  `bk_id` varchar(15) NOT NULL,
  `bk_date` date NOT NULL,
  `bk_type` varchar(4) NOT NULL,
  `bk_description` varchar(100) DEFAULT NULL,
  `bk_amount` bigint NOT NULL,
  `bk_create_date` date DEFAULT NULL,
  `bk_creater` varchar(20) DEFAULT NULL,
  `bk_approval_state` varchar(4) DEFAULT '미결',
  `bk_approval_date` date DEFAULT NULL,
  `bk_approval_p` varchar(20) DEFAULT NULL,
  `employee_code` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`bk_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accountbook`
--

LOCK TABLES `accountbook` WRITE;
/*!40000 ALTER TABLE `accountbook` DISABLE KEYS */;
INSERT INTO `accountbook` VALUES ('20250317030001','2025-03-17','대체전표','회사 시작',10000000,'2025-03-17',NULL,'승인','2025-03-17',NULL,NULL),('20250317030002','2025-03-17','대체전표','현금 계좌에 입금',4000000,'2025-03-17',NULL,'승인','2025-03-17',NULL,NULL),('20250325030001','2025-03-25','대체전표','직원 급여 분개',3000000,'2025-03-17',NULL,'승인','2025-03-17',NULL,NULL),('20250325030002','2025-03-25','대체전표','직원 급여 보통예금 계좌에서 지급',3000000,'2025-03-17',NULL,'승인','2025-03-17',NULL,NULL);
/*!40000 ALTER TABLE `accountbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accountsubject`
--

DROP TABLE IF EXISTS `accountsubject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accountsubject` (
  `account_code` int NOT NULL,
  `account_name` varchar(45) NOT NULL,
  `account_type` varchar(20) NOT NULL,
  PRIMARY KEY (`account_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accountsubject`
--

LOCK TABLES `accountsubject` WRITE;
/*!40000 ALTER TABLE `accountsubject` DISABLE KEYS */;
INSERT INTO `accountsubject` VALUES (101,'현금','자산'),(103,'보통예금','자산'),(107,'유가증권','자산'),(108,'외상매출금','자산'),(110,'받을어음','자산'),(114,'단기대여금','자산'),(120,'미수금','자산'),(131,'선급금','자산'),(135,'부가세대급금','자산'),(146,'상품','자산'),(150,'제품','자산'),(153,'원재료','자산'),(212,'비품','자산'),(239,'개발비','자산'),(253,'미지급금','부채'),(254,'예수금','부채'),(255,'부가세예수금','부채'),(259,'선수금','부채'),(262,'미지급비용','부채'),(263,'선수수익','부채'),(331,'자본금','자본'),(401,'상품매출','수익'),(404,'제품매출','수익'),(451,'상품매출원가','비용'),(455,'제품매출원가','비용'),(501,'재료비','비용'),(503,'급여(제조)','비용'),(504,'임금(제조)','비용'),(505,'상여금(제조)','비용'),(507,'잡급(제조)','비용'),(510,'퇴직급여','비용'),(511,'경비(제조)','비용'),(801,'급여','비용'),(803,'상여금','비용'),(811,'경비','비용'),(813,'세금과공과금','비용'),(901,'이자수익','수익'),(930,'잡이익','수익');
/*!40000 ALTER TABLE `accountsubject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `analysis_report`
--

DROP TABLE IF EXISTS `analysis_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `analysis_report` (
  `report_id` int NOT NULL AUTO_INCREMENT,
  `analysis_reportcol` varchar(45) DEFAULT NULL,
  `estimated_cost` bigint NOT NULL,
  `actual_cost` bigint NOT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analysis_report`
--

LOCK TABLES `analysis_report` WRITE;
/*!40000 ALTER TABLE `analysis_report` DISABLE KEYS */;
INSERT INTO `analysis_report` VALUES (1,'12312321',100,1000),(2,'123',100,1000),(3,'ki',10,100),(4,'ki',10,100),(5,'aaa',1,3),(6,'aaa',1,2),(7,'bbb',2,3),(8,'과목test',400,500);
/*!40000 ALTER TABLE `analysis_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `approval`
--

DROP TABLE IF EXISTS `approval`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `approval` (
  `appr_id` int NOT NULL AUTO_INCREMENT,
  `appr_state` int NOT NULL,
  `appr_line1` tinyint NOT NULL,
  `appr_line2` tinyint NOT NULL,
  `appr_line3` tinyint NOT NULL,
  `employee_code` varchar(20) NOT NULL,
  `appr_type` varchar(30) NOT NULL,
  `appr_content` varchar(200) DEFAULT NULL,
  `appr_deny` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`appr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `approval`
--

LOCK TABLES `approval` WRITE;
/*!40000 ALTER TABLE `approval` DISABLE KEYS */;
/*!40000 ALTER TABLE `approval` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bom`
--

DROP TABLE IF EXISTS `bom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bom` (
  `bom_code` varchar(255) NOT NULL,
  `sop_code` varchar(255) DEFAULT NULL,
  `written_date` varchar(255) DEFAULT NULL,
  `order_code` varchar(255) DEFAULT NULL,
  `material_code` varchar(255) DEFAULT NULL,
  `material_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`bom_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bom`
--

LOCK TABLES `bom` WRITE;
/*!40000 ALTER TABLE `bom` DISABLE KEYS */;
INSERT INTO `bom` VALUES ('bom1','sop1','2025-03-14','order111','product222','완제품222'),('bom2','sop2','2025-03-15','order222','product333','완제품333'),('bom3','sop3','2025-03-16','order333','product444','완제품444'),('bom4','sop4','2025-03-14','order1234','product111','완제품111'),('bom5','','','','','');
/*!40000 ALTER TABLE `bom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bom_f`
--

DROP TABLE IF EXISTS `bom_f`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bom_f` (
  `bom_code` varchar(255) DEFAULT NULL,
  `material_code` varchar(255) DEFAULT NULL,
  `material_name` varchar(255) DEFAULT NULL,
  `quantity` varchar(255) DEFAULT NULL,
  `unit` varchar(255) DEFAULT NULL,
  `purchase_price` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bom_f`
--

LOCK TABLES `bom_f` WRITE;
/*!40000 ALTER TABLE `bom_f` DISABLE KEYS */;
INSERT INTO `bom_f` VALUES ('BOM001','680966','','5','',''),('BOM001','dfghsh1','','2','',''),('bom1','mat1','원자재1','','','(\',)');
/*!40000 ALTER TABLE `bom_f` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chat_room`
--

DROP TABLE IF EXISTS `chat_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chat_room` (
  `employee_code` varchar(20) NOT NULL,
  `room_code` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_room`
--

LOCK TABLES `chat_room` WRITE;
/*!40000 ALTER TABLE `chat_room` DISABLE KEYS */;
INSERT INTO `chat_room` VALUES ('e001','r001'),('e002','r001'),('e003','r001'),('e003','r002'),('e004','r002');
/*!40000 ALTER TABLE `chat_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companyfile`
--

DROP TABLE IF EXISTS `companyfile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companyfile` (
  `fiscal_year` varchar(50) NOT NULL,
  `business_registration_number` varchar(20) NOT NULL,
  `corporation_registration_number` int NOT NULL,
  `representative_foreign` tinyint(1) DEFAULT NULL,
  `representative_resident_number` varchar(13) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `detailed_address` varchar(50) DEFAULT NULL,
  `business_type` varchar(50) DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  `fax_number` varchar(20) DEFAULT NULL,
  `establishment_date` date DEFAULT NULL,
  `closed_date` date DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`fiscal_year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companyfile`
--

LOCK TABLES `companyfile` WRITE;
/*!40000 ALTER TABLE `companyfile` DISABLE KEYS */;
/*!40000 ALTER TABLE `companyfile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companyprofile`
--

DROP TABLE IF EXISTS `companyprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companyprofile` (
  `FY` varchar(50) NOT NULL,
  `coperationNumber` int DEFAULT NULL,
  `representativeNumber` varchar(50) DEFAULT NULL,
  `proprietor` tinyint(1) DEFAULT NULL,
  `resodentRegistrationNumber` varchar(13) DEFAULT NULL,
  `zipcode` varchar(10) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `particularAddress` varchar(50) DEFAULT NULL,
  `businessType` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `phoneNumber` varchar(50) DEFAULT NULL,
  `faxNumber` int DEFAULT NULL,
  `establishmentDate` date DEFAULT NULL,
  ` closedDownDate` date DEFAULT NULL,
  `userdOrNot` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`FY`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companyprofile`
--

LOCK TABLES `companyprofile` WRITE;
/*!40000 ALTER TABLE `companyprofile` DISABLE KEYS */;
/*!40000 ALTER TABLE `companyprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_management`
--

DROP TABLE IF EXISTS `customer_management`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer_management` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Customer_name` char(100) DEFAULT NULL,
  `business_number` int DEFAULT NULL,
  `Customer_code` char(100) DEFAULT NULL,
  `Type_business` char(100) DEFAULT NULL,
  `business_adress` char(250) DEFAULT NULL,
  `ContactPerson_name` char(100) DEFAULT NULL,
  `Country` char(50) DEFAULT NULL,
  `ContactPerson_phone` char(100) DEFAULT NULL,
  `e_mail` char(100) DEFAULT NULL,
  `Memo` char(250) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_management`
--

LOCK TABLES `customer_management` WRITE;
/*!40000 ALTER TABLE `customer_management` DISABLE KEYS */;
INSERT INTO `customer_management` VALUES (1,'zzz',NULL,'aaa',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'132',1321,'312321','국내매출거래처','231123 132132','321','한국','123','312','312'),(3,'132',123,'231','해외매입거래처','321 dsafasf','1321','중국','312','321','123	312312'),(4,'te',123,'tr','해외매출거래처','trert tre','tre','일본','tre','tre','tre	tre');
/*!40000 ALTER TABLE `customer_management` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employee_code` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `name_eng` varchar(50) DEFAULT NULL,
  `name_hanja` varchar(50) DEFAULT NULL,
  `e_mail` varchar(100) DEFAULT NULL,
  `zip_code` varchar(10) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `detail_address` varchar(255) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `emergency_number` varchar(20) DEFAULT NULL,
  `date_of_employment` date DEFAULT NULL,
  `date_of_retirement` date DEFAULT NULL,
  `employment_status` varchar(20) DEFAULT NULL,
  `employment_type` varchar(20) DEFAULT NULL,
  `department` varchar(50) DEFAULT NULL,
  `job_grade` varchar(50) DEFAULT NULL,
  `work_place` varchar(50) DEFAULT NULL,
  `basic_salary` int DEFAULT NULL,
  `allowance` int DEFAULT NULL,
  `bonus` int DEFAULT NULL,
  `account` varchar(50) DEFAULT NULL,
  `this_month_state` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`employee_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('e001','성진하','sung','성성성','@','1323','내맘속','깊은곳','01041234123',NULL,'2025-03-07',NULL,'재직','정규직','인사부','사원','asd',5000000,10000,10000,'123123',NULL),('e002','침팬치','dg651sdg','5gsd51','@','','박민환 집 주인','0000','0123123',NULL,'2025-03-17',NULL,'선택하세요','선택하세요','선택하세요','선택하세요','',500,10,5,'12',NULL),('e003','이이름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'인사부','사원',NULL,NULL,NULL,NULL,NULL,NULL),('e004','사사름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'인사부','사원',NULL,NULL,NULL,NULL,NULL,NULL),('e005','오오름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'인사부','대리',NULL,NULL,NULL,NULL,NULL,NULL),('e006','육육름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'인사부','과장',NULL,NULL,NULL,NULL,NULL,NULL),('e007','칠칠름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'인사부','부장',NULL,NULL,NULL,NULL,NULL,NULL),('e008','팔팔름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'영업부','사원',NULL,NULL,NULL,NULL,NULL,NULL),('e009','구구름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'영업부','대리',NULL,NULL,NULL,NULL,NULL,NULL),('e010','십십름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'영업부','사원',NULL,NULL,NULL,NULL,NULL,NULL),('e011','십일름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'영업부','부장',NULL,NULL,NULL,NULL,NULL,NULL),('e012','십이름',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'영업부','사장',NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `financial_report`
--

DROP TABLE IF EXISTS `financial_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `financial_report` (
  `financial_id` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(45) NOT NULL,
  `dr_cost` bigint DEFAULT NULL,
  `cr_cost` bigint DEFAULT NULL,
  PRIMARY KEY (`financial_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `financial_report`
--

LOCK TABLES `financial_report` WRITE;
/*!40000 ALTER TABLE `financial_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `financial_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incomel_report`
--

DROP TABLE IF EXISTS `incomel_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `incomel_report` (
  `income_id` int NOT NULL AUTO_INCREMENT,
  `subject` varchar(45) NOT NULL,
  `dr_cost` bigint DEFAULT NULL,
  `cr_cost` bigint DEFAULT NULL,
  PRIMARY KEY (`income_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incomel_report`
--

LOCK TABLES `incomel_report` WRITE;
/*!40000 ALTER TABLE `incomel_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `incomel_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `journalizingbook`
--

DROP TABLE IF EXISTS `journalizingbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `journalizingbook` (
  `jr_id` int NOT NULL AUTO_INCREMENT,
  `jr_type` varchar(2) NOT NULL,
  `account_code` varchar(5) NOT NULL,
  `account_name` varchar(45) DEFAULT NULL,
  `business_code` varchar(5) DEFAULT NULL,
  `business_client` varchar(45) DEFAULT NULL,
  `jr_dr` varchar(14) DEFAULT '0',
  `jr_cr` varchar(14) DEFAULT '0',
  `jr_description` varchar(100) DEFAULT NULL,
  `jr_evidence` varchar(6) DEFAULT NULL,
  `bk_id` varchar(15) DEFAULT NULL,
  `ti_id` varchar(15) DEFAULT NULL,
  `jr_base` varchar(2) NOT NULL,
  PRIMARY KEY (`jr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `journalizingbook`
--

LOCK TABLES `journalizingbook` WRITE;
/*!40000 ALTER TABLE `journalizingbook` DISABLE KEYS */;
INSERT INTO `journalizingbook` VALUES (1,'차변','101','현금','','','10000000','','','','20250317030001',NULL,'bk'),(2,'대변','331','자본금','','','','10000000','','','20250317030001',NULL,'bk'),(3,'차변','135','부가세대급금','','','100000','','','세금계산서',NULL,'20250317120001','ti'),(4,'대변','101','현금','','','','1100000','','',NULL,'20250317120001','ti'),(5,'차변','153','원재료','','','1000000','','','',NULL,'20250317120001','ti'),(6,'차변','103','보통예금','','국민은행','4000000','','','','20250317030002',NULL,'bk'),(7,'대변','101','현금','','','','4000000','','','20250317030002',NULL,'bk'),(8,'차변','801','급여','','','3000000','','','','20250325030001',NULL,'bk'),(9,'대변','254','예수금','','','','300000','소득세 등 예수금','','20250325030001',NULL,'bk'),(10,'대변','262','미지급비용','','','','2700000','','','20250325030001',NULL,'bk'),(11,'차변','254','예수금','','','300000','','','','20250325030002',NULL,'bk'),(12,'대변','103','보통예금','','','','3000000','','','20250325030002',NULL,'bk'),(13,'차변','262','미지급비용','','','2700000','','','','20250325030002',NULL,'bk'),(14,'대변','255','부가세예수금','','','','200000','','세금계산서',NULL,'20250320110001','ti'),(15,'차변','103','보통예금','','','2200000','','상품 매출 후 계좌로 입금 받음','',NULL,'20250320110001','ti'),(16,'대변','146','상품','','','','2000000','','',NULL,'20250320110001','ti');
/*!40000 ALTER TABLE `journalizingbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materialtable`
--

DROP TABLE IF EXISTS `materialtable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materialtable` (
  `materialCode` varchar(10) NOT NULL,
  `materialName` varchar(255) DEFAULT NULL,
  `materialType` varchar(10) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `sellingPrice` int DEFAULT NULL,
  `purchasePrice` int DEFAULT NULL,
  `unit` varchar(10) DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `correspondentCode` varchar(15) DEFAULT NULL,
  `correspondentName` varchar(15) DEFAULT NULL,
  `Date_up` varchar(10) DEFAULT NULL,
  `department` varchar(10) DEFAULT NULL,
  `manager` char(10) DEFAULT NULL,
  PRIMARY KEY (`materialCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materialtable`
--

LOCK TABLES `materialtable` WRITE;
/*!40000 ALTER TABLE `materialtable` DISABLE KEYS */;
INSERT INTO `materialtable` VALUES ('','','',NULL,NULL,NULL,'',NULL,'','','','',''),('123',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'이윤서'),('13456','m12314','',NULL,NULL,NULL,'',NULL,'','','','',''),('47484','fhgdh','완제품',100,1000,NULL,'',NULL,'','','','',''),('680966','dzdjzd','완제품',NULL,NULL,NULL,'',NULL,'','',NULL,'',''),('796969','hdhsdhs','',NULL,NULL,NULL,'',NULL,'1','',NULL,'',''),('8079','sgsg','완제품',NULL,NULL,NULL,'',NULL,'dg35','',NULL,'',''),('dddd','fhgdh','완제품',100,1000,NULL,'',NULL,'','','','',''),('dfghsh1','gvsv','완제품',NULL,NULL,NULL,'',1000,'1','zzz','','',''),('m123','','',NULL,NULL,NULL,'',NULL,'','','','',''),('m1234','테스트','완제품',100,100,NULL,'',NULL,'','','','',''),('qwer','nddfh','완제품',NULL,NULL,NULL,'',NULL,'','','','',''),('safdsdaf','fasafsd','',12,34,56,'fdsdff',100,'aaa','zzz','sdfsdf','sdfsdfsdf','aaa'),('tt1','testtest','완제품',NULL,NULL,NULL,'',NULL,'aaa','zzz','','','');
/*!40000 ALTER TABLE `materialtable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mo`
--

DROP TABLE IF EXISTS `mo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mo` (
  `mo_code` varchar(255) NOT NULL,
  `sop_code` varchar(255) DEFAULT NULL,
  `bom_code` varchar(255) DEFAULT NULL,
  `quantity` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `material_code` varchar(255) DEFAULT NULL,
  `material_name` varchar(255) DEFAULT NULL,
  `order_code` varchar(255) DEFAULT NULL,
  `due_date` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`mo_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mo`
--

LOCK TABLES `mo` WRITE;
/*!40000 ALTER TABLE `mo` DISABLE KEYS */;
INSERT INTO `mo` VALUES ('MO001','SOP001','BOM001','100','In Progress','MAT001','Steel Sheet','ORD001','2025-03-15'),('MO002','SOP002','BOM002','200','Completed','MAT002','Aluminum Alloy','ORD002','2025-03-14'),('MO003','SOP003','BOM003','150','In Progress','MAT003','Copper Wire','ORD003','2025-03-13'),('MO004','SOP004','BOM004','500','Pending','MAT004','PVC Pipe','ORD004','2025-03-12'),('MO005','SOP005','BOM005','300','In Progress','MAT005','Rubber Seal','ORD005','2025-03-11'),('MO006','SOP006','BOM006','400','Completed','MAT006','Iron Rod','ORD006','2025-03-10'),('MO007','SOP007','BOM007','250','Pending','MAT007','Plastic Container','ORD007','2025-03-09'),('MO008','SOP008','BOM008','600','In Progress','MAT008','Carbon Steel','ORD008','2025-03-08'),('MO009','SOP009','BOM009','450','Completed','MAT009','Glass Sheet','ORD009','2025-03-07'),('MO010','SOP010','BOM010','120','In Progress','MAT010','Wooden Plank','ORD010','2025-03-06');
/*!40000 ALTER TABLE `mo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_form`
--

DROP TABLE IF EXISTS `order_form`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_form` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `order_code` varchar(20) NOT NULL,
  `internal_external` varchar(20) NOT NULL,
  `creator_name` varchar(50) NOT NULL,
  `creator_position` varchar(30) DEFAULT NULL,
  `creator_phone` varchar(20) DEFAULT NULL,
  `creator_email` varchar(50) DEFAULT NULL,
  `administrator_name` varchar(50) NOT NULL,
  `administrator_position` varchar(30) DEFAULT NULL,
  `administrator_phone` varchar(20) DEFAULT NULL,
  `administrator_email` varchar(50) DEFAULT NULL,
  `product_name` varchar(100) NOT NULL,
  `unit_price` int DEFAULT NULL,
  `storage` varchar(50) DEFAULT NULL,
  `material_cost` int DEFAULT NULL,
  `personnel_expenses` int DEFAULT NULL,
  `expenses` int DEFAULT NULL,
  `stock` varchar(30) DEFAULT NULL,
  `transaction_quantity` int DEFAULT NULL,
  `total_price` int DEFAULT NULL,
  `order_vat` int DEFAULT NULL,
  `account_code` varchar(50) NOT NULL,
  `account_name` varchar(50) DEFAULT NULL,
  `account_type` varchar(50) DEFAULT NULL,
  `account_address` varchar(200) DEFAULT NULL,
  `account_manager` varchar(50) DEFAULT NULL,
  `manager_phone` varchar(20) DEFAULT NULL,
  `manager_email` varchar(50) DEFAULT NULL,
  `sledding` varchar(50) DEFAULT NULL,
  `delivery_date` datetime DEFAULT NULL,
  `creation_date` datetime DEFAULT NULL,
  `modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_form`
--

LOCK TABLES `order_form` WRITE;
/*!40000 ALTER TABLE `order_form` DISABLE KEYS */;
INSERT INTO `order_form` VALUES (1,'aa','aaa','aa','aa','12313','sd','ddd','dd','123213a','aaaa','',12212,NULL,NULL,NULL,NULL,'',1212,12121,1212,'','','','','','','','','2025-03-17 00:00:00','2025-03-13 00:00:00',NULL),(3,'a111','as','sa','sa','sa','sa','sa','sa','sa','sa','231',321,NULL,NULL,NULL,NULL,'123',123,123,123,'213','213','213','321','213','123','123','32121','2025-03-17 00:00:00','2025-03-17 00:00:00',NULL);
/*!40000 ALTER TABLE `order_form` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pay_stub`
--

DROP TABLE IF EXISTS `pay_stub`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pay_stub` (
  `pay_stub_id` int NOT NULL AUTO_INCREMENT,
  `employee_code` varchar(20) NOT NULL,
  `date_of_paystub` date NOT NULL,
  `total_salary` int NOT NULL,
  `deductible` int NOT NULL,
  `actual_salary` int NOT NULL,
  PRIMARY KEY (`pay_stub_id`),
  KEY `employee_code` (`employee_code`),
  CONSTRAINT `pay_stub_ibfk_1` FOREIGN KEY (`employee_code`) REFERENCES `employee` (`employee_code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pay_stub`
--

LOCK TABLES `pay_stub` WRITE;
/*!40000 ALTER TABLE `pay_stub` DISABLE KEYS */;
/*!40000 ALTER TABLE `pay_stub` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plant`
--

DROP TABLE IF EXISTS `plant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plant` (
  `plant_code` varchar(4) NOT NULL,
  `plant_name` char(50) NOT NULL,
  `location` varchar(45) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `fax` varchar(15) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `created_by` varchar(20) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `changed_by` varchar(20) DEFAULT NULL,
  `changed_on` datetime DEFAULT NULL,
  `del_flag` char(1) DEFAULT NULL,
  PRIMARY KEY (`plant_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plant`
--

LOCK TABLES `plant` WRITE;
/*!40000 ALTER TABLE `plant` DISABLE KEYS */;
INSERT INTO `plant` VALUES ('P001','진하창고','진하네집',NULL,NULL,NULL,NULL,'2025-03-11 00:00:00','USER01','2025-03-17 09:56:22',NULL),('P002','정윤창고_수정','정윤이네',NULL,NULL,NULL,'USER01','2025-03-14 20:13:05','USER01','2025-03-14 20:13:13','X'),('P003','ㅇㅇㅇ',NULL,NULL,NULL,'aaa@naver.com','USER01','2025-03-17 09:16:21',NULL,NULL,NULL),('P004','bb창고',NULL,NULL,NULL,NULL,'USER01','2025-03-17 09:17:26',NULL,NULL,'X'),('P005','cc창고',NULL,NULL,NULL,NULL,'USER01','2025-03-17 09:19:38',NULL,NULL,NULL),('P006','test창고',NULL,NULL,NULL,NULL,'USER01','2025-03-17 09:21:05',NULL,NULL,NULL),('P007','asa','aaaa','112233','3a','dffdds@naver.com','USER01','2025-03-17 09:55:32',NULL,NULL,NULL);
/*!40000 ALTER TABLE `plant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plant_material`
--

DROP TABLE IF EXISTS `plant_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plant_material` (
  `material_code` varchar(50) NOT NULL,
  `material_name` varchar(50) DEFAULT NULL,
  `material_type` varchar(50) DEFAULT NULL,
  `plant_name` varchar(50) DEFAULT NULL,
  `plant_code` varchar(50) DEFAULT NULL,
  `plant_location` varchar(50) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `unit` varchar(50) DEFAULT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`material_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plant_material`
--

LOCK TABLES `plant_material` WRITE;
/*!40000 ALTER TABLE `plant_material` DISABLE KEYS */;
INSERT INTO `plant_material` VALUES ('MAT002','Aluminum Alloy','Raw Material','대전창고','PLT002','대전',200,'kg',12000),('MAT003','Copper Wire','Raw Material','대구창고','PLT003','대구',150,'m',8000);
/*!40000 ALTER TABLE `plant_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchasing_order`
--

DROP TABLE IF EXISTS `purchasing_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchasing_order` (
  `po_num` varchar(6) NOT NULL,
  `vendor` varchar(6) DEFAULT NULL,
  `mat_code` varchar(45) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `measure` varchar(4) DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `measure2` varchar(4) DEFAULT NULL,
  `plant` varchar(4) DEFAULT NULL,
  `manufactoring_code` varchar(10) DEFAULT NULL,
  `manager` varchar(20) DEFAULT NULL,
  `department` varchar(50) DEFAULT NULL,
  `created_by` varchar(20) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  `changed_by` varchar(20) DEFAULT NULL,
  `changed_on` datetime DEFAULT NULL,
  `del_flag` char(1) DEFAULT NULL,
  `stat` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`po_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchasing_order`
--

LOCK TABLES `purchasing_order` WRITE;
/*!40000 ALTER TABLE `purchasing_order` DISABLE KEYS */;
INSERT INTO `purchasing_order` VALUES ('po0001','1','796969',5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2025-03-11 00:00:00',NULL,NULL,NULL,'H');
/*!40000 ALTER TABLE `purchasing_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receiving`
--

DROP TABLE IF EXISTS `receiving`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receiving` (
  `receiving_code` varchar(10) NOT NULL,
  `order_code` varchar(20) DEFAULT NULL,
  `receiving_classification` varchar(20) DEFAULT NULL,
  `client_code` varchar(10) DEFAULT NULL,
  `client_name` varchar(50) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `unit` varchar(10) DEFAULT NULL,
  `material_code` varchar(50) DEFAULT NULL,
  `material_name` varchar(50) DEFAULT NULL,
  `receiving_responsibility` varchar(20) DEFAULT NULL,
  `purchase_order_code` varchar(10) DEFAULT NULL,
  `plant_code` varchar(20) DEFAULT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`receiving_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receiving`
--

LOCK TABLES `receiving` WRITE;
/*!40000 ALTER TABLE `receiving` DISABLE KEYS */;
INSERT INTO `receiving` VALUES ('REC001','ORD001','Raw Material','C001','John Doe',100,'kg','MAT001','Steel Sheet','Manager1','PO001','P001',10000),('REC002','ORD002','Raw Material','C002','Jane Smith',200,'kg','MAT002','Aluminum Alloy','Manager2','PO002','P002',12000),('REC003','ORD003','Raw Material','C003','Tom Lee',150,'m','MAT003','Copper Wire','Manager3','PO003','P003',8000),('REC004','ORD004','Finished Goods','C004','Alice Johnson',500,'m','MAT004','PVC Pipe','Manager4','PO004','P004',5000),('REC005','ORD005','Raw Material','C005','Bob Brown',300,'piece','MAT005','Rubber Seal','Manager5','PO005','P005',15000),('REC006','ORD006','Raw Material','C006','Charlie White',400,'kg','MAT006','Iron Rod','Manager6','PO006','PLT006',7000),('REC007','ORD007','Finished Goods','C007','David Green',250,'piece','MAT007','Plastic Container','Manager7','PO007','PLT007',6000),('REC008','ORD008','Raw Material','C008','Eva Black',600,'kg','MAT008','Carbon Steel','Manager8','PO008','PLT008',11000),('REC009','ORD009','Raw Material','C009','Frank Blue',450,'kg','MAT009','Glass Sheet','Manager9','PO009','PLT009',13000),('REC010','ORD010','Finished Goods','C010','Grace Red',120,'piece','MAT010','Wooden Plank','Manager10','PO010','PLT010',4000),('REC012','ORD002','0','0','0',200,'0','MAT002','Aluminum Alloy','0','0','0',0),('REC013','ORD005','0','0','0',300,'0','MAT005','Rubber Seal','0','0','0',0),('REC014','ORD002','0','0','04545',200,'0','MAT002','Aluminum Alloy','0','0','0',0);
/*!40000 ALTER TABLE `receiving` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary_details`
--

DROP TABLE IF EXISTS `salary_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary_details` (
  `pay_stub_id` int NOT NULL AUTO_INCREMENT,
  `employee_code` varchar(20) NOT NULL,
  `pay_out_date` date DEFAULT NULL,
  `basic_salary` int DEFAULT '0',
  `allowance` int DEFAULT '0',
  `bonus` int DEFAULT '0',
  `additional_allowance` int DEFAULT '0',
  `annual_leave_allowance` int DEFAULT '0',
  `total_salary` int DEFAULT '0',
  `income_tax` int DEFAULT '0',
  `final_payment` int DEFAULT '0',
  PRIMARY KEY (`pay_stub_id`),
  KEY `fk_salarydetails_employee` (`employee_code`),
  CONSTRAINT `fk_salarydetails_employee` FOREIGN KEY (`employee_code`) REFERENCES `employee` (`employee_code`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary_details`
--

LOCK TABLES `salary_details` WRITE;
/*!40000 ALTER TABLE `salary_details` DISABLE KEYS */;
INSERT INTO `salary_details` VALUES (27,'e001','2025-03-17',5000000,1000,1000,0,0,5002000,165066,4836934),(28,'e002','2025-03-17',500,1000000,50000,0,0,1050500,34666,1015834);
/*!40000 ALTER TABLE `salary_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales_performance`
--

DROP TABLE IF EXISTS `sales_performance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_performance` (
  `performance_id` int NOT NULL AUTO_INCREMENT,
  `order_code` varchar(20) NOT NULL,
  `internal_external` varchar(20) NOT NULL,
  `creator_name` varchar(50) NOT NULL,
  `creator_position` varchar(30) DEFAULT NULL,
  `creator_phone` varchar(20) DEFAULT NULL,
  `creator_email` varchar(50) DEFAULT NULL,
  `administrator_name` varchar(50) NOT NULL,
  `administrator_position` varchar(30) DEFAULT NULL,
  `administrator_phone` varchar(20) DEFAULT NULL,
  `administrator_email` varchar(50) DEFAULT NULL,
  `product_name` varchar(50) NOT NULL,
  `product_code` varchar(50) DEFAULT NULL,
  `unit_price` int DEFAULT NULL,
  `storage` varchar(50) DEFAULT NULL,
  `material_cost` int DEFAULT NULL,
  `personnel_expenses` int DEFAULT NULL,
  `expenses` int DEFAULT NULL,
  `stock` varchar(30) DEFAULT NULL,
  `transaction_quantity` int DEFAULT NULL,
  `total_price` int DEFAULT NULL,
  `order_vat` int DEFAULT NULL,
  `NetProfit` int DEFAULT NULL,
  `total_budget` int DEFAULT NULL,
  `account_code` varchar(50) NOT NULL,
  `business_number` varchar(50) DEFAULT NULL,
  `account_name` varchar(50) DEFAULT NULL,
  `account_type` varchar(50) DEFAULT NULL,
  `account_address` varchar(200) DEFAULT NULL,
  `Country` varchar(50) DEFAULT NULL,
  `account_manager` varchar(50) DEFAULT NULL,
  `manager_phone` varchar(20) DEFAULT NULL,
  `manager_email` varchar(50) DEFAULT NULL,
  `sledding` varchar(50) DEFAULT NULL,
  `delivery_date` datetime DEFAULT NULL,
  `creation_date` datetime DEFAULT NULL,
  `modified_date` datetime DEFAULT NULL,
  PRIMARY KEY (`performance_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_performance`
--

LOCK TABLES `sales_performance` WRITE;
/*!40000 ALTER TABLE `sales_performance` DISABLE KEYS */;
/*!40000 ALTER TABLE `sales_performance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `severance_pay`
--

DROP TABLE IF EXISTS `severance_pay`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `severance_pay` (
  `severance_pay_id` int NOT NULL AUTO_INCREMENT,
  `employee_code` varchar(20) NOT NULL,
  `calculation_period` varchar(50) NOT NULL,
  `total_days` int NOT NULL,
  `basic_salary` int NOT NULL,
  `additional_allowance` int DEFAULT NULL,
  `total_salary` int NOT NULL,
  `annual_bonus_total` int DEFAULT NULL,
  `average_daily_wage` int DEFAULT NULL,
  `annual_leave_allowance` int DEFAULT NULL,
  `severance_income` int DEFAULT NULL,
  `income_tax` int DEFAULT NULL,
  `local_income_tax` int DEFAULT NULL,
  `final_payment` int DEFAULT NULL,
  PRIMARY KEY (`severance_pay_id`),
  KEY `employee_code` (`employee_code`),
  CONSTRAINT `severance_pay_ibfk_1` FOREIGN KEY (`employee_code`) REFERENCES `employee` (`employee_code`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `severance_pay`
--

LOCK TABLES `severance_pay` WRITE;
/*!40000 ALTER TABLE `severance_pay` DISABLE KEYS */;
/*!40000 ALTER TABLE `severance_pay` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shipping`
--

DROP TABLE IF EXISTS `shipping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shipping` (
  `shipping_code` varchar(10) NOT NULL,
  `order_code` varchar(20) DEFAULT NULL,
  `material_classification` varchar(20) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `unit` varchar(10) DEFAULT NULL,
  `selling_price` int DEFAULT NULL,
  `vat_price` int DEFAULT NULL,
  `total_price` int DEFAULT NULL,
  `material_code` varchar(50) DEFAULT NULL,
  `material_name` varchar(50) DEFAULT NULL,
  `sales_order_number` varchar(20) DEFAULT NULL,
  `purchase_order_code` varchar(10) DEFAULT NULL,
  `client_code` char(10) DEFAULT NULL,
  `client_name` char(50) DEFAULT NULL,
  PRIMARY KEY (`shipping_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shipping`
--

LOCK TABLES `shipping` WRITE;
/*!40000 ALTER TABLE `shipping` DISABLE KEYS */;
INSERT INTO `shipping` VALUES ('SHP001','ORD001','Raw Material',100,'kg',15000,1500,16500,'MAT001','Steel Sheet','SO001','PO001','C001','John Doe'),('SHP002','ORD002','Raw Material',200,'kg',18000,1800,19800,'MAT002','Aluminum Alloy','SO002','PO002','C002','Jane Smith'),('SHP003','ORD003','Raw Material',150,'m',12000,1200,13200,'MAT003','Copper Wire','SO003','PO003','C003','Tom Lee'),('SHP004','ORD004','Finished Goods',500,'m',8000,800,8800,'MAT004','PVC Pipe','SO004','PO004','C004','Alice Johnson'),('SHP005','ORD005','Raw Material',300,'piece',22000,2200,24200,'MAT005','Rubber Seal','SO005','PO005','C005','Bob Brown'),('SHP006','ORD006','Raw Material',400,'kg',10000,1000,11000,'MAT006','Iron Rod','SO006','PO006','C006','Charlie White'),('SHP007','ORD007','Finished Goods',250,'piece',9000,900,9900,'MAT007','Plastic Container','SO007','PO007','C007','David Green'),('SHP008','ORD008','Raw Material',600,'kg',16000,1600,17600,'MAT008','Carbon Steel','SO008','PO008','C008','Eva Black'),('SHP009','ORD009','Raw Material',450,'kg',20000,2000,22000,'MAT009','Glass Sheet','SO009','PO009','C009','Frank Blue'),('SHP010','ORD010','Finished Goods',120,'piece',NULL,456,6600,'MAT010','Wooden Plank','SO010','PO010','C010','Grace Red'),('SHP012','ORD002','0',200,'0',123,NULL,5466,'MAT002','Aluminum Alloy','0','0','0','0'),('SHP013','ORD005','0',300,'0',1111,0,0,'MAT005','Rubber Seal','0','0','0','0'),('SHP015','ORD006','0',400,'4646',4545,0,0,'MAT006','Iron Rod','0','0','0','0'),('SHP016','ORD004','0',500,'0',0,0,0,'MAT004','PVC Pipe','0','0','0','0'),('SHP018','ORD006','0',400,'0',0,0,0,'MAT006','Iron Rod','0','0','0','0'),('SHP020','ORD008','0',600,'0',0,0,0,'MAT008','Carbon Steel','0','0','0','0'),('SHP021','ORD001','0',100,'0',0,0,0,'MAT001','Steel Sheet','0','0','0','0');
/*!40000 ALTER TABLE `shipping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sop`
--

DROP TABLE IF EXISTS `sop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sop` (
  `SOP_Code` varchar(255) NOT NULL,
  `BOM_Code` varchar(255) DEFAULT NULL,
  `order_code` varchar(255) DEFAULT NULL,
  `material_code` varchar(255) DEFAULT NULL,
  `material_name` varchar(255) DEFAULT NULL,
  `writter` varchar(255) DEFAULT NULL,
  `written_date` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`SOP_Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sop`
--

LOCK TABLES `sop` WRITE;
/*!40000 ALTER TABLE `sop` DISABLE KEYS */;
INSERT INTO `sop` VALUES ('123','234','345','456','완제품이름','성진하','2025-03-11'),('12345','111','111','','','',''),('test','tset','','','','',''),('test1','test1','test1','','','','');
/*!40000 ALTER TABLE `sop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sop_f`
--

DROP TABLE IF EXISTS `sop_f`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sop_f` (
  `sop_code` varchar(255) DEFAULT NULL,
  `work_name` varchar(255) DEFAULT NULL,
  `working` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sop_f`
--

LOCK TABLES `sop_f` WRITE;
/*!40000 ALTER TABLE `sop_f` DISABLE KEYS */;
INSERT INTO `sop_f` VALUES ('test1','w','',''),('test','test','','');
/*!40000 ALTER TABLE `sop_f` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taxinvoice`
--

DROP TABLE IF EXISTS `taxinvoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taxinvoice` (
  `ti_id` varchar(15) NOT NULL,
  `ti_create_date` date NOT NULL,
  `ti_type` varchar(2) NOT NULL,
  `business_client` varchar(45) DEFAULT NULL,
  `business_number` varchar(14) NOT NULL,
  `business_code` varchar(5) DEFAULT NULL,
  `ti_description` varchar(100) DEFAULT NULL,
  `ti_ori_amount` bigint NOT NULL,
  `ti_tax_rate` char(3) DEFAULT '10%',
  `ti_vat` bigint NOT NULL,
  `ti_amount` bigint NOT NULL,
  `ti_publish_state` varchar(4) DEFAULT 'None',
  PRIMARY KEY (`ti_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taxinvoice`
--

LOCK TABLES `taxinvoice` WRITE;
/*!40000 ALTER TABLE `taxinvoice` DISABLE KEYS */;
INSERT INTO `taxinvoice` VALUES ('20250317120001','2025-03-17','매입','','123-12-12345',NULL,'원재료매입',1000000,'10%',100000,1100000,''),('20250320110001','2025-03-20','매출','','456-45-45678',NULL,'상품 매출',2000000,'10%',200000,2200000,'');
/*!40000 ALTER TABLE `taxinvoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test` (
  `work_name` varchar(255) DEFAULT NULL,
  `working` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `sop_code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test1`
--

DROP TABLE IF EXISTS `test1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test1` (
  `work_name` varchar(255) DEFAULT NULL,
  `working` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `sop_code` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test1`
--

LOCK TABLES `test1` WRITE;
/*!40000 ALTER TABLE `test1` DISABLE KEYS */;
/*!40000 ALTER TABLE `test1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction_history_inquiry`
--

DROP TABLE IF EXISTS `transaction_history_inquiry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction_history_inquiry` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Transaction_date` char(100) DEFAULT NULL,
  `Customer_name` char(100) DEFAULT NULL,
  `business_number` int DEFAULT NULL,
  `Customer_code` char(100) DEFAULT NULL,
  `Type_business` char(100) DEFAULT NULL,
  `Country` char(100) DEFAULT NULL,
  `item` char(100) DEFAULT NULL,
  `quantity` char(50) DEFAULT NULL,
  `unit_price` char(100) DEFAULT NULL,
  `total_price` char(100) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction_history_inquiry`
--

LOCK TABLES `transaction_history_inquiry` WRITE;
/*!40000 ALTER TABLE `transaction_history_inquiry` DISABLE KEYS */;
/*!40000 ALTER TABLE `transaction_history_inquiry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'erp_db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-17 20:43:58
