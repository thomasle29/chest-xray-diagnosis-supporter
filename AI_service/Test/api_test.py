import requests
import os
import json

def chest_diagnosis():
    URL = "http://127.0.0.1:8020/chest/diagnosis"
    image_base64_url = "base64_image.txt"
    
    with open(image_base64_url, "r") as f:
        base64_image = f.readline()

    # print(base64_image)

    data = {
        "base64_image": base64_image
    }

    json_string = json.dumps(data)

    # print(json_string)

    response = requests.post(URL, data=json_string)
    print(response.text)
    # y = response.json()
    # print(y)

def main():
    chest_diagnosis()


if __name__ == "__main__":
    main()