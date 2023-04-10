import requests
from package_c import twitter


def request_google():
    resp = requests.get("https://google.com")
    return resp.status_code

def google_plus_twitter():
    return twitter.request_twitter() + request_google()