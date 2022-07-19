import flask
import Config.reader as reader
import json
import Delivery.handler as handler
from flask_cors import CORS, cross_origin

if __name__ == "__main__":
    # Get config
    server_config = reader.Reader()
    config = server_config.get_config_sever()


    # Identify server name
    app = flask.Flask(config["SERVER"]["NAME"])
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # DEBUG flag
    # app.config["DEBUG"] = True

    app = handler.Handler().setup(app)

    # Start server with host and port
    app.run(host=config["SERVER"]["HOST"], port=config["SERVER"]["PORT"], debug=False, threaded=False)