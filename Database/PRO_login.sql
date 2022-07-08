USE hopital_db;
DROP PROCEDURE IF EXISTS pro_login;
DELIMITER $$
CREATE PROCEDURE pro_login(IN param_user VARCHAR(20),IN param_pass CHAR(255))
BEGIN
   select `doctor_id` from `doctor`
   WHERE `doctor_user_name` LIKE param_user and `doctor_pasword` LIKE param_pass;
END; $$
DELIMITER ;