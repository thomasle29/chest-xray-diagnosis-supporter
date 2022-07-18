# from aem import Query
import queue
from mysql.connector import connect, Error
from Config.reader import Reader
import uuid

class DBUtil:
    
    def __init__(self) -> None:
        config = Reader().get_config_MySQL()

        try:
            self.mysql =  connect(
                host=config["MYSQL"]["HOST"],
                user=config["MYSQL"]["USER"],
                password=config["MYSQL"]["PASSWORD"],
                database=config["MYSQL"]["DATABASE"]
            )
            self.cursor = self.mysql.cursor()
        except Error as e:
            print(e)

    def medical_record_analysis(self, medical_record, image_diagnosis_dict):
        # patient record 
        patient_record_id = uuid.uuid1()
        parient_record_query = """
            CALL hopital_db.add_patient_record(
                {patient_id},
                {patient_name},
                {patient_age},
                {patient_sex},
                {patient_job},
                {patient_address},
                {patient_symptoms}
            )
            """.format(
                patient_id = patient_record_id,
                patient_name = medical_record.patient_name,
                patient_age = medical_record.patient_age,
                patient_sex = medical_record.patient_sex,
                patient_job = medical_record.patient_job,
                patient_address = medical_record.patient_address,
                patient_symptoms = medical_record.patient_symptoms
            )
        self.cursor.execute(parient_record_query)

        # medical record
        medical_record_id = uuid.uuid1()
        medical_record_query = ""

        pass