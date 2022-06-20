class Handler:
    '''
    Handler class
    Setup and install api function to the router
    '''

    # Import api functional
    import Delivery.api as  api

    def setup(self, router):
        '''
        This function setup a list of function for api
        Parameter:
            router: the host router
        Return:
            the host router have include api functional
        '''

        router.add_url_rule('/ping', 'ping', self.api.API().ping,  methods=['GET'])
    
        return router