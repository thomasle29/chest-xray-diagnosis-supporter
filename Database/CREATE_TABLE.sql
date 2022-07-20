DROP DATABASE IF EXISTS hopital_db;
CREATE DATABASE hopital_db; 

CREATE TABLE `hopital_db`.`doctor` (
  `doctor_id` SMALLINT NOT NULL AUTO_INCREMENT,
  `doctor_user_name` VARCHAR(20) NOT NULL,
  `doctor_pasword` CHAR(255) NOT NULL,
  `doctor_name` NVARCHAR(30) NOT NULL,
  `doctor_DoB` DATE NULL,
  `doctor_sex` TINYINT NULL,
  PRIMARY KEY (`doctor_id`));
  
  
CREATE TABLE `hopital_db`.`patient_record` (
	`patient_record_id` CHAR(36) NOT NULL,
    `patient_record_name` NVARCHAR(20) NOT NULL,
	`patient_record_dob` date NOT NULL,
	`patient_record_sex` TINYINT NULL,
	`patient_record_job` NVARCHAR(20) NULL,
	`patient_record_address` NVARCHAR(100) NULL,
	PRIMARY KEY (`patient_record_id`));


CREATE TABLE `hopital_db`.`medical_record` (
	`medical_record_id` CHAR(36) NOT NULL,
    `patient_record_id` CHAR(36) NOT NULL,
    `doctor_id` SMALLINT NOT NULL,
    `medical_record_date` DATE NOT NULL,
	`medical_record_advice` NVARCHAR(100) NULL,
	`medical_record_symptom` NVARCHAR(100) NULL,
	`medical_record_image` LONGTEXT NULL,
	`medical_record_prediction_num` TINYINT NULL,
	`medical_record_doctor_comment` NVARCHAR(25) NULL,
    `medical_record_disease_prediction_by_doctor` NVARCHAR(25) NULL,
	PRIMARY KEY (`medical_record_id`),
    FOREIGN KEY (`doctor_id`) REFERENCES `doctor`(`doctor_id`),
	FOREIGN KEY (`patient_record_id`) REFERENCES `patient_record`(`patient_record_id`));

CREATE TABLE `hopital_db`.`disease` (
	`disease_id` TINYINT NOT NULL AUTO_INCREMENT,
	`disease_name` NCHAR(20) NOT NULL,
	`disease_dangerouse_level` TINYINT,
	PRIMARY KEY (`disease_id`));

CREATE TABLE `hopital_db`.`medical_record_disease` (
	`medical_record_id` CHAR(36) NOT NULL,
	`disease_id` TINYINT NOT NULL,
	`medical_record_disease_image_prediction` LONGTEXT NULL,
	`medical_record_prediction` DECIMAL(3,2) NOT NULL,
	`medical_record_disease_doctor_validation` BIT NULL,
    PRIMARY KEY(`disease_id`,`medical_record_id`),
	FOREIGN KEY(`disease_id`) REFERENCES `disease`(`disease_id`),
	FOREIGN KEY(`medical_record_id`) REFERENCES `medical_record`(`medical_record_id`)
);
  
  
