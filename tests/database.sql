
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