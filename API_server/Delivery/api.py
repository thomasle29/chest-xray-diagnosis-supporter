import Application.app as app
import json
import flask
from . import entity 
import sys

class API:
    '''
    API class:
    Manufacturing api function
    '''
    def __init__(self) -> None:
        self.app = app.App()

    def ping(self):
        '''
        This function will check that if this service is good runnable
        '''

        try:
            return "pong"
        except:
            return "ping function have error"

    def analysis(self):

        # Convert json data to distionary
        print('Run delevery.API.analysis', file=sys.stderr)
        contents = json.loads(flask.request.data)
        medical_record = entity.MedicalRecord(**contents)

        result = self.app.chestAnalysis(medical_record)

        json_results = json.dumps(str(result))
        try:
            return json_results
        except:
            return "chestDiagnosis function have error"
