import flask
import Config.reader as reader
import json
import Delivery.handler as handler
from Infrastructure import util


if __name__ == "__main__":
    
    # Get config
    reader = reader.Reader()
    config_sv = reader.get_config_sever()
    
    # Identify server name
    app = flask.Flask(config_sv["SERVER"]["NAME"])

    # DEBUG flag
    # app.config["DEBUG"] = True

    app = handler.Handler().setup(app)

    # Start server with host and port
    app.run(host=config_sv["SERVER"]["HOST"], port=config_sv["SERVER"]["PORT"], debug=False, threaded=False)