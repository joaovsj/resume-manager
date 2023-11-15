-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 15-Nov-2023 às 15:29
-- Versão do servidor: 8.0.31
-- versão do PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `resumes`
--
CREATE DATABASE IF NOT EXISTS `resumes` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `resumes`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `candidates`
--

DROP TABLE IF EXISTS `candidates`;
CREATE TABLE IF NOT EXISTS `candidates` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `telephone` bigint DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `candidates`
--

INSERT INTO `candidates` (`id`, `name`, `telephone`, `description`) VALUES
(1, 'Becky Peegrem', 2317857230, 'dignissim vestibulum vestibulum ante ipsum'),
(2, 'Gracia Lygoe', 2114995032, 'a ipsum integer a nibh '),
(3, 'Jasmin Hastings', 4516675712, 'aenean sit amet justo morbi ut'),
(4, 'Nessy Bagenal', 6051260676, 'sit amet sem fusce consequat nulla nisl nunc nisl'),
(5, 'Randal Blything', 42416682020, 'pede lobortis ligula sit amet'),
(6, 'Cedric Chinge', 7113059606, 'rhoncus aliquet pulvinar '),
(7, 'Boone Gotcliff', 48425660709, 'nibh ligula nec sem duis '),
(8, 'Osbourn Defraine', 98489386349, 'orci pede venenatis non '),
(9, 'Giffard Robard', 28499378739, 'elementum in hac habitasse'),
(10, 'Arron Stuckford', 61468525649, 'auctor sed tristique in '),
(11, 'Kalli Seggie', 93436902509, 'luctus et ultrices posuere '),
(12, 'Dewie Allaway', 254627414, 'fusce congue diam id ornare '),
(13, 'Mellie Canadas', 11499541509, 'lobortis convallis tortor '),
(14, 'Norrie Oherlihy', 20467916459, 'morbi ut odio cras mi pede'),
(15, 'Allsun Drysdall', 74435171659, 'dolor vel est donec odio '),
(16, 'Douglass Cooke', 14439334189, 'bibendum felis sed interdum'),
(17, 'Zsa zsa Cannavan', 42474039979, 'enim in tempor turpis nec'),
(18, 'Kristal Gurley', 34413616399, 'sit amet turpis elementum '),
(19, 'Caritta Sealeaf', 69434603969, 'nisl nunc rhoncus dui vel'),
(20, 'Jodi Sappson', 23451662069, 'tincidunt in leo maecenas ');

-- --------------------------------------------------------

--
-- Estrutura da tabela `grades`
--

DROP TABLE IF EXISTS `grades`;
CREATE TABLE IF NOT EXISTS `grades` (
  `id` int NOT NULL AUTO_INCREMENT,
  `interview` int DEFAULT NULL,
  `theory` int DEFAULT NULL,
  `practice` int DEFAULT NULL,
  `softSkill` int DEFAULT NULL,
  `id_candidate` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_candidate` (`id_candidate`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Extraindo dados da tabela `grades`
--

INSERT INTO `grades` (`id`, `interview`, `theory`, `practice`, `softSkill`, `id_candidate`) VALUES
(1, 5, 4, 5, 5, 1),
(2, 3, 8, 4, 2, 2),
(3, 1, 6, 10, 9, 3),
(4, 2, 6, 9, 4, 4),
(5, 4, 10, 4, 5, 5),
(6, 6, 1, 1, 9, 6),
(7, 10, 1, 7, 6, 7),
(8, 8, 5, 9, 1, 8),
(9, 7, 7, 4, 7, 9),
(10, 10, 3, 6, 1, 10),
(11, 6, 4, 9, 2, 11),
(12, 5, 6, 5, 3, 12),
(13, 3, 4, 8, 9, 13),
(14, 6, 9, 7, 5, 14),
(15, 7, 9, 2, 3, 15),
(16, 1, 9, 3, 4, 16),
(17, 9, 9, 2, 10, 17),
(18, 5, 7, 3, 2, 18),
(19, 9, 7, 8, 10, 19),
(20, 3, 4, 5, 4, 20);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
