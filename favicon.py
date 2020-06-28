##this script is used to get the hash funtction from the favicon.ico of diffrent websites
##to search it from shodan.io.

import mmh3

import requests
 
response = requests.get('https://www.washington.edu/favicon.ico')

favicon = response.content.encode('base64')

hash = mmh3.hash(favicon)

print (hash)