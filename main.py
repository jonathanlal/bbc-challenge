import sys
import requests # pip install requests
import json
import asciiArt


#after typing in all the urls, user can type 'done' to start processing the urls
def proccessInput():
    buffer = []
    while True:
        line = sys.stdin.readline().rstrip('\n')
        if line == 'done':
            for x in buffer:
                proccessUrl(x)
            break
        else:
            buffer.append(line)


#take in a url and stdout the results
def proccessUrl(url):
    data = {}
    data['Url'] = url
    try:
        r = requests.get(url)
        data['Status_code'] = r.status_code
        data['Content_length'] = r.headers['Content-Length']
        data['Date'] = r.headers['Date']
    except Exception as e:
        data['Error'] = str(e)
    print(json.dumps(data, indent=4, sort_keys=True))
    #asciiArt.makeArt('Some Finish Message','blue','on_cyan','doom',None)

asciiArt.makeArt('BBC Challenge','yellow','on_red','doom','Seperate each URL by a new line.\nType \'done\' on a new line when you are done!\n')
proccessInput()
