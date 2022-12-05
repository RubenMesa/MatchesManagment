-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: cafeteria
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `boletas`
--

DROP TABLE IF EXISTS `boletas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `boletas` (
  `bol_cod` int(11) NOT NULL AUTO_INCREMENT,
  `bol_iva` decimal(9,2) NOT NULL,
  `bol_total` int(11) NOT NULL,
  `ven_cod` int(11) NOT NULL,
  PRIMARY KEY (`bol_cod`),
  KEY `fk_Boletas_Ventas1_idx` (`ven_cod`),
  CONSTRAINT `fk_Boletas_Ventas1` FOREIGN KEY (`ven_cod`) REFERENCES `ventas` (`ven_cod`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `boletas`
--

LOCK TABLES `boletas` WRITE;
/*!40000 ALTER TABLE `boletas` DISABLE KEYS */;
INSERT INTO `boletas` VALUES (1,956.00,5926,1),(2,758.00,4748,2);
/*!40000 ALTER TABLE `boletas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `cli_cod` int(11) NOT NULL AUTO_INCREMENT,
  `cli_puntos` int(11) DEFAULT NULL,
  `cli_descto` decimal(9,2) DEFAULT NULL,
  `cli_frecuente` tinyint(4) DEFAULT NULL,
  `per_run` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`cli_cod`),
  KEY `fk_clientes_personas1_idx` (`per_run`),
  CONSTRAINT `fk_clientes_personas1` FOREIGN KEY (`per_run`) REFERENCES `personas` (`per_run`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,0,0.10,1,444444444),(2,0,0.00,0,555555555),(4,0,0.00,0,666666666);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comandas`
--

DROP TABLE IF EXISTS `comandas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comandas` (
  `com_cod` int(11) NOT NULL AUTO_INCREMENT,
  `com_cant` int(11) NOT NULL,
  `com_hora` datetime NOT NULL,
  `pro_cod` int(11) NOT NULL,
  `ven_cod` int(11) NOT NULL,
  PRIMARY KEY (`com_cod`,`pro_cod`,`ven_cod`),
  KEY `fk_Comandas_Productos1_idx` (`pro_cod`),
  KEY `fk_Comandas_Ventas1_idx` (`ven_cod`),
  CONSTRAINT `fk_Comandas_Productos1` FOREIGN KEY (`pro_cod`) REFERENCES `productos` (`pro_cod`),
  CONSTRAINT `fk_Comandas_Ventas1` FOREIGN KEY (`ven_cod`) REFERENCES `ventas` (`ven_cod`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comandas`
--

