import sys
import requests # pip install requests
import json
import asciiArt

def processInput():
    buffer = []
    while True:
        line = sys.stdin.readline().rstrip('\n')
        if line == 'done':
            print("Your text is: ")
            for x in buffer:
                print(x) #processUrl(x)
            break
        else:
            buffer.append(line)

print("Enter some urls then enter 'done' when you are finished")
processInput()
