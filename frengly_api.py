import urllib
import requests
import requests.exceptions
import json

frengly_base_url = "http://www.syslang.com"

f = open("frengly_credentials")
str_lines = f.read().splitlines()

frengly_user = str_lines[0]
frengly_pass = str_lines[1]

def translate(mText, mFrom, mTo):
    translateUrl = frengly_base_url + \
                   "?src=" + urllib.quote(mFrom) + \
                   "&dest=" + urllib.quote(mTo) + \
                   "&text=" + urllib.quote(mText) + \
                   "&email=" + urllib.quote(frengly_user) + \
                   "&password=" + urllib.quote(frengly_pass) + \
                   "&outformat=" + urllib.quote("json")

    try:
        r = requests.get(translateUrl)
    except requests.exceptions.RequestException, e:
        return e.message

    try:
        json_data = json.loads(r.text)
    except ValueError:
        return "Json error parsing"

    return json_data["translation"]