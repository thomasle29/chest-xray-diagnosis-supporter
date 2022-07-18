import requests
import json
from Config.reader import Reader

class RequestUtil:

    def __init__(self) -> None:
        self.AI_server_config = Reader().get_config_AI_server()

    def get_diagnosis(self, base64_image):
        data = {
            "base64_image": base64_image
        }
        
        json_string = json.dumps(data)

        response = requests.post(
            self.AI_server_config["SERVER"]["URL"] + "diagnosis", 
            data=json_string
            )
        
        return response.text