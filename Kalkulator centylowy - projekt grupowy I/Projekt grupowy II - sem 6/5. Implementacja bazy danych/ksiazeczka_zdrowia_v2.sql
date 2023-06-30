-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Apr 24, 2023 at 09:58 AM
-- Wersja serwera: 10.4.28-MariaDB
-- Wersja PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ksiazeczka_zdrowia`
--
-- WYWALA CAŁĄ BAZE DANYCH!!!
DROP Database if exists ksiazeczka_zdrowia;
CREATE Database ksiazeczka_zdrowia;
USE ksiazeczka_zdrowia;
-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pacjent`
--

CREATE TABLE `pacjent` (
  `pesel` varchar(11) NOT NULL,
  `imie` varchar(20) NOT NULL,
  `nazwisko` varchar(50) NOT NULL,
  `płeć` varchar(4) NOT NULL,
  `imia_ojca` varchar(20) DEFAULT NULL,
  `imie_matki` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `pacjent`
--

INSERT INTO `pacjent` (`pesel`, `imie`, `nazwisko`, `płeć`, `imia_ojca`, `imie_matki`) VALUES
(22291295576, 'Maciej', 'Kowalski', 'boy', 'Tomasz', 'Ewa');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `siatka_centylowa`
--

CREATE TABLE `siatka_centylowa` (
  `id` int NOT NULL,
  `pesel` varchar(11) NOT NULL,
  `wiek[miesiace]` smallint NOT NULL,
  `wysokosc[cm]` float DEFAULT NULL,
  `waga[kg]` float DEFAULT NULL,
  `obwod_glowy[cm]` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_polish_ci;

--
-- Dumping data for table `siatka_centylowa`
--

INSERT INTO `siatka_centylowa` (`id`, `pesel`, `wiek[miesiace]`, `wysokosc[cm]`, `waga[kg]`, `obwod_glowy[cm]`) VALUES
(1, "22291295576", 0, 51, 4.4, 35),
(2, "22291295576", 1, 55, 4.625, 36),
(3, "22291295576", 2, 63, 5.565, 38),
(4, "22291295576", 3, 64, 6.3, 38),
(5, "22291295576", 4, 66, 7, 40);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `pacjent`
--
ALTER TABLE `pacjent`
  ADD PRIMARY KEY (`pesel`);

--
-- Indeksy dla tabeli `siatka_centylowa`
--
ALTER TABLE `siatka_centylowa`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `siatka_centylowa`
--
ALTER TABLE `siatka_centylowa`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

ALTER TABLE siatka_centylowa
  ADD CONSTRAINT FK_pesel FOREIGN KEY (pesel) REFERENCES pacjent(pesel);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
