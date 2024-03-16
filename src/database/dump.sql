CREATE SCHEMA IF NOT EXISTS `datingapp` DEFAULT CHARACTER SET utf8 ;
USE `datingapp`;

DROP TABLE IF EXISTS `userprofile`;
CREATE TABLE `userprofile` (
`id` int NOT NULL DEFAULT '0',
`timestamp` timestamp,
`google_user_id` varchar(100) NOT NULL DEFAULT '',
`email` varchar(100) NOT NULL DEFAULT '',
`firstname`varchar(100) NOT NULL DEFAULT'',
`surname`varchar(100) NOT NULL DEFAULT'',
`about_me` varchar(500) NOT NULL DEFAULT '',
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

DROP TABLE IF EXISTS `searchprofile`;
CREATE TABLE `searchprofile` (
`id` int NOT NULL DEFAULT '0',
`timestamp` timestamp,
`userprofile_id` int NOT NULL DEFAULT '0',
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

DROP TABLE IF EXISTS `matching`;
CREATE TABLE `matching` (
`id` int NOT NULL DEFAULT '0',
`timestamp` timestamp,
`userprofile_id` int NOT NULL DEFAULT '0',
`candidateprofile_id` int NOT NULL DEFAULT '0',
`unseen_profile` boolean,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

DROP TABLE IF EXISTS `similarity`;
CREATE TABLE `similarity` (
`id` int NOT NULL DEFAULT '0',
`timestamp` timestamp,
`matching_id` int NOT NULL DEFAULT '0',
`score` int NOT NULL DEFAULT '0',
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
