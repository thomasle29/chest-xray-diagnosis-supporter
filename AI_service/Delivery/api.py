class API:
    '''
    API class:
    Manufacturing api function
    '''

    def ping(self):
        '''
        This function will check that if this service is good runnable
        '''

        try:
            return "pong"
        except:
            return "ping function have error"