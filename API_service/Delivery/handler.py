# Import api functional

import Delivery.api as  api

class Handler:
    '''
    Handler class
    Setup and install api function to the router
    '''

    def __init__(self):
        self.api = api.API()

    def setup(self, router):
        '''
        This function setup a list of function for api
        Parameter:
            router: the host router
        Return:
            the host router have include api functional
        '''


        router.add_url_rule('/ping', 'ping', self.api.ping,  methods=['GET'])
        router.add_url_rule('/api_service/login', 'login', self.api.login, methods=['POST'])
        router.add_url_rule('/api_service/submit', 'submit', self.api.new_medical_record, methods=['POST'])
        router.add_url_rule('/api_service/report', 'report', self.api.diagnosis_report, methods=['POST'])
        return router