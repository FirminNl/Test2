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

DROP TABLE IF EXISTS `chat`;
CREATE TABLE `chat` (
  `id` int NOT NULL DEFAULT '0',
  `timestamp` timestamp,
  `sender_id` int NOT NULL DEFAULT '0',
  `receiver_id` int NOT NULL DEFAULT '0',
  `accepted` boolean,
  `is_open` boolean,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `id` int NOT NULL DEFAULT '0',
  `timestamp` timestamp,
  `chat_id` int NOT NULL DEFAULT '0',
  `content` VARCHAR(200) NULL,
  `sender_id` INT NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

DROP TABLE IF EXISTS `blockedprofile`;
CREATE TABLE `blockedprofile` (
  `id` int NOT NULL DEFAULT '0',
  `timestamp` timestamp,
  `userprofile_id` int NOT NULL DEFAULT '0',
  `blockeduser_id` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

DROP TABLE IF EXISTS `characteristic`;
CREATE TABLE `characteristic` (
  `id` int NOT NULL DEFAULT '0',
  `timestamp` timestamp,
  `name` VARCHAR(145) NULL,
  `description` VARCHAR(145) NULL,
  `is_selection` boolean,
  `author_id` int NOT NULL DEFAULT '0',
  `is_standart` boolean,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

DROP TABLE IF EXISTS `info`;
CREATE TABLE `info` (
  `id` int NOT NULL DEFAULT '0',
  `timestamp` timestamp,
  `userprofile_id` int NOT NULL DEFAULT '0',
  `answer_id` int NOT NULL DEFAULT '0',
  `is_selection` boolean,
  `is_searchprofile` boolean,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

DROP TABLE IF EXISTS `description`;
CREATE TABLE `description` (
  `id` int NOT NULL DEFAULT '0',
  `timestamp` timestamp,
  `characteristic_id` int NOT NULL DEFAULT '0',
  `answer` VARCHAR(200) NULL,
  `max_answer` VARCHAR(200) NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

DROP TABLE IF EXISTS `selection`;
CREATE TABLE `selection` (
  `id` int NOT NULL DEFAULT '0',
  `timestamp` timestamp,
  `characteristic_id` int NOT NULL DEFAULT '0',
  `answer` VARCHAR(200) NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

DROP TABLE IF EXISTS `memoboard`;
CREATE TABLE `memoboard` (
  `id` int NOT NULL DEFAULT '0',
  `timestamp` timestamp,
  `userprofile_id` int NOT NULL DEFAULT '0',
  `matching_id` int NOT NULL DEFAULT '0',
  `saved_id` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

INSERT INTO `datingapp`.`characteristic`
(`id`,
`timestamp`,
`name`,
`description`,
`is_selection`,
`author_id`,
`is_standart`)
VALUES
(1,
"2023-06-26 17:18:42",
"Geschlecht",
"Diese Eigenschaft soll dein Geschlecht identifzieren",
true,
0,
true);

INSERT INTO `datingapp`.`characteristic`
(`id`,
`timestamp`,
`name`,
`description`,
`is_selection`,
`author_id`,
`is_standart`)
VALUES
(2,
"2023-06-26 17:18:42",
"Absicht",
"Diese Eigenschaft soll identifizieren was deine Absicht ist",
true,
0,
true);

INSERT INTO `datingapp`.`characteristic`
(`id`,
`timestamp`,
`name`,
`description`,
`is_selection`,
`author_id`,
`is_standart`)
VALUES
(3,
"2023-06-26 17:18:42",
"Alter",
"Diese Eigenschaft soll dein Alter identifizieren",
false,
0,
true);

INSERT INTO `datingapp`.`characteristic`
(`id`,
`timestamp`,
`name`,
`description`,
`is_selection`,
`author_id`,
`is_standart`)
VALUES
(4,
"2023-06-26 17:18:42",
"Koerpergroesse (in cm)",
"Diese Eigenschaft soll deine Koerpergroesse in Zentimeter identifizieren",
false,
0,
true);

INSERT INTO `datingapp`.`characteristic`
(`id`,
`timestamp`,
`name`,
`description`,
`is_selection`,
`author_id`,
`is_standart`)
VALUES
(5,
"2023-06-26 17:18:42",
"Haarfarbe",
"Diese Eigenschaft soll deine Haarfarbe identifizieren",
true,
0,
true);

INSERT INTO `datingapp`.`characteristic`
(`id`,
`timestamp`,
`name`,
`description`,
`is_selection`,
`author_id`,
`is_standart`)
VALUES
(6,
"2023-06-26 17:18:42",
"Raucher",
"Diese Eigenschaft soll dein Rauchverhalten identifizieren",
true,
0,
true);

INSERT INTO `datingapp`.`characteristic`
(`id`,
`timestamp`,
`name`,
`description`,
`is_selection`,
`author_id`,
`is_standart`)
VALUES
(7,
"2023-06-26 17:18:42",
"Religion",
"Diese Eigenschaft soll deine Religion identifizieren",
true,
0,
true);

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(1,
"2023-06-26 17:18:42",
1,
"Weiblich");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(2,
"2023-06-26 17:18:42",
1,
"Maennlich");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(3,
"2023-06-26 17:18:42",
1,
"Divers");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(4,
"2023-06-26 17:18:42",
2,
"Freundschaft");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(5,
"2023-06-26 17:18:42",
2,
"Beziehung");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(6,
"2023-06-26 17:18:42",
2,
"Chat");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(7,
"2023-06-26 17:18:42",
5,
"Schwarz");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(8,
"2023-06-26 17:18:42",
5,
"Braun");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(9,
"2023-06-26 17:18:42",
5,
"Blond");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(10,
"2023-06-26 17:18:42",
5,
"Rot");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(11,
"2023-06-26 17:18:42",
6,
"Haeufig");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(12,
"2023-06-26 17:18:42",
6,
"Gelegenheitsraucher");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(13,
"2023-06-26 17:18:42",
6,
"Nie");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(14,
"2023-06-26 17:18:42",
7,
"Christentum");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(15,
"2023-06-26 17:18:42",
7,
"Islam");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(16,
"2023-06-26 17:18:42",
7,
"Judentum");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(17,
"2023-06-26 17:18:42",
7,
"Buddhismus");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(18,
"2023-06-26 17:18:42",
7,
"Atheist");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(19,
"2023-06-26 17:18:42",
7,
"Sonstiges");

INSERT INTO `datingapp`.`selection`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`)
VALUES
(20,
"2023-06-26 17:18:42",
7,
"Egal");

INSERT INTO `datingapp`.`description`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`,
`max_answer`)
VALUES
(1,
"2023-06-26 17:18:42",
3,
"",
"-");

INSERT INTO `datingapp`.`description`
(`id`,
`timestamp`,
`characteristic_id`,
`answer`,
`max_answer`)
VALUES
(2,
"2023-06-26 17:18:42",
4,
"",
"-");