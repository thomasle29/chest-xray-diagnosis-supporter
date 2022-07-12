import flask
import Config.reader as reader
import json
import Delivery.handler as handler
from MySQL import connect_MySql

if __name__ == "__main__":

    # Get config
    server_config = reader.Reader()
    config_sv = server_config.get_config_sever()

    MySQL_config = reader.Reader()
    config_MySQL = MySQL_config.get_config_MySQL()
    
    # connect to database
    connect_MySql.MySQL.MySQL_CONFIG(   host = config_MySQL['MYSQL']['HOST'], 
                                        user = config_MySQL['MYSQL']['USER'], 
                                        password = config_MySQL['MYSQL']['PASSWORD'], 
                                        database = config_MySQL['MYSQL']['DATABASE'])
                                        
    # Identify server name
    app = flask.Flask(config_sv["SERVER"]["NAME"])

    # DEBUG flag
    # app.config["DEBUG"] = True

    app = handler.Handler().setup(app)

    # Start server with host and port
    app.run(host=config_sv["SERVER"]["HOST"], port=config_sv["SERVER"]["PORT"], debug=False, threaded=False)