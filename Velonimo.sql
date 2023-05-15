--
-- Création de la base de données :
--

DROP DATABASE IF EXISTS Velonimo;

CREATE DATABASE Velonimo CHARACTER SET 'utf8';

USE Velonimo;

CREATE TABLE Compte (
	com_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	com_user VARCHAR(30) NOT NULL,
    com_mdp VARCHAR(30) NOT NULL,
    com_age INT NOT NULL,
    com_win INT DEFAULT 0,
    com_lose INT DEFAULT 0,
	PRIMARY KEY (com_id)

)
ENGINE=INNODB;

CREATE TABLE Cartes (
	car_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	car_color VARCHAR(30) NOT NULL,
    car_value INT NOT NULL,
	car_image VARCHAR(30) NOT NULL,
	PRIMARY KEY (car_id)

)

ENGINE=INNODB;

INSERT INTO Cartes
VALUES	(1, 'rouge', 1 ,'card_1_red.png'), (2, 'rouge', 2 ,'card_2_red.png'), (3, 'rouge', 3 ,'card_3_red.png'), (4, 'rouge', 4 ,'card_4_red.png'), (5, 'rouge', 5 ,'card_5_red.png'), (6, 'rouge', 6 ,'card_6_red.png'), (7, 'rouge', 7 ,'card_7_red.png'),
(8, 'bleu', 1 ,'card_1_blue.png'), (9, 'bleu', 2,'card_2_blue.png'), (10, 'bleu', 3,'card_3_blue.png'), (11, 'bleu', 4,'card_4_blue.png'), (12, 'bleu', 5,'card_5_blue.png'), (13, 'bleu', 6,'card_6_blue.png'), (14, 'bleu', 7,'card_7_blue.png'),
(15, 'vert', 1 ,'card_1_green.png'), (16, 'vert', 2 ,'card_2_green.png'), (17, 'vert', 3 ,'card_3_green.png'), (18, 'vert', 4 ,'card_4_green.png'), (19, 'vert', 5 ,'card_5_green.png'), (20, 'vert', 6 ,'card_6_green.png'), (21, 'vert', 7 ,'card_7_green.png'),
(22, 'jaune', 1 ,'card_1_yellow.png'), (23, 'jaune', 2,'card_2_yellow.png'), (24, 'jaune', 3,'card_3_yellow.png'), (25, 'jaune', 4,'card_4_yellow.png'), (26, 'jaune', 5,'card_5_yellow.png'), (27, 'jaune', 6,'card_6_yellow.png'), (28, 'jaune', 7,'card_7_yellow.png'),
(29, 'rose', 1 ,'card_1_pink.png'), (30, 'rose', 2 ,'card_2_pink.png'), (31, 'rose', 3 ,'card_3_pink.png'), (32, 'rose', 4 ,'card_4_pink.png'), (33, 'rose', 5 ,'card_5_pink.png'), (34, 'rose', 6 ,'card_6_pink.png'), (35, 'rose', 7 ,'card_7_pink.png'),
(36, 'gris', 1 ,'card_1_grey.png'), (37, 'gris', 2 ,'card_2_grey.png'), (38, 'gris', 3 ,'card_3_grey.png'), (39, 'gris', 4 ,'card_4_grey.png'), (40, 'gris', 5 ,'card_5_grey.png'), (41, 'gris', 6 ,'card_6_grey.png'), (42, 'gris', 7 ,'card_7_grey.png'),
(43, 'marron', 1 ,'card_1_brown.png'), (44, 'marron', 2 ,'card_2_brown.png'), (45, 'marron', 3 ,'card_3_brown.png'), (46, 'marron', 4 ,'card_4_brown.png'), (47, 'marron', 5 ,'card_5_brown.png'), (48, 'marron', 6 ,'card_6_brown.png'), (49, 'marron', 7 ,'card_7_brown.png'),
(50, 'baroudeur', 25 ,'card_1_baroudeur.png'), (51, 'baroudeur', 30 ,'card_2_baroudeur.png'), (52, 'baroudeur', 35 ,'card_3_baroudeur.png'), (53, 'baroudeur', 40 ,'card_4_baroudeur.png'), (54, 'baroudeur', 45 ,'card_5_baroudeur.png'), (55, 'baroudeur', 50 ,'card_6_baroudeur.png')
;

ENGINE=INNODB;
INSERT INTO Compte
VALUES ();
