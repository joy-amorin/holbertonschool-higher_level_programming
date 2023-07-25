-- cript that creates a table called first_table in the current database in your MySQL server
CREATE TABLE if NOT EXISTS `first_table` (
    `ID` INT NOT NULL AUTO_INCREMENT,
    `NAME` VARCHAR(256),
    PRIMARY KEY (`ID`)
)