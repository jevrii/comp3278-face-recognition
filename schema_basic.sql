-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 17, 2020 at 09:41 PM
-- Server version: 5.7.28-0ubuntu0.18.04.4
-- PHP Version: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `facerecognition`
--

# Create TABLE 'Student'
CREATE TABLE `Student` (
  `student_id` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `login_datetime` datetime NOT NULL,
  `email_address` varchar(100) NOT NULL,
  PRIMARY KEY (student_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Course` (
  `course_name` varchar(50) NOT NULL,
  `course_code` varchar(50) NOT NULL,
  PRIMARY KEY (course_code)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Lesson` (
  `course_code` varchar(50) NOT NULL,
  `start_datetime` datetime NOT NULL,
  `end_datetime` datetime NOT NULL,
  `zoom_link` varchar(100) NOT NULL,
  `venue` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `teacher` varchar(50) NOT NULL,
  PRIMARY KEY (course_code)
  -- FOREIGN KEY (course_code) REFERENCES Course (course_code)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `CourseMaterial` (
  `material_id` varchar(100) NOT NULL,
  `course_code` varchar(50) NOT NULL,
  `material_name` varchar(50) NOT NULL,
  `material_link` varchar(100) NOT NULL,
  PRIMARY KEY (material_id,course_code)
  -- FOREIGN KEY (course_code) REFERENCES Course (course_code)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Enroll` (
  `course_code` varchar(50) NOT NULL,
  `student_id` varchar(50) NOT NULL,
  PRIMARY KEY (course_code,student_id)
	-- FOREIGN KEY (course_code) REFERENCES Course (course_code),
	-- FOREIGN KEY (student_id) REFERENCES Student (student_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
