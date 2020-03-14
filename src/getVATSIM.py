import requests
import json


def getvatsim():
    print("Enter key-word for partial search of remarks: ")
    searchword = input()
    url = "https://glacial-inlet-67016.herokuapp.com/vatsim/pilots/" + searchword

    r = requests.get(url)

    if r.ok:
        jdata = json.loads(r.text)
        return jdata

    else:
        resp = r.raise_for_status()
        print(resp)
