-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 23, 2023 at 02:43 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sup_shop`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `cid` int(11) NOT NULL,
  `name` varchar(55) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`cid`, `name`) VALUES
(1, 'whey'),
(2, 'Gainner'),
(3, 'Creatine'),
(4, 'BCAA');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `pro_id` int(11) NOT NULL,
  `supplier` varchar(55) DEFAULT NULL,
  `category` varchar(55) DEFAULT NULL,
  `name` varchar(55) DEFAULT NULL,
  `price` varchar(55) DEFAULT NULL,
  `qty` varchar(55) DEFAULT NULL,
  `status` varchar(55) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`pro_id`, `supplier`, `category`, `name`, `price`, `qty`, `status`) VALUES
(3, 'Karan', 'whey', 'optimal nutrition', '1000', '195', 'Active'),
(4, 'Karan', 'BCAA', 'pro brust', '2000', '115', 'Active'),
(7, 'vrushabh', 'whey', '100% grow whey', '5000', '296', 'Active'),
(8, 'prasad', 'Creatine', 'MB', '300', '97', 'Active'),
(9, 'Karan', 'BCAA', 'muscle Mass', '2000', '115', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `report`
--

CREATE TABLE `report` (
  `bill_no` int(11) NOT NULL,
  `date` varchar(55) DEFAULT NULL,
  `cname` varchar(55) DEFAULT NULL,
  `contact` varchar(55) DEFAULT NULL,
  `bill_amt` varchar(55) DEFAULT NULL,
  `bill_dics` varchar(55) DEFAULT NULL,
  `net_pay` varchar(55) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `report`
--

INSERT INTO `report` (`bill_no`, `date`, `cname`, `contact`, `bill_amt`, `bill_dics`, `net_pay`) VALUES
(356224, '22/04/2023', 'ruihr', '9067467472', '7000', '5', '6000'),
(396161, '23/04/2023', 'Ritesh', '9090909090', '5300', '265', '5035');

-- --------------------------------------------------------

--
-- Table structure for table `supplier`
--

CREATE TABLE `supplier` (
  `invoice` int(11) NOT NULL,
  `name` varchar(55) DEFAULT NULL,
  `contact` varchar(55) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `supplier`
--

INSERT INTO `supplier` (`invoice`, `name`, `contact`) VALUES
(1, 'Karan', '7030139430'),
(2, 'prasad', '7875140747'),
(3, 'vrushabh', '8389598976'),
(5, NULL, NULL),
(7, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `userinfo`
--

CREATE TABLE `userinfo` (
  `emp_id` int(11) NOT NULL,
  `contact` varchar(55) DEFAULT NULL,
  `name` varchar(55) DEFAULT NULL,
  `email` varchar(55) DEFAULT NULL,
  `user_type` varchar(55) DEFAULT NULL,
  `password` varchar(55) DEFAULT NULL,
  `salary` varchar(55) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userinfo`
--

INSERT INTO `userinfo` (`emp_id`, `contact`, `name`, `email`, `user_type`, `password`, `salary`) VALUES
(1001, '0000000000', 'Admin', 'admin@gmail.com', 'Admin', 'admin', 'NA'),
(2001, '9067467472', 'Ritesh', 'ritesh@gmail.com', 'Emplyee', 'ritesh', '20000'),
(2002, '9067467472', 'omkar', 'omkar@gmail.com', 'Emplyee', 'omkar', '20000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`pro_id`);

--
-- Indexes for table `report`
--
ALTER TABLE `report`
  ADD PRIMARY KEY (`bill_no`);

--
-- Indexes for table `supplier`
--
ALTER TABLE `supplier`
  ADD PRIMARY KEY (`invoice`);

--
-- Indexes for table `userinfo`
--
ALTER TABLE `userinfo`
  ADD PRIMARY KEY (`emp_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `pro_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
