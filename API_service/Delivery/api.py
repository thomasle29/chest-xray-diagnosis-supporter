from MySQL import connect_MySql
import Application.app as app
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
            return "responding"
        except:
            return "ping function have error"

    def login(self):
        arg = list([flask.request.args.get('user_pass'),flask.request.args.get('user_name')])
        sql = connect_MySql.MySQL
        ID = sql.call_procedure('pro_login', arg)
        return str(ID[0][0])
    

    def new_patient():
        pass
