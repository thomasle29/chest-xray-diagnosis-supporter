class Prediction(object):
    def __init__(
        self, 
        disease_name, 
        base64_image_diagnosis,
        predictions
        ):
        self.disease_name = disease_name
        self.base64_image_diagnosis = base64_image_diagnosis
        self.predictions = predictions