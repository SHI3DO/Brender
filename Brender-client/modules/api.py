import requests

API_URL = "http://asphodel.kro.kr:8585/api/"
VERSION = "v1"


def call_api(method, endpoint, data=None, params=None) -> requests.Response:
    return requests.request(
        method=method, url=API_URL + VERSION + "/" + endpoint, data=data, params=params
    )


def test_api():
    testing = call_api("GET", "test")
    if testing.status_code == 200:
        print("Brender API is working.")
    else:
        print("Brender API is not working.")


test_api()
