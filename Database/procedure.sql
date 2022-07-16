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
	IN param_medical_record_image TEXT
)

BEGIN

	DECLARE new_patient_id CHAR(36);
	SET new_patient_id = UUID();
   
   
   INSERT INTO `hopital_db`.`patient_record` (`patient_record_id`,`patient_record_name`,`patient_record_DoB`,`patient_record_sex`,`patient_record_job`,`patient_record_address`) 
   VALUES (new_patient_id,param_patient_record_name,param_patient_record_DoB,param_patient_record_sex,param_patient_record_job,param_patient_record_address);

   INSERT INTO `hopital_db`.`medical_record` (`medical_record_id`,`patient_record_id`,`doctor_id`,`medical_record_date`,`medical_record_advice`,`medical_record_symptom`,`medical_record_image`)
   VALUES  (UUID(),new_patient_id,param_doctor_id,CURRENT_DATE(),param_medical_record_advice,param_medical_record_symptom,param_medical_record_image);
   
END; $$
DELIMITER ;



USE hopital_db;
DROP PROCEDURE IF EXISTS pro_diagnosis_report;
DELIMITER $$
CREATE PROCEDURE pro_diagnosis_report(
IN param_medical_record_id CHAR(36),
IN param_disease_id SMALLINT,
IN param_medical_record_disease_image_prediction  TEXT,
IN param_medical_record_prediction DECIMAL(3,2),
IN param_medical_record_disease_doctor_validation BIT
)
BEGIN
	INSERT INTO `hopital_db`.`medical_record_disease` (	`medical_record_id`,`disease_id`,`medical_record_disease_image_prediction`,
														`medical_record_prediction_validation`,`medical_record_disease_doctor_validation`) 
    VALUES (param_medical_record_id,param_disease_id,param_medical_record_disease_image_prediction,
			param_medical_record_prediction,param_medical_record_disease_doctor_validation);
END; $$
DELIMITER ;




USE hopital_db;
DROP PROCEDURE IF EXISTS pr_disease_id;
DELIMITER $$

CREATE PROCEDURE pro_disease_id(
IN param_disease_name NCHAR(20)
)
BEGIN
	SELECT hopital_db.disease_id FROM disease
    WHERE param_disease_name LIKE disease_id;
END; $$
DELIMITER ;