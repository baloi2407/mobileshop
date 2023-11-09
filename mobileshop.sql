-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3308
-- Generation Time: Nov 09, 2023 at 03:33 AM
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
-- Table structure for table `about`
--

CREATE TABLE `about` (
  `id` bigint(20) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `content` text DEFAULT NULL,
  `image` text DEFAULT NULL,
  `status` tinyint(4) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `app_product`
--

CREATE TABLE `app_product` (
  `id` bigint(20) NOT NULL,
  `title` varchar(100) NOT NULL,
  `selling_price` double NOT NULL,
  `discounted_price` double NOT NULL,
  `description` longtext NOT NULL,
  `composition` longtext NOT NULL,
  `prodapp` longtext NOT NULL,
  `category` varchar(2) NOT NULL,
  `product_image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'add product');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_group_permissions`
--

INSERT INTO `auth_group_permissions` (`id`, `group_id`, `permission_id`) VALUES
(1, 1, 25);

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add product', 7, 'add_product'),
(26, 'Can change product', 7, 'change_product'),
(27, 'Can delete product', 7, 'delete_product'),
(28, 'Can view product', 7, 'view_product'),
(29, 'Can add customer', 8, 'add_customer'),
(30, 'Can change customer', 8, 'change_customer'),
(31, 'Can delete customer', 8, 'delete_customer'),
(32, 'Can view customer', 8, 'view_customer'),
(33, 'Can add cart', 9, 'add_cart'),
(34, 'Can change cart', 9, 'change_cart'),
(35, 'Can delete cart', 9, 'delete_cart'),
(36, 'Can view cart', 9, 'view_cart'),
(37, 'Can add payment', 10, 'add_payment'),
(38, 'Can change payment', 10, 'change_payment'),
(39, 'Can delete payment', 10, 'delete_payment'),
(40, 'Can view payment', 10, 'view_payment'),
(41, 'Can add order placed', 11, 'add_orderplaced'),
(42, 'Can change order placed', 11, 'change_orderplaced'),
(43, 'Can delete order placed', 11, 'delete_orderplaced'),
(44, 'Can view order placed', 11, 'view_orderplaced'),
(45, 'Can add wishlist', 12, 'add_wishlist'),
(46, 'Can change wishlist', 12, 'change_wishlist'),
(47, 'Can delete wishlist', 12, 'delete_wishlist'),
(48, 'Can view wishlist', 12, 'view_wishlist');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$x6akCOOJt3vJQp1oP1Y6hm$Nf5teD7PlDp6p+Hu1XliRUhgPXrFA8oFq41DfuebtVo=', '2023-11-04 06:05:43.235767', 1, 'admin', '', '', '', 1, 1, '2023-10-27 05:15:06.815884'),
(2, 'pbkdf2_sha256$600000$fargOXTlzQhXMmJ3NW8Vya$jJKeJKYpS+4j5lxAXlrV5addVM5Mo1E/v+F0VitQjbw=', '2023-11-01 15:53:55.485746', 0, 'admin123', '', '', '', 1, 1, '2023-11-01 03:18:48.000000'),
(3, 'pbkdf2_sha256$600000$kuMcNcG3vwIFzuZLWZ5OZt$Jsn9wK6tmclgVvYt+KfcLR47LnG61BFkRosmA2mWE7I=', '2023-11-03 02:01:53.868474', 0, 'admin4', '', '', 'kiwi@email.com', 0, 1, '2023-11-03 01:12:31.170456');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `brands`
--

CREATE TABLE `brands` (
  `id` bigint(20) NOT NULL,
  `brand_name` varchar(100) NOT NULL COMMENT 'brand name',
  `summary` varchar(100) DEFAULT NULL COMMENT 'brand summary',
  `content` text DEFAULT NULL COMMENT 'brand content',
  `image` text DEFAULT NULL COMMENT 'brand image',
  `sku` varchar(100) DEFAULT NULL COMMENT 'brand code: provided by the supplier for each product\r\n',
  `alias` varchar(100) DEFAULT NULL COMMENT 'SEO',
  `title` varchar(100) DEFAULT NULL COMMENT 'SEO',
  `description` text DEFAULT NULL COMMENT 'SEO',
  `image_share` text DEFAULT NULL COMMENT 'SEO',
  `status` varchar(50) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `brands`
--

INSERT INTO `brands` (`id`, `brand_name`, `summary`, `content`, `image`, `sku`, `alias`, `title`, `description`, `image_share`, `status`, `created_at`, `updated_at`) VALUES
(5, 'Apple', NULL, '', 'brand/new_product6_7YQ4jvR.jpg', NULL, NULL, NULL, '', NULL, 'Active', '2023-10-30 16:56:40', '2023-11-01 03:03:33'),
(6, 'Samsung', NULL, '', 'brand/new_product8_Vq3zaVz.jpg', NULL, NULL, NULL, '', NULL, 'Block', '2023-10-31 03:54:51', '2023-11-01 03:15:20'),
(7, 'Huewei', NULL, '', '', NULL, NULL, NULL, '', NULL, 'Active', '2023-11-06 16:18:28', '2023-11-06 16:18:37'),
(8, 'Xiaomi', NULL, '', '', NULL, NULL, NULL, '', NULL, 'Active', '2023-11-06 16:18:41', '2023-11-06 16:18:46'),
(9, 'Oppo', NULL, '', '', NULL, NULL, NULL, '', NULL, 'Active', '2023-11-06 16:18:48', '2023-11-06 16:18:59');

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `id` bigint(20) NOT NULL,
  `quantity` int(11) NOT NULL,
  `prod_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`id`, `quantity`, `prod_id`, `user_id`) VALUES
(4, 2, 11, 1);

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` bigint(20) NOT NULL,
  `cat_name` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `alias` varchar(100) DEFAULT NULL,
  `content` longtext DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `sku` varchar(100) DEFAULT NULL,
  `status` varchar(50) NOT NULL,
  `summary` varchar(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` bigint(20) NOT NULL,
  `contact_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `subject` varchar(100) DEFAULT NULL,
  `message` text DEFAULT NULL,
  `status` tinyint(4) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  `avatar` text DEFAULT NULL,
  `user_id` bigint(20) NOT NULL,
  `status` varchar(50) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `first_name`, `last_name`, `email`, `address`, `date_of_birth`, `phone`, `avatar`, `user_id`, `status`, `created_at`, `updated_at`) VALUES
(2, 'nguyen ba', 'loi', 'nguyenbaloi123@gmail.com', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.', '2002-11-06', 363664067, 'avatar/3.png', 1, 'Block', '2023-11-03 00:48:55', '2023-11-03 16:40:15');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-10-27 05:33:46.947015', '0', 'Category object (0)', 1, '[{\"added\": {}}]', 13, 1),
(2, '2023-10-28 06:38:30.424962', '1', 'i', 1, '[{\"added\": {}}]', 7, 1),
(3, '2023-10-29 09:32:42.709869', '0', 'Category object (0)', 2, '[{\"changed\": {\"fields\": [\"Summary\", \"Content\", \"Sku\", \"Description\", \"Status\"]}}]', 13, 1),
(4, '2023-10-29 09:36:38.534208', '0', 'Category object (0)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 13, 1),
(5, '2023-10-29 09:48:43.887253', '0', 'Category object (0)', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 13, 1),
(6, '2023-10-29 10:09:38.819860', '0', 'Category object (0)', 1, '[{\"added\": {}}]', 13, 1),
(7, '2023-10-29 10:14:24.540579', '2', 'Category object (2)', 1, '[{\"added\": {}}]', 13, 1),
(8, '2023-10-29 15:37:55.872320', '2', 'iphone', 1, '[{\"added\": {}}]', 7, 1),
(9, '2023-10-29 16:39:14.919080', '2', 'iphone', 2, '[]', 7, 1),
(10, '2023-10-29 16:39:28.121745', '2', 'iphone', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 7, 1),
(11, '2023-10-30 04:20:37.454283', '3', 'Iphone 15', 1, '[{\"added\": {}}]', 7, 1),
(12, '2023-10-30 06:17:08.359084', '4', 'phone', 1, '[{\"added\": {}}]', 7, 1),
(13, '2023-10-30 06:17:43.463060', '5', 'phone', 1, '[{\"added\": {}}]', 7, 1),
(14, '2023-10-30 06:27:34.973558', '6', 'ccccccc', 1, '[{\"added\": {}}]', 7, 1),
(15, '2023-10-30 06:28:27.686324', '7', 'c', 1, '[{\"added\": {}}]', 7, 1),
(16, '2023-10-30 08:05:05.589810', '8', 'iphone 5', 1, '[{\"added\": {}}]', 7, 1),
(17, '2023-10-30 08:13:26.687862', '3', 'opp', 1, '[{\"added\": {}}]', 14, 1),
(18, '2023-10-30 08:17:38.560613', '9', 'iphone 1', 1, '[{\"added\": {}}]', 7, 1),
(19, '2023-10-30 08:18:07.944932', '10', 'x', 1, '[{\"added\": {}}]', 7, 1),
(20, '2023-10-30 15:53:02.795271', '3', 'opp', 3, '', 14, 1),
(21, '2023-10-30 15:53:02.839275', '2', 'Apple', 3, '', 14, 1),
(22, '2023-10-30 15:53:02.881085', '1', 'Samsung', 3, '', 14, 1),
(23, '2023-10-30 16:06:19.626991', '4', 'Apple', 1, '[{\"added\": {}}]', 14, 1),
(24, '2023-10-30 16:33:33.546797', '4', 'Apple', 2, '[{\"changed\": {\"fields\": [\"Sku\"]}}]', 14, 1),
(25, '2023-10-30 16:56:59.353761', '5', 'Apple', 1, '[{\"added\": {}}]', 14, 1),
(26, '2023-10-30 16:57:50.967024', '5', 'Apple', 2, '[]', 14, 1),
(27, '2023-10-30 16:58:13.111216', '5', 'Apple', 2, '[]', 14, 1),
(28, '2023-10-31 03:54:20.798234', '11', 'iphone', 1, '[{\"added\": {}}]', 7, 1),
(29, '2023-10-31 03:57:10.500475', '6', '@#!', 1, '[{\"added\": {}}]', 14, 1),
(30, '2023-10-31 04:00:16.937522', '6', 'ncncncn', 2, '[{\"changed\": {\"fields\": [\"Brand name\"]}}]', 14, 1),
(31, '2023-10-31 04:00:30.871436', '6', 'ncncncn#@', 2, '[{\"changed\": {\"fields\": [\"Brand name\"]}}]', 14, 1),
(32, '2023-10-31 16:16:20.856748', '6', 'ddd', 2, '[{\"changed\": {\"fields\": [\"Brand name\"]}}]', 14, 1),
(33, '2023-10-31 16:16:29.148763', '6', 'ddd', 2, '[]', 14, 1),
(34, '2023-10-31 16:16:37.661517', '6', 'ddd###', 2, '[{\"changed\": {\"fields\": [\"Brand name\"]}}]', 14, 1),
(35, '2023-10-31 16:17:12.161979', '6', 'ddd', 2, '[{\"changed\": {\"fields\": [\"Brand name\"]}}]', 14, 1),
(36, '2023-10-31 16:17:21.705702', '6', 'ddd#1', 2, '[{\"changed\": {\"fields\": [\"Brand name\"]}}]', 14, 1),
(37, '2023-10-31 16:20:03.350207', '6', 'ddd#1', 2, '[]', 14, 1),
(38, '2023-10-31 16:22:13.617200', '6', 'ddd#1', 2, '[]', 14, 1),
(39, '2023-10-31 16:24:59.311954', '6', 'chú', 2, '[{\"changed\": {\"fields\": [\"Brand name\"]}}]', 14, 1),
(40, '2023-11-01 02:59:19.911323', '5', 'Apple', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 14, 1),
(41, '2023-11-01 02:59:36.729739', '5', 'Apple', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 14, 1),
(42, '2023-11-01 03:11:59.822808', '6', 'Samsung', 2, '[{\"changed\": {\"fields\": [\"Brand name\", \"Status\"]}}]', 14, 1),
(43, '2023-11-01 03:15:20.291782', '6', 'Samsung', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 14, 1),
(44, '2023-11-01 03:17:26.438123', '1', 'add product', 1, '[{\"added\": {}}]', 3, 1),
(45, '2023-11-01 03:18:49.181701', '2', 'admin123', 1, '[{\"added\": {}}]', 4, 1),
(46, '2023-11-01 03:19:03.652033', '2', 'admin123', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(47, '2023-11-01 03:19:18.108436', '2', 'admin123', 2, '[{\"changed\": {\"fields\": [\"Staff status\"]}}]', 4, 1),
(48, '2023-11-03 00:49:25.918778', '2', 'nguyenbaloi2407@gmail.com', 1, '[{\"added\": {}}]', 8, 1),
(49, '2023-11-03 17:17:51.100523', '0', 'Cart object (0)', 1, '[{\"added\": {}}]', 9, 1),
(50, '2023-11-06 16:10:00.844660', '11', 'iphone', 2, '[{\"changed\": {\"fields\": [\"Quantity\"]}}]', 7, 1),
(51, '2023-11-06 16:18:37.638526', '7', 'Huewei', 1, '[{\"added\": {}}]', 14, 1),
(52, '2023-11-06 16:18:46.573038', '8', 'Xiaomi', 1, '[{\"added\": {}}]', 14, 1),
(53, '2023-11-06 16:18:59.301613', '9', 'Oppo', 1, '[{\"added\": {}}]', 14, 1),
(54, '2023-11-07 01:31:59.753219', '1', 'OrderPlaced object (1)', 2, '[{\"changed\": {\"fields\": [\"Status\"]}}]', 11, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(14, 'app', 'brand'),
(9, 'app', 'cart'),
(13, 'app', 'category'),
(8, 'app', 'customer'),
(11, 'app', 'orderplaced'),
(10, 'app', 'payment'),
(7, 'app', 'product'),
(12, 'app', 'wishlist'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-10-27 05:06:05.522367'),
(2, 'auth', '0001_initial', '2023-10-27 05:06:19.074108'),
(3, 'admin', '0001_initial', '2023-10-27 05:06:21.904083'),
(30, 'admin', '0002_logentry_remove_auto_add', '2023-11-02 15:34:23.100856'),
(31, 'admin', '0003_logentry_add_action_flag_choices', '2023-11-02 15:34:23.244414'),
(32, 'app', '0001_initial', '2023-11-02 15:34:23.743652');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('k4g0d30wzlojf0vvkzx5cqm91edstn2u', '.eJxVjDsOwjAQBe_iGln2Lv5R0ucMltcfHEC2FCcV4u4QKQW0b2bei_mwrdVvIy9-TuzCJDv9bhTiI7cdpHtot85jb-syE98VftDBp57y83q4fwc1jPqtSyhnBQohYjEGgUTRiqJ1MYGRFqROpBQKIpNTdERZY4CMiMIJq4C9P-HmN5c:1qz9mx:a6x6wlO_N3xEivH3rSgyxEtgxrFkNRHMMimbeZGm5vw', '2023-11-18 06:05:43.342132'),
('krlj4diyk3p1oe5f7pfl36s8exbdkctj', '.eJxVjDsOwjAQBe_iGln2Lv5R0ucMltcfHEC2FCcV4u4QKQW0b2bei_mwrdVvIy9-TuzCJDv9bhTiI7cdpHtot85jb-syE98VftDBp57y83q4fwc1jPqtSyhnBQohYjEGgUTRiqJ1MYGRFqROpBQKIpNTdERZY4CMiMIJq4C9P-HmN5c:1qy1nP:rko93eT-koRCywgWPbetIcGfGnDu3Sr_kq2MC-m6Src', '2023-11-15 03:21:31.669958');

-- --------------------------------------------------------

--
-- Table structure for table `orderplaced`
--

CREATE TABLE `orderplaced` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `customer_id` bigint(20) DEFAULT NULL,
  `prod_id` bigint(20) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `payment_id` bigint(20) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orderplaced`
--

INSERT INTO `orderplaced` (`id`, `user_id`, `customer_id`, `prod_id`, `quantity`, `payment_id`, `status`, `created_at`, `updated_at`) VALUES
(1, 1, 2, 11, 3, 7, 'On The Way', '2023-11-04 08:30:33', '2023-11-07 01:31:59');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `razorpay_order_id` int(11) DEFAULT NULL,
  `razorpay_payment_status` int(11) DEFAULT NULL,
  `razorpay_payment_id` int(11) DEFAULT NULL,
  `paid` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`id`, `user_id`, `amount`, `razorpay_order_id`, `razorpay_payment_status`, `razorpay_payment_id`, `paid`, `status`, `created_at`, `updated_at`) VALUES
(7, 1, 300, 0, 0, 0, 1, NULL, '0000-00-00 00:00:00', '0000-00-00 00:00:00');

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

-- --------------------------------------------------------

--
-- Table structure for table `reviews`
--

CREATE TABLE `reviews` (
  `id` bigint(20) NOT NULL,
  `prod_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `rating` float DEFAULT NULL,
  `comment` text DEFAULT NULL,
  `alias` varchar(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `image_share` text DEFAULT NULL,
  `status` tinyint(4) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `wishlist`
--

CREATE TABLE `wishlist` (
  `id` bigint(20) NOT NULL,
  `prod_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `wishlist`
--

INSERT INTO `wishlist` (`id`, `prod_id`, `user_id`) VALUES
(6, 11, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `about`
--
ALTER TABLE `about`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `app_product`
--
ALTER TABLE `app_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `brands`
--
ALTER TABLE `brands`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `orderplaced`
--
ALTER TABLE `orderplaced`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `wishlist`
--
ALTER TABLE `wishlist`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `about`
--
ALTER TABLE `about`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `app_product`
--
ALTER TABLE `app_product`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `brands`
--
ALTER TABLE `brands`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `orderplaced`
--
ALTER TABLE `orderplaced`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'product id', AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `wishlist`
--
ALTER TABLE `wishlist`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
