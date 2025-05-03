import requests
import re

def get_tokens():
    session = requests.Session()
    url = "https://www.facebook.com/reg"
    response = session.get(url)
    html = response.text

    privacy_mutation_token = ""
    __dyn = ""
    __a = ""

    pm_token_match = re.search(r'privacy_mutation_token=([a-zA-Z0-9%_=\-]+)', html)
    if pm_token_match:
        privacy_mutation_token = pm_token_match.group(1)

    dyn_match = re.search(r'"__dyn":\s*"([^"]+)"', html)
    if not dyn_match:
        dyn_match = re.search(r'__dyn=([a-zA-Z0-9\-]+)', html)
    if dyn_match:
        __dyn = dyn_match.group(1)

    a_match = re.search(r'"__a":\s*"([^"]+)"', html)
    if not a_match:
        a_match = re.search(r'__a=([A-Za-z0-9\-_\.]+)', html)
    if a_match:
        __a = a_match.group(1)

    return {
        "privacy_mutation_token": privacy_mutation_token,
        "__dyn": __dyn,
        "__a": __a
    }