LOCK TABLES `comandas` WRITE;
/*!40000 ALTER TABLE `comandas` DISABLE KEYS */;
INSERT INTO `comandas` VALUES (1,1,'2022-11-23 09:00:00',2,1);
/*!40000 ALTER TABLE `comandas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perfiles`
--

DROP TABLE IF EXISTS `perfiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `perfiles` (
  `perf_cod` int(11) NOT NULL AUTO_INCREMENT,
  `perf_nom` varchar(45) NOT NULL,
  `perf_desc` varchar(45) NOT NULL,
  PRIMARY KEY (`perf_cod`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perfiles`
--

LOCK TABLES `perfiles` WRITE;
/*!40000 ALTER TABLE `perfiles` DISABLE KEYS */;
INSERT INTO `perfiles` VALUES (1,'Cajero','Encargado del manejo de la caja'),(2,'Administrador','Encargado de la cafetería'),(3,'Garzón','Mesero');
/*!40000 ALTER TABLE `perfiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas`
--

DROP TABLE IF EXISTS `personas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personas` (
  `per_run` int(10) unsigned NOT NULL,
  `per_nombre` varchar(30) NOT NULL,
  `per_app` varchar(30) NOT NULL,
  `per_apm` varchar(30) DEFAULT NULL,
  `per_tel` varchar(15) DEFAULT NULL,
  `per_email` varchar(45) DEFAULT NULL,
  `per_fnac` date DEFAULT NULL,
  PRIMARY KEY (`per_run`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas`
--

LOCK TABLES `personas` WRITE;
/*!40000 ALTER TABLE `personas` DISABLE KEYS */;
INSERT INTO `personas` VALUES (111111111,'Paola','Nuñez','Galindo','43243459','paola.nuñez@gmail.com','1960-11-30'),(222222222,'Juan','Perez','Gonzalez','123456789','juan.perez@gmail.com','1955-01-23'),(333333333,'Patricio','Muñoz','López','987654321','patricio.muñoz@gmail.com','1990-04-14'),(444444444,'Natalia','Fuenzalida','Mondaca','934123678','natalia.fuenzalida@gmail.com','2000-08-07'),(555555555,'Daniel','Rocco','Cataldo','876612456','daniel.rocco@gmail.com','1980-12-20'),(666666666,'Rodrigo','Aguirre','Pizarro','876322456','rodrigo.aguirre@gmail.com','1995-05-12');
/*!40000 ALTER TABLE `personas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `pro_cod` int(11) NOT NULL AUTO_INCREMENT,
  `pro_nombre` varchar(45) NOT NULL,
  `pro_descripcion` varchar(45) NOT NULL,
  `pro_stock` int(11) NOT NULL,
  `pro_precio` int(11) NOT NULL,
  PRIMARY KEY (`pro_cod`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Donuts','Rellenas de Chocolate',10,2000),(2,'Trozo Tora','Selva Negra',8,2990),(3,'Trozo Torta','Tres Leches',8,2990),(4,'Expreso','Café Solo',10,1490),(5,'Americano','Café No Concentrado',10,1990),(6,'Macchiato','Café Espumoso',10,1990),(7,'Café Con Leche','Mitad café, Mitad Leche',10,1990),(8,'Cappuchino','Poca Leche y Mucha Espuma',10,1990),(9,'Café Latte','Poca Leche y Mucha Espuma',10,1990);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trabajadores`
--

DROP TABLE IF EXISTS `trabajadores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trabajadores` (
  `tra_cod` int(11) NOT NULL AUTO_INCREMENT,
  `tra_inicio_turno` datetime NOT NULL,
  `tra_termino_turno` datetime NOT NULL,
  `tra_fcontr` varchar(45) NOT NULL,
  `tra_contrato` varchar(1000) DEFAULT NULL,
  `perf_cod` int(11) NOT NULL,
  `per_run` int(10) unsigned NOT NULL,
  PRIMARY KEY (`tra_cod`,`perf_cod`,`per_run`),
  KEY `fk_Trabajadores_Perfiles1_idx` (`perf_cod`),
  KEY `fk_Trabajadores_Personas1_idx` (`per_run`),
  CONSTRAINT `fk_Trabajadores_Perfiles1` FOREIGN KEY (`perf_cod`) REFERENCES `perfiles` (`perf_cod`),
  CONSTRAINT `fk_Trabajadores_Personas1` FOREIGN KEY (`per_run`) REFERENCES `personas` (`per_run`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trabajadores`
--

LOCK TABLES `trabajadores` WRITE;
/*!40000 ALTER TABLE `trabajadores` DISABLE KEYS */;
INSERT INTO `trabajadores` VALUES (1,'2022-10-03 08:00:00','2022-10-08 18:00:00','1983',NULL,1,111111111),(2,'2022-10-03 08:00:00','2022-10-08 18:00:00','2011',NULL,2,222222222),(3,'2022-10-03 08:00:00','2022-10-08 18:00:00','1983',NULL,3,333333333);
/*!40000 ALTER TABLE `trabajadores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `usu_cod` int(11) NOT NULL AUTO_INCREMENT,
  `usu_nom` varchar(45) NOT NULL,
  `usu_pass` varchar(45) NOT NULL,
  `tra_cod` int(11) DEFAULT NULL,
  `cli_cod` int(11) DEFAULT NULL,
  PRIMARY KEY (`usu_cod`),
  KEY `fk_Usuarios_Trabajadores1_idx` (`tra_cod`),
  KEY `fk_Usuarios_Clientes1_idx` (`cli_cod`),
  CONSTRAINT `fk_Usuarios_Clientes1` FOREIGN KEY (`cli_cod`) REFERENCES `clientes` (`cli_cod`),
  CONSTRAINT `fk_Usuarios_Trabajadores1` FOREIGN KEY (`tra_cod`) REFERENCES `trabajadores` (`tra_cod`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'paola.nunez','123456',1,NULL),(2,'juan.perez','123456',2,NULL),(3,'patricio.muñoz','123456',3,NULL),(4,'naty.fuenzalida','123456',NULL,1),(5,'dani.rocco','123456',NULL,2);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas`
--

DROP TABLE IF EXISTS `ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas` (
  `ven_cod` int(11) NOT NULL AUTO_INCREMENT,
  `ven_descrip` varchar(45) NOT NULL,
  `ven_fecha` varchar(45) NOT NULL,
  `ven_subtotal` varchar(45) NOT NULL,
  `cli_cod` int(11) DEFAULT NULL,
  `usu_cod` int(11) DEFAULT NULL,
  PRIMARY KEY (`ven_cod`),
  KEY `fk_Ventas_Clientes1_idx` (`cli_cod`),
  KEY `fk_Ventas_Usuarios1_idx` (`usu_cod`),
  CONSTRAINT `fk_Ventas_Clientes1` FOREIGN KEY (`cli_cod`) REFERENCES `clientes` (`cli_cod`),
  CONSTRAINT `fk_Ventas_Usuarios1` FOREIGN KEY (`usu_cod`) REFERENCES `usuarios` (`usu_cod`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
INSERT INTO `ventas` VALUES (1,'Cappuchino + Trozo Torta','2022-11-23','4980',4,NULL),(2,'Latte + Donuts','2022-11-27','3990',NULL,5);
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-27 23:59:53
