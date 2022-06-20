import flask
import Config.reader as reader
import json
import Delivery.handler as handler

if __name__ == "__main__":
    # Get config
    server_config = reader.Reader()
    config = server_config.get_config()


    # Identify server name
    app = flask.Flask(config["SERVER"]["NAME"])

    # DEBUG flag
    # app.config["DEBUG"] = True

    app = handler.Handler().setup(app)

    # Start server with host and port
    app.run(host=config["SERVER"]["HOST"], port=config["SERVER"]["PORT"])