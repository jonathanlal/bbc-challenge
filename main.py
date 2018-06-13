import sys
import requests # pip install requests
import json
import asciiArt

from collections import defaultdict

#after typing in all the urls, user can type 'done' to start processing the urls
list = []
def proccessInput():
    asciiArt.makeArt('BBC Challenge','yellow','on_red','doom','Seperate each URL by a new line.\nType \'done\' on a new line when you are done!\n')
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
        r = requests.get(url, stream=True)
        data['Status_code'] = r.status_code
        data['Date'] = r.headers['Date']
        if 'Content-Length' in r.headers:
            data['Content_length'] = r.headers['Content-Length']
        else:
            data['Content_length'] = len(r.raw.read())
    except Exception as e:
        data['Error'] = str(e)
    print(json.dumps(data, indent=4, sort_keys=True))
    list.append(data)


#for each unique status code in list, create a dictionary (of 'status_code' and 'Number_of_responses') and add it to a new list, else increment dictionary value for key 'Number_of_responses'
def additionalRequirement():
    asciiArt.makeArt(None,'red','on_grey','doom','Additional Requirement\n')
    #print(list)
    list2 = []
    #for each list in dictionary...
    for i in range(0,len(list)):
        #for each item in list
        for k,v in list[i].items():
            #if list key value is Status_code
            if k == 'Status_code':
                data2 = {}

                if len(list2)>0:
                    #check if v exists in list2
                    for x in range(0,len(list2)):
                        for k2,v2 in list2[x].items():
                            if k2 == 'Status_code':
                                if v == v2:
                                    list2[x]['Number_of_responses'] += 1
                else:
                    data2['Status_code'] = v
                    data2['Number_of_responses'] = 1
                    list2.append(data2)

    print(list2)





proccessInput()
additionalRequirement()


# need to do this stuff below if running in command prompt
#"'charmap' codec can't encode character '\\u2013' in position 110906: character maps to <undefined>"
# chcp 65001
# set PYTHONIOENCODING=utf-8
