CREATE TABLE IF NOT EXISTS `second_table`(
    `ID` INT AUTO_INCREMENT,
    `NAME` VARCHAR(256),
    `SCORE` INT,
    PRIMARY KEY (`ID`)
);

INSERT INTO second_table (id, name, score) VALUES (1, "Jhon", 10);
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
INSERT INTO second_table (id, name, score) VALUES (4, "George", 8);