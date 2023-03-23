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
ENGINE=INNODB;
INSERT INTO Joueur
VALUES ()
