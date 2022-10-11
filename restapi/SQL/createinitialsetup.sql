-- MySQL Script generated by MySQL Workbench
-- Sun Oct 31 23:07:04 2021
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema hrm_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hrm_db` DEFAULT CHARACTER SET utf8mb4 ;
USE `hrm_db` ;

-- -----------------------------------------------------
-- Table `hrm_db`.`Colleagues`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hrm_db`.`Colleagues` (
  `User_id` INT NOT NULL AUTO_INCREMENT,
  `First_name` VARCHAR(50) NULL,
  `Last_name` VARCHAR(100) NULL,
  `Email` VARCHAR(255) NOT NULL,
  `Dob` DATETIME NOT NULL,
  `DOJ` DATETIME NOT NULL,
  `Contact_no` NVARCHAR(255) NOT NULL,
  `Password` NVARCHAR(255) NOT NULL,
  `Photo_url` NVARCHAR(255) NULL,
  PRIMARY KEY (`User_id`, `Email`),
  UNIQUE INDEX `Email_UNIQUE` (`Email` ASC),
  UNIQUE INDEX `Contact_no_UNIQUE` (`Contact_no` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hrm_db`.`Marital_status`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hrm_db`.`Marital_status` (
  `M_id` INT NOT NULL AUTO_INCREMENT,
  `M_name` VARCHAR(50) NULL,
  PRIMARY KEY (`M_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hrm_db`.`Gender`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hrm_db`.`Gender` (
  `Gender_id` INT NOT NULL AUTO_INCREMENT,
  `Gender_name` VARCHAR(50) NULL,
  PRIMARY KEY (`Gender_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hrm_db`.`Department`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hrm_db`.`Department` (
  `Dep_id` INT NOT NULL AUTO_INCREMENT,
  `Dep_name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`Dep_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hrm_db`.`Designation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hrm_db`.`Designation` (
  `Des_id` INT NOT NULL AUTO_INCREMENT,
  `Des_name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`Des_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hrm_db`.`Address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hrm_db`.`Address` (
  `Add_id` INT NOT NULL AUTO_INCREMENT,
  `Apt_no` VARCHAR(150) NULL,
  `Street` VARCHAR(255) NULL,
  `City` VARCHAR(100) NULL,
  `State` VARCHAR(100) NULL,
  `Pincode` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Add_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hrm_db`.`Timesheet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hrm_db`.`Timesheet` (
  `Time_id` INT NOT NULL AUTO_INCREMENT,
  `Sick_leave` INT NULL,
  `Casual_leave` INT NULL,
  `Annual_leave` INT NULL,
  `Total_leave_consumed` INT NULL,
  `Total_leave_remaining` INT NULL,
  PRIMARY KEY (`Time_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hrm_db`.`Salary`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hrm_db`.`Salary` (
  `Salary_id` INT NOT NULL AUTO_INCREMENT,
  `Basic` INT NULL,
  `allowance` INT NULL,
  `deduction` INT NULL,
  `Netpay` INT NULL,
  `Grosspay` INT NULL,
  PRIMARY KEY (`Salary_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hrm_db`.`Colleagues_mappings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hrm_db`.`Colleagues_mappings` (
  `User_id` INT NOT NULL,
  `Salary_id` INT NOT NULL,
  `Add_id` INT NOT NULL,
  `Time_id` INT NOT NULL,
  `Gender_id` INT NOT NULL,
  `Des_id` INT NOT NULL,
  `M_id` INT NOT NULL,
  `Dep_id` INT NOT NULL,
  `Manager_id` INT NOT NULL,
  INDEX `fk_Colleagues_mappings_Colleagues_idx` (`User_id` ASC),
  INDEX `fk_Colleagues_mappings_Salary1_idx` (`Salary_id` ASC),
  INDEX `fk_Colleagues_mappings_Address1_idx` (`Add_id` ASC),
  INDEX `fk_Colleagues_mappings_Timesheet1_idx` (`Time_id` ASC),
  INDEX `fk_Colleagues_mappings_Gender1_idx` (`Gender_id` ASC),
  INDEX `fk_Colleagues_mappings_Designation1_idx` (`Des_id` ASC),
  INDEX `fk_Colleagues_mappings_Marital_status1_idx` (`M_id` ASC),
  INDEX `fk_Colleagues_mappings_Department1_idx` (`Dep_id` ASC),
  INDEX `fk_Colleagues_mappings_Colleagues1_idx` (`Manager_id` ASC),
  CONSTRAINT `fk_Colleagues_mappings_Colleagues`
    FOREIGN KEY (`User_id`)
    REFERENCES `hrm_db`.`Colleagues` (`User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Salary1`
    FOREIGN KEY (`Salary_id`)
    REFERENCES `hrm_db`.`Salary` (`Salary_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Address1`
    FOREIGN KEY (`Add_id`)
    REFERENCES `hrm_db`.`Address` (`Add_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Timesheet1`
    FOREIGN KEY (`Time_id`)
    REFERENCES `hrm_db`.`Timesheet` (`Time_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Gender1`
    FOREIGN KEY (`Gender_id`)
    REFERENCES `hrm_db`.`Gender` (`Gender_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Designation1`
    FOREIGN KEY (`Des_id`)
    REFERENCES `hrm_db`.`Designation` (`Des_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Marital_status1`
    FOREIGN KEY (`M_id`)
    REFERENCES `hrm_db`.`Marital_status` (`M_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Department1`
    FOREIGN KEY (`Dep_id`)
    REFERENCES `hrm_db`.`Department` (`Dep_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Colleagues_mappings_Colleagues1`
    FOREIGN KEY (`Manager_id`)
    REFERENCES `hrm_db`.`Colleagues` (`User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;