import requests
from .errors import *


def get(url: str, error=True, data=True):
    """
    Request get the url
    :param url: The URL of the site
    :param error: Check for error message
    :param data: Data of the response
    :return: Response
    """
    response = requests.get(url)

    if error:
        if "errorMessage" in response.json():
            if data:
                raise ErrorMessage(f"Error message is {response.json()['errorMessage']}. Data is {response.text}.")
            else:
                raise ErrorMessage(f"Error message is {response.json()['errorMessage']}.")

    if response.status_code == 200:
        return response
    elif response.status_code == 404:
        if data:
            raise NotFound(f"Got status code {response.status_code} from {url}. Data is {response.text}.")
        else:
            raise NotFound(f"Got status code {response.status_code} from {url}.")
    elif response.status_code == 400:
        if data:
            raise BadRequest(f"Got status code {response.status_code} from {url}. Data is {response.text}.")
        else:
            raise BadRequest(f"Got status code {response.status_code} from {url}.")
    else:
        if data:
            raise BadStatus(f"Got status code {response.status_code} from {url}. Data is {response.text}.")
        else:
            raise BadStatus(f"Got status code {response.status_code} from {url}.")
