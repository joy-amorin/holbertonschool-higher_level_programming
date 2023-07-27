-- at creates a table second_table in the database hbtn_0c_0 
-- in your MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS `second_table`(
    `ID` INT AUTO_INCREMENT,
    `NAME` VARCHAR(256),
    `SCORE` INT,
    PRIMARY KEY (`ID`)
);

INSERT INTO second_table (name, score) VALUES ("John", 10);
INSERT INTO second_table (name, score) VALUES ("Alex", 3);
INSERT INTO second_table (name, score) VALUES ("Bob", 14);
INSERT INTO second_table (name, score) VALUES ("George", 8);