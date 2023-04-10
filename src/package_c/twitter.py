import requests


def request_twitter():
    resp = requests.get("https://twitter.com")
    return resp.status_code
