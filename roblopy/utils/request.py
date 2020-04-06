import requests
from .errors import *

def get(url: str):
    response = requests.get(url)

    if "errorMessage" in response.json():
        raise ErrorMessage(f"Error message is {response.json()['errorMessage']}. Data is {response.text}.")

    if response.status_code == 200:
        return response
    elif response.status_code == 404:
        raise NotFound(f"Got status code {response.status_code} from {url}. Data is {response.text}.")
    elif response.status_code == 400:
        raise BadRequest(f"Got status code {response.status_code} from {url}. Data is {response.text}.")
    else:
        raise BadStatus(f"Got status code {response.status_code} from {url}. Data is {response.text}.")

def no_json_get(url: str):
    response = requests.get(url)

    if response.status_code == 200:
        return response
    elif response.status_code == 404:
        raise NotFound(f"Got status code {response.status_code} from {url}. Data is {response.text}.")
    elif response.status_code == 400:
        raise BadRequest(f"Got status code {response.status_code} from {url}. Data is {response.text}.")
    else:
        raise BadStatus(f"Got status code {response.status_code} from {url}. Data is {response.text}.")

def no_data_get(url: str):
    response = requests.get(url)

    if response.status_code == 200:
        return response
    elif response.status_code == 404:
        raise NotFound(f"Got status code {response.status_code} from {url}.")
    elif response.status_code == 400:
        raise BadRequest(f"Got status code {response.status_code} from {url}.")
    else:
        raise BadStatus(f"Got status code {response.status_code} from {url}.")
                           
