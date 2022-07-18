class MedicalRecord(object):
    def __init__(
        self,
        patient_name, 
        patient_age,
        patient_sex,
        patient_job,
        patient_address,
        doctor_id,
        patient_symptoms,
        doctor_advice,
        xray_image
        ):
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.patient_sex = patient_sex
        self.patient_job = patient_job
        self.patient_address = patient_address
        self.doctor_id = doctor_id
        self.patient_symptoms = patient_symptoms
        self.doctor_advice = doctor_advice
        self.xray_image = xray_image
        
