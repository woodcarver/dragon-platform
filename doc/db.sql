# ************************************************************
# Sequel Pro SQL dump
# Version 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 127.0.0.1 (MySQL 5.6.19)
# Database: dragon
# Generation Time: 2018-10-23 14:49:49 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table simulation
# ------------------------------------------------------------

DROP TABLE IF EXISTS `simulation`;

CREATE TABLE `simulation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT 'simulation名称',
  `profile` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '星团密度分布',
  `rh` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '星团半质量半径',
  `imf` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '初始质量函数',
  `q` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '双星质量比分布',
  `kick_ns` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '中子星 kicked velocity',
  `rt` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '星团潮汐半径',
  `simulation_time` bigint(20) DEFAULT NULL COMMENT '模拟产出时间',
  `publish_date` timestamp NULL DEFAULT NULL COMMENT '发布时间',
  `video_path` varchar(255) DEFAULT NULL COMMENT '视频地址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `simulation` WRITE;
/*!40000 ALTER TABLE `simulation` DISABLE KEYS */;

INSERT INTO `simulation` (`id`, `title`, `profile`, `rh`, `imf`, `q`, `kick_ns`, `rt`, `simulation_time`, `publish_date`, `video_path`)
VALUES
	(1,'xxx','profile','rh','imf','q','kick','rt',1,'2018-09-01 10:00:00',NULL),
	(2,'ssss','sss','ss','ss','s','s','s',1222222,'2018-09-09 10:00:00',NULL);

/*!40000 ALTER TABLE `simulation` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table simulation_down_log
# ------------------------------------------------------------

DROP TABLE IF EXISTS `simulation_down_log`;

CREATE TABLE `simulation_down_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `simulation_id` int(11) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL COMMENT '留下的email',
  `create_date` timestamp NULL DEFAULT NULL COMMENT '发布时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `simulation_down_log` WRITE;
/*!40000 ALTER TABLE `simulation_down_log` DISABLE KEYS */;

INSERT INTO `simulation_down_log` (`id`, `simulation_id`, `email`, `create_date`)
VALUES
	(1,1,'xiedandan@xdd.com','2018-09-12 15:17:33'),
	(2,0,'string','2018-09-16 16:24:36'),
	(3,0,'string','2018-09-16 16:27:11');

/*!40000 ALTER TABLE `simulation_down_log` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table simulation_files
# ------------------------------------------------------------

DROP TABLE IF EXISTS `simulation_files`;

CREATE TABLE `simulation_files` (
  `file_name` varchar(255) NOT NULL DEFAULT '' COMMENT '文件名',
  `simulation_id` int(11) NOT NULL DEFAULT '0',
  `time_range` int(11) DEFAULT NULL,
  `stellar_type` varchar(255) DEFAULT NULL,
  `populations` varchar(255) DEFAULT NULL,
  `create_date` timestamp NULL DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`simulation_id`,`file_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table simulation_preview
# ------------------------------------------------------------

DROP TABLE IF EXISTS `simulation_preview`;

CREATE TABLE `simulation_preview` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_name` varchar(255) DEFAULT NULL,
  `nbody_time` varchar(255) DEFAULT NULL COMMENT 'nbody_time',
  `kw` int(11) DEFAULT NULL COMMENT 'kw',
  `mass` varchar(255) DEFAULT NULL COMMENT '质量',
  `luminosity` varchar(255) DEFAULT NULL,
  `temperature` varchar(255) DEFAULT NULL,
  `metallicity` varchar(255) DEFAULT NULL,
  `create_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `simulation_preview` WRITE;
/*!40000 ALTER TABLE `simulation_preview` DISABLE KEYS */;

INSERT INTO `simulation_preview` (`id`, `file_name`, `nbody_time`, `kw`, `mass`, `luminosity`, `temperature`, `metallicity`, `create_time`)
VALUES
	(1,'x','x',1,'1','1','1','1','2018-09-16 00:00:00');

/*!40000 ALTER TABLE `simulation_preview` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

