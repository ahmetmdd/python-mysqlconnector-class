# Create Testuser
CREATE USER 'coldrimp'@'localhost' IDENTIFIED BY 'coldrimp';
GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP ON *.* TO 'dev'@'localhost';
# Create DB
CREATE DATABASE IF NOT EXISTS `tabloadi` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `tabloadi`;
# Create Table

CREATE TABLE `tabloadi` (
  `Id` bigint(22) NOT NULL,
  `names` varchar(255) NOT NULL,
  `fak` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `tabloadi`
  ADD PRIMARY KEY (`Id`);
ALTER TABLE `tabloadi`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;
# Add Data