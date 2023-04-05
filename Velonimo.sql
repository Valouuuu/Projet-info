--
-- Création de la base de données :
--

DROP DATABASE IF EXISTS Velonimo;

CREATE DATABASE Velonimo CHARACTER SET 'utf8';

USE Velonimo;

CREATE TABLE Joueur (
	jou_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	jou_user VARCHAR(30) NOT NULL,
    jou_mdp VARCHAR(30) NOT NULL,
    jou_age INT NOT NULL,
    jou_win INT NOT NULL,
    jou_lose INT NOT NULL,
	PRIMARY KEY (jou_id)
    
)
CREATE TABLE Cartes (
	car_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	car_user VARCHAR(30) NOT NULL,
    car_mdp VARCHAR(30) NOT NULL,
	PRIMARY KEY (car_id)
    
)

INSERT INTO Cartes
VALUES	(1, 'rouge', '1'), (2, 'rouge', '2'), (3, 'rouge', '3'), (4, 'rouge', '4'), (5, 'rouge', '5'), (6, 'rouge', '6'), (7, 'rouge', '7'),
(8, 'bleu', '1'), (9, 'bleu', '2'), (10, 'bleu', '3'), (11, 'bleu', '4'), (12, 'bleu', '5'), (13, 'bleu', '6'), (14, 'bleu', '7'),
(15, 'vert', '1'), (16, 'vert', '2'), (17, 'vert', '3'), (18, 'vert', '4'), (19, 'vert', '5'), (20, 'vert', '6'), (21, 'vert', '7'),
(22, 'jaune', '1'), (23, 'jaune', '2'), (24, 'jaune', '3'), (25, 'jaune', '4'), (26, 'jaune', '5'), (27, 'jaune', '6'), (28, 'jaune', '7'),
(29, 'rose', '1'), (30, 'rose', '2'), (31, 'rose', '3'), (32, 'rose', '4'), (33, 'rose', '5'), (34, 'rose', '6'), (35, 'rose', '7'),
(36, 'gris', '1'), (37, 'gris', '2'), (38, 'gris', '3'), (39, 'gris', '4'), (40, 'gris', '5'), (41, 'gris', '6'), (42, 'gris', '7'),
(43, 'marron', '1'), (44, 'marron', '2'), (45, 'marron', '3'), (46, 'marron', '4'), (47, 'marron', '5'), (48, 'marron', '6'), (49, 'marron', '7'),
(50, 'baroudeur', '25'), (51, 'baroudeur', '30'), (52, 'baroudeur', '35'), (53, 'baroudeur', '40'), (54, 'baroudeur', '45'), (55, 'baroudeur', '50'),
;

ENGINE=INNODB;
INSERT INTO Joueur
VALUES ()
