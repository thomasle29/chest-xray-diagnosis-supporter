from Infrastructure import db_util, request_util
import json
import ast
from . import entity
import sys

class App:
    '''
    App class
    Manufacturing application function of this service
    '''
    def __init__(self) -> None:
        self.db = db_util.DBUtil()
        self.request = request_util.RequestUtil()

    def chestAnalysis(self, medical_record):
        print('Run application.App.chestAnalysis', file=sys.stderr)
        print(medical_record, file=sys.stderr)
        # Diagnosis image
        image_diagnosis = self.request.get_diagnosis(medical_record.xray_image)
        image_diagnosis_dict = ast.literal_eval(image_diagnosis)
        # print(len(image_diagnosis_dict))

        # Database update
        self.db.medical_record_analysis(medical_record, image_diagnosis_dict)

        pass