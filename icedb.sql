-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 17, 2023 at 08:24 PM
-- Server version: 5.5.53
-- PHP Version: 5.6.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `icedb`
--

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(64) NOT NULL,
  `shopping` varchar(512) NOT NULL,
  `phone` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `name`, `shopping`, `phone`) VALUES
(2, 'Jasurbek Boltabayev', 'Gurlan ICE-Cream', '+998332853358'),
(3, 'Jo\'rbaek Egamov', 'Baxt qushi', '+998931234567'),
(4, 'Temur Eshqobilov', 'Mo\'jiza market', '+998941234321'),
(5, 'Bobur Babajanov', 'Babajanovlar', '+998914321545');

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(64) NOT NULL,
  `address` text NOT NULL,
  `salary` double NOT NULL,
  `salary_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`id`, `name`, `address`, `salary`, `salary_date`) VALUES
(2, 'Jasurbek Tajibayev', 'Urganch tumani', 9000000, '2023-04-01'),
(3, 'Sherzodbek Quziyev', 'Xazorasp', 5000000, '2023-04-01'),
(4, 'Jo\'rabek Egamov', 'Qo\'shko\'pir', 5000000, '2023-04-02'),
(5, 'Oxunjon Pirov', 'Shovot tumani', 5000000, '2023-04-02'),
(6, 'Abdulla Xabibullayev', 'Xonqa tumani', 1197000, '2023-04-17'),
(7, 'Oybek Allayarov', 'Xonqa', 6000000, '2023-04-04');

-- --------------------------------------------------------

--
-- Table structure for table `ice_cream`
--

CREATE TABLE `ice_cream` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` text NOT NULL,
  `price` double NOT NULL,
  `type_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `ice_cream`
--

INSERT INTO `ice_cream` (`id`, `name`, `price`, `type_id`) VALUES
(1, 'Bomba', 4500, 4),
(2, '1001 kecha', 6000, 3),
(3, 'Best', 3800, 4),
(4, 'Xochu', 4200, 4);

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `id` int(10) UNSIGNED NOT NULL,
  `customer_id` int(11) NOT NULL,
  `ice_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` double NOT NULL,
  `qqs` int(11) NOT NULL,
  `total_price` double NOT NULL,
  `sell_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`id`, `customer_id`, `ice_id`, `quantity`, `price`, `qqs`, `total_price`, `sell_date`) VALUES
(1, 2, 1, 50, 4500, 3, 231750, '2023-04-17'),
(2, 4, 2, 300, 6000, 3, 1854000, '2023-04-17');

-- --------------------------------------------------------

--
-- Table structure for table `store`
--

CREATE TABLE `store` (
  `id` int(10) UNSIGNED NOT NULL,
  `ice_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `made_date` date NOT NULL,
  `pull_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `store`
--

INSERT INTO `store` (`id`, `ice_id`, `quantity`, `made_date`, `pull_date`) VALUES
(1, 3, 50, '2023-04-13', '2023-05-13'),
(2, 1, 0, '2023-04-13', '2023-04-20'),
(3, 2, 700, '2023-04-14', '2023-04-30'),
(4, 4, 70, '2023-04-14', '2023-04-21'),
(5, 4, 100, '2023-04-17', '2023-04-24');

-- --------------------------------------------------------

--
-- Table structure for table `types`
--

CREATE TABLE `types` (
  `id` int(10) UNSIGNED NOT NULL,
  `type` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `types`
--

INSERT INTO `types` (`id`, `type`) VALUES
(1, 'Muzli'),
(3, 'Shakoladli'),
(4, 'Qaymoqli'),
(5, 'Pecheniali');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ice_cream`
--
ALTER TABLE `ice_cream`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `store`
--
ALTER TABLE `store`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `types`
--
ALTER TABLE `types`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `ice_cream`
--
ALTER TABLE `ice_cream`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `sales`
--
ALTER TABLE `sales`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `store`
--
ALTER TABLE `store`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `types`
--
ALTER TABLE `types`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
