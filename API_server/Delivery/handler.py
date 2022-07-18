from crypt import methods
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
        router.add_url_rule('/chest/analysis', 'analysis', self.api.analysis, methods=['POST'])

        return router