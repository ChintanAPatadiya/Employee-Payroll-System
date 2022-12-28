-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 19, 2021 at 07:44 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ems`
--

-- --------------------------------------------------------

--
-- Table structure for table `emp_salary`
--

CREATE TABLE `emp_salary` (
  `e_id` int(11) NOT NULL,
  `designation` text NOT NULL,
  `name` text NOT NULL,
  `age` text NOT NULL,
  `gender` text NOT NULL,
  `email` text NOT NULL,
  `hr_location` text NOT NULL,
  `doj` text NOT NULL,
  `dob` text NOT NULL,
  `experience` text NOT NULL,
  `proof_id` text NOT NULL,
  `contact_no` text NOT NULL,
  `status` text NOT NULL,
  `address` text NOT NULL,
  `month` text NOT NULL,
  `year` text NOT NULL,
  `basic_salary` text NOT NULL,
  `total_days` text NOT NULL,
  `absent_days` text NOT NULL,
  `medical` text NOT NULL,
  `pf` text NOT NULL,
  `convence` text NOT NULL,
  `net_salary` text NOT NULL,
  `salary_receipt` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `emp_salary`
--

INSERT INTO `emp_salary` (`e_id`, `designation`, `name`, `age`, `gender`, `email`, `hr_location`, `doj`, `dob`, `experience`, `proof_id`, `contact_no`, `status`, `address`, `month`, `year`, `basic_salary`, `total_days`, `absent_days`, `medical`, `pf`, `convence`, `net_salary`, `salary_receipt`) VALUES
(1, 'software developer', 'chintan', '25', 'Male', 'chintan11402@gmail.com', 'main branch', '23/03/2019', '11/04/1997', '3 years', '1122336655', '1236547890', 'senior developer', 'fdghjkkanthar chowk, behind divya agarbatti, devchakla, nadiad', '0', '0', '0', '1', '0', '0', '0', '0', '0.0', '1.txt'),
(5, 't', 't', '0', 'e', 'w', 'q', 'y', 'u', 'i', 'o', 'p', 'q', 'qawsedrftghyjkl', 'apr', '2021', '20000', '30', '13', '3456', '7654', '1234', '3456', 'Receipt'),
(6, 'q', 'w', '0', 'r', 't', 'y', 'a', 's', 'd', 'f', 'g', 'h', 'zxcvbnm', 'may', '2021', '41000', '31', '20', '3214', '2568', '14785', '25896', 'Receipt'),
(7, 'q', 'w', '0', 'r', 't', 'y', 'a', 's', 'd', 'f', 'g', 'h', 'zxcvbnm', 'may', '2021', '41000', '31', '20', '3214', '2568', '14785', '25896', 'Receipt'),
(8, 'seo', 'chintan', '14', 'male', 'chi@gmail.com', 'ADS', '12-03-2000', '12-03-1956', '10 yrs', '1234567890', '9876543210', 'active', 'wedfghjkoiujhgfsrthjkldffgh', 'apr', '2021', '55000', '30', '5', '5000', '2310', '1564', '40087.33', '8.txt'),
(10, 'Software', 'xfgc', 'fhjhkj', 'dghg', 'ssdfghjkl', 'wsfdghjmn,', 'dfghjkl', 'fghjkl', 'dfghjkl', 'fghjk', 'dfghj', 'fghjmk,', 'fdghjk', 'dec', '2100', '40000', '31', '10', '2001', '1000', '1000', '25096.77', '10.txt');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `emp_salary`
--
ALTER TABLE `emp_salary`
  ADD PRIMARY KEY (`e_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `emp_salary`
--
ALTER TABLE `emp_salary`
  MODIFY `e_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
