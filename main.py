import sys
import httplib2 # pip install httplib2

#consume input from stdin
userInput = input("Enter a url: ")
contents = httplib2.Http(".cache")
(resp_headers, content) = contents.request(userInput, "GET")


#output stdout
print(contents);
