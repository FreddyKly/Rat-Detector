CREATE TABLE `detections` (
    `idpic` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    `caption` VARCHAR(45),
    `img` LONGBLOB NOT NULL,
    `createdAt` DATETIME NOT NULL,
    `numberOfRats` INT UNSIGNED,
    `confidence` INT UNSIGNED,
  PRIMARY KEY (`idpic`)
)
