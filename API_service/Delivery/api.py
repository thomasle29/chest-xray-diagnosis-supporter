from MySQL import connect_MySql
import Application.app as app
import flask
import json

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
            return "responding"
        except:
            return "ping function have error"

    def login(self):
        contents = json.loads(flask.request.data)
        ID = self.app.pro_login(contents)
        return str(ID)
        
    def new_medical_record(self):
        contents = json.loads(flask.request.data)
        result = self.app.pro_new_medical_record(contents)
        return result
    

    def diagnosis_report(self):
        contents = json.loads(flask.request.data)
        result = self.app.pro_diagnosis_report(contents)
        return result
