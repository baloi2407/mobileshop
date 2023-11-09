-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: Nov 09, 2023 at 03:24 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mobileshop`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` bigint(20) NOT NULL COMMENT 'product id',
  `pro_name` varchar(100) NOT NULL COMMENT 'product name',
  `price` float NOT NULL COMMENT 'original price',
  `discount` float NOT NULL COMMENT 'discount percent',
  `summary` varchar(100) DEFAULT NULL COMMENT 'product summary',
  `content` text DEFAULT NULL COMMENT 'product content',
  `image` text DEFAULT NULL COMMENT 'product image',
  `quantity` int(11) DEFAULT NULL COMMENT 'stock quantity',
  `brand_id` bigint(20) NOT NULL COMMENT 'brand id',
  `display_size` varchar(50) DEFAULT NULL,
  `os` varchar(50) DEFAULT NULL COMMENT 'operating system',
  `rear_camera` varchar(50) DEFAULT NULL,
  `front_camera` varchar(20) DEFAULT NULL,
  `chip` varchar(50) DEFAULT NULL,
  `ram` varchar(50) DEFAULT NULL,
  `storage` varchar(50) DEFAULT NULL,
  `sim` varchar(100) DEFAULT NULL,
  `battery_capacity` varchar(50) DEFAULT NULL,
  `sku` varchar(100) DEFAULT NULL COMMENT 'Product code: provided by the supplier for each product\r\n',
  `alias` varchar(100) DEFAULT NULL COMMENT 'SEO',
  `title` varchar(100) DEFAULT NULL COMMENT 'SEO',
  `description` text DEFAULT NULL COMMENT 'SEO',
  `image_share` text DEFAULT NULL COMMENT 'SEO',
  `status` varchar(50) DEFAULT NULL COMMENT '0.block 1.active',
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `pro_name`, `price`, `discount`, `summary`, `content`, `image`, `quantity`, `brand_id`, `display_size`, `os`, `rear_camera`, `front_camera`, `chip`, `ram`, `storage`, `sim`, `battery_capacity`, `sku`, `alias`, `title`, `description`, `image_share`, `status`, `created_at`, `updated_at`) VALUES
(11, 'iphone', 100, 0, NULL, '', 'brand/new_product6_LzY2izN.jpg', 0, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '', NULL, 'Active', '2023-10-31 03:53:47', '2023-11-06 16:10:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'product id', AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
