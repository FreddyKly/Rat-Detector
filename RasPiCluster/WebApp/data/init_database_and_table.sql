CREATE DATABASE IF NOT EXISTS RatDetections;
USE RatDetections;
CREATE TABLE IF NOT EXISTS `detections` (
    `id_pic` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    `img` LONGBLOB NOT NULL,
    `createdAt` DATETIME NOT NULL,
    `numberOfRats` INT UNSIGNED,
    `confidence` INT UNSIGNED,
  PRIMARY KEY (`id_pic`)
);
