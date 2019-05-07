/*
SQLyog Ultimate v12.4.3 (64 bit)
MySQL - 10.1.36-MariaDB : Database - db_toko2
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_toko2` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `db_toko2`;

/*Table structure for table `tb_integrasi` */

DROP TABLE IF EXISTS `tb_integrasi`;

CREATE TABLE `tb_integrasi` (
  `id_invoice` int(11) DEFAULT NULL,
  `total_transaksi` int(11) DEFAULT NULL,
  `status` enum('1','2') NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tb_integrasi` */

insert  into `tb_integrasi`(`id_invoice`,`total_transaksi`,`status`) values 
(41,100,'2'),
(43,67,'1');

/*Table structure for table `tb_invoice` */

DROP TABLE IF EXISTS `tb_invoice`;

CREATE TABLE `tb_invoice` (
  `id_invoice` int(11) NOT NULL AUTO_INCREMENT,
  `total_transaksi` int(11) DEFAULT NULL,
  `status` enum('1','2') NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_invoice`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;

/*Data for the table `tb_invoice` */

insert  into `tb_invoice`(`id_invoice`,`total_transaksi`,`status`) values 
(41,100,'2'),
(43,67,'1');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
