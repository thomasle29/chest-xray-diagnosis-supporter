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
        
    def __str__(self):
        return f"""
            <MedicalRecord 
            patient_name:{self.patient_name},
            patient_age:{self.patient_age},
            patient_sex:{self.patient_sex},
            patient_job:{self.patient_job},
            patient_address:{self.patient_address},
            doctor_id:{self.doctor_id},
            patient_symptoms:{self.patient_symptoms},
            doctor_advice:{self.doctor_advice},
            xray_image:{self.xray_image}
            >
            """