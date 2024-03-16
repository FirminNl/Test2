DROP TABLE IF EXISTS `similarity`;
CREATE TABLE `similarity` (
`id` int NOT NULL DEFAULT '0',
`timestamp` timestamp,
`matching_id` int NOT NULL DEFAULT '0',
`score` int NOT NULL DEFAULT '0',
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
