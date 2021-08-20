import urequests as requests

import ujson as json

class FirebaseException(Exception):
    pass


def put(URL, msg):
    to_post = json.dumps(msg)
    response = requests.put(URL, data=to_post)
    if response.status_code != 200:
        raise FirebaseException(response.text)


def patch(URL, msg):
    to_post = json.dumps(msg)
    response = requests.patch(URL, data=to_post)
    if response.status_code != 200:
        raise FirebaseException(response.text)


def get(URL):
    response = requests.get(URL)
    if response.status_code != 200:
        raise FirebaseException(response.text)
    return json.loads(response.text)


def push(URL, msg):
    to_post = json.dumps(msg)
    response = requests.post(URL, data=to_post)
    if response.status_code != 200:
        raise Exception(response.text)