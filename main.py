import sys
import requests # pip install requests
import json


#after typing in all the urls via stdin, user can type 'done' to start processing the urls
list = [] #needs to be global so we can add each dictionary to the list and access it in the additionalRequirement
def processInput():
    print("\n<---------------BBC Challenge--------------->\n")
    print("Seperate each URL by a new line.\nType \'done\' on a new line when you are done!\n")
    buffer = []
    while True:
        line = sys.stdin.readline().rstrip('\n')
        if line == 'done':
            for x in buffer:
                processUrl(x)
            break
        else:
            buffer.append(line)



#take in a url and stdout the results
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
    list.append(data) # add result to list we declared globally so we can use the results in additionalRequirement()


#for each unique status code in list, create a dictionary (of 'status_code' and 'Number_of_responses') and add it to a new list, else increment dictionary value for key 'Number_of_responses'
def additionalRequirement():
    print("<----Additional Requirement---->")
    list2 = []
    #for each dictionary in list
    for i in range(0,len(list)):
        #get key value pair in dictionary
        for k,v in list[i].items():
            #if dictionary key is Status_code
            if k == 'Status_code':
                #if size of our second list is not greater than 0 (add first "object" to "array")
                if len(list2)>0:
                    #if status code value exists in list2
                    if any(list['Status_code'] == v for list in list2):
                        #for each dictionary in list
                        for x in range(0,len(list2)):
                            #get key value pair of dictionary
                            for k2,v2 in list2[x].items():
                                #if key value is status_code and value of dictionary in list 1 is equal to value of dictionary in list 2
                                if k2 == 'Status_code' and v == v2:
                                    #increment number of responses
                                    list2[x]['Number_of_responses'] += 1
                    else:
                        #if status code value does not exist in list2 (add it)
                        data2 = {}
                        data2['Status_code'] = v
                        data2['Number_of_responses'] = 1
                        list2.append(data2)
                else:
                    #if list2 is not greater than 0, add our first record
                    data2 = {}
                    data2['Status_code'] = v
                    data2['Number_of_responses'] = 1
                    list2.append(data2)

    #print(list2)
    print(json.dumps(list2, indent=4, sort_keys=True))




processInput()
additionalRequirement()


# need to do this stuff below if running in command prompt on windows and you get the following error
#ERROR: "'charmap' codec can't encode character '\\u2013' in position 110906: character maps to <undefined>"
# chcp 65001
# set PYTHONIOENCODING=utf-8
