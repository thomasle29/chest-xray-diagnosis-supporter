import Application.app as app
import json
import flask

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

    def chestDiagnosis(self):
        
        # Convert json data to distionary
        contents = json.loads(flask.request.data)

        result = self.app.chestDiagnosis(contents['base64_image'])
        # print(result)
        json_results = json.dumps(str(result))
        try:
            return json_results
        except:
            return "chestDiagnosis function have error"