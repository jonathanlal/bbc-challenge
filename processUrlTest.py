import sys
import requests # pip install requests
import json

def processUrl(url):
    data = {}
    data['Url'] = url
    try:
        r = requests.get(url, stream=True, timeout=3) #3 second timeout
        data['Status_code'] = r.status_code
        data['Date'] = r.headers['Date']
        if 'Content-Length' in r.headers:
            data['Content_length'] = r.headers['Content-Length']
        else:
            data['Content_length'] = len(r.raw.read())
    except Exception as e:
        data['Error'] = str(e)
    print(json.dumps(data, indent=4, sort_keys=True))


processUrl("https://stackoverflow.com")
