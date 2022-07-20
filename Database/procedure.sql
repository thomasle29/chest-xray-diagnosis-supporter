USE hopital_db;
DROP PROCEDURE IF EXISTS pro_login;
DELIMITER $$
CREATE PROCEDURE pro_login(IN param_user VARCHAR(20),IN param_pass CHAR(255))
BEGIN
   select `doctor_id`,`doctor_name` from `doctor`
   WHERE `doctor_user_name` LIKE param_user and `doctor_pasword` LIKE param_pass;
END; $$
DELIMITER ;


/* this procedure use to submit a new patient */

USE hopital_db;
DROP PROCEDURE IF EXISTS pro_new_medical_record;
DELIMITER $$
CREATE PROCEDURE pro_new_medical_record(
	IN param_patient_record_name nvarchar(20),
	IN param_patient_record_DoB date,
	IN param_patient_record_sex tinyint,
	IN param_patient_record_job varchar(20),
	in param_patient_record_address varchar(100),

	IN param_doctor_id SMALLINT,
    IN param_medical_record_symptom NVARCHAR(100),
	IN param_medical_record_advice NVARCHAR(100),
	IN param_medical_record_image LONGTEXT
)

BEGIN

	DECLARE new_patient_id CHAR(36);
    declare new_medical_id CHAR(36);
    
	SET new_patient_id = UUID();
    SET new_medical_id = UUID();
   
   INSERT INTO `hopital_db`.`patient_record` (`patient_record_id`,`patient_record_name`,`patient_record_DoB`,`patient_record_sex`,`patient_record_job`,`patient_record_address`) 
   VALUES (new_patient_id,param_patient_record_name,param_patient_record_DoB,param_patient_record_sex,param_patient_record_job,param_patient_record_address);

   INSERT INTO `hopital_db`.`medical_record` (`medical_record_id`,`patient_record_id`,`doctor_id`,`medical_record_date`,`medical_record_advice`,`medical_record_symptom`,`medical_record_image`)
   VALUES  (new_medical_id,new_patient_id,param_doctor_id,CURRENT_DATE(),param_medical_record_advice,param_medical_record_symptom,param_medical_record_image);
   select new_medical_id;
   
END; $$
DELIMITER ;



USE hopital_db;
DROP PROCEDURE IF EXISTS pro_diagnosis_report;
DELIMITER $$
CREATE PROCEDURE pro_diagnosis_report(
IN param_medical_record_id CHAR(36),
IN param_disease_id SMALLINT,
IN param_medical_record_disease_image_prediction  LONGTEXT,
IN param_medical_record_prediction DECIMAL(3,2),
IN param_medical_record_disease_doctor_validation BIT
)
BEGIN
	INSERT INTO `hopital_db`.`medical_record_disease` (	`medical_record_id`,`disease_id`,`medical_record_disease_image_prediction`,
														`medical_record_prediction`,`medical_record_disease_doctor_validation`) 
    VALUES (param_medical_record_id,param_disease_id,param_medical_record_disease_image_prediction,
			param_medical_record_prediction,param_medical_record_disease_doctor_validation);
END; $$
DELIMITER ;




USE hopital_db;
DROP PROCEDURE IF EXISTS pro_disease_id;
DELIMITER $$

CREATE PROCEDURE pro_disease_id(
IN param_disease_name NCHAR(20)
)
BEGIN
	SELECT `disease_id` FROM `hopital_db`.`disease`
    WHERE param_disease_name = `disease`.`disease_name`;
END; $$
DELIMITER ;


USE hopital_db;
DROP PROCEDURE IF EXISTS pro_report_medical;
DELIMITER $$

CREATE PROCEDURE pro_report_medical(
IN param_id CHAR(36),
IN param_medical_record_doctor_comment NVARCHAR(25),
IN param_medical_record_disease_prediction_by_doctor NVARCHAR(25),
IN param_medical_record_prediction_num TINYINT 
)
BEGIN
	UPDATE `medical_record`
	SET `medical_record_doctor_comment` = param_medical_record_doctor_comment,
		`medical_record_disease_prediction_by_doctor` = param_medical_record_disease_prediction_by_doctor,
        `medical_record_prediction_num` = param_medical_record_prediction_num
    WHERE param_id = `medical_record`.`medical_record_id`;
END; $$
DELIMITER ;






