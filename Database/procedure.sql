DELIMITER //

DROP PROCEDURE IF EXISTS hopital_db.login //
CREATE PROCEDURE hopital_db.login(
   IN param_user VARCHAR(20),
   IN param_pass CHAR(255)
)
BEGIN
   SELECT d.`doctor_id`, d.`doctor_name`
   FROM hopital_db.`doctor` AS d
   WHERE `doctor_user_name` LIKE param_user 
   AND `doctor_pasword` LIKE param_pass;
END; //

DROP PROCEDURE IF EXISTS hopital_db.add_patient_record //
CREATE PROCEDURE hopital_db.add_patient_record(
   IN param_patient_id CHAR(36),
   IN param_patient_name NVARCHAR(20),
   IN param_patient_age TINYINT,
   IN param_patient_sex TINYINT,
   IN param_patient_job NVARCHAR(20),
   IN param_patient_address NVARCHAR(100)
)
BEGIN
   INSERT INTO hopital_db.patient_record(
      patient_record_id,
      patient_record_name,
      patient_record_age,
      patient_record_sex,
      patient_record_job,
      patient_record_address,
      )
   VALUES (
      param_patient_id,
      param_patient_name,
      param_patient_age,
      param_patient_sex,
      param_patient_job,
      param_patient_address
   )
END //

DROP PROCEDURE IF EXISTS hopital_db.add_medical_record //
CREATE PROCEDURE hopital_db.add_medical_record(
   IN param_medical_record_id CHAR(36),
   IN param_patient_id CHAR(36),
   IN param_doctor_id SMALLINT,
   IN param_medical_record_advice NVARCHAR(100),
   IN param_medical_record_symptom NVARCHAR(100),
   IN param_medical_record_image BLOB
)
BEGIN
   INSERT INTO hopital_db.medical_record(
      medical_record_id,
      patient_record_id,
      doctor_id,
      medical_record_date,
      medical_record_advice,
      medical_record_symptom,
      medical_record_image
      )
   VALUES (
      param_medical_record_id,
      param_patient_id,
      param_doctor_id,
      CURDATE(),
      param_medical_record_advice,
      param_medical_record_symptom,
      param_medical_record_image
   )
END //