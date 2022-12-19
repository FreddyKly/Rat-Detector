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
INSERT INTO RatDetections.detections (img, createdAt, numberOfRats, confidence)
VALUES (
    "This is a test entry, to prevent having errors due to an empty database!",
    "2001-07-29 21:28:00",
    1,
    90
  );
