# --------------------------- XML -------------------------------------

# Ex 1 - XML find()
import xml.etree.ElementTree as ET
data = '''
    <person>
        <name>Chuck</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>'''

# if XML is bad / improper, this can raise an exception. 
# fromstring() converts the string representation of the XML into a “tree” of XML elements
tree = ET.fromstring(data)  
# find() searches through the XML tree and retrieves the element that matches the specified tag.
print('Name:', tree.find('name').text)  # text is the text attr node = Chuck
print('Attr:', tree.find('email').get('hide'))  # hide is hide attr node = yes
# Name: Chuck
# Attr: yes


# Ex 2 - XML findall()
import xml.etree.ElementTree as ET
data = '''
    <stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Chuck</name>
            </user>
            <user x="7">
                <id>009</id>
                <name>Brent</name>
            </user>
        </users>
    </stuff>'''

stuff = ET.fromstring(data)     #make a tree out of XML data
# find all user tags below users, return all user tags in a list
# i.e. lst is a list of tags
# findall() returns a list of subtrees that represent the user structures in the XML tree
# include all parent level elements in the findall() statement except for the top level element (i.e. users/user). Otherwise Python will not find any desired node.
lst = stuff.findall('users/user')  
print('User count:', len(lst))  #len(lst)==2
for user in lst:
    print('Name', user.find('name').text)   #Chuck
    print('Id', user.find('id').text)       #001
    print('Attribute', user.get("x"))       #2
# User count: 2
# Name Chuck
# Id 001
# Attribute 2
# Name Brent
# Id 009
# Attribute 7


# Ex 3 - urlopen => read() => ET.fromstring() => findall()
# template code https://www.py4e.com/code3/geoxml.py?PHPSESSID=1a1214fe8b59b5204f325c9fcf9014a5

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def xml_extract(address):
    uh = urllib.request.urlopen(address, context=ctx)
    
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    # print(data.decode())
    
    tree = ET.fromstring(data)
    results = tree.findall('comments/comment')
    print('Comment count:', len(results)) 
    
    num_lst = []
    for comment in results:
        num_lst.append(int(comment.find('count').text))
    print(num_lst)
    
    total = sum(num_lst)
    print(total)
    
address1 = 'http://py4e-data.dr-chuck.net/comments_42.xml'
address2 = 'http://py4e-data.dr-chuck.net/comments_1629783.xml'

xml_extract(address2)


# ------------------------ JSON -------------------------------------------
# With json structure, you don't have to make a tree b/c the return data for json.load() is a native Python structure, a list of dictionaries


# Tutorial: https://www.youtube.com/watch?v=9N6a-VLBa2I

# load() vs loads() https://stackoverflow.com/questions/39719689/what-is-the-difference-between-json-load-and-json-loads-functions
# load() can accept a file object
# loads() the file object must have undergone read() - s stands for string

# Ex:
with open("json_data.json", "r") as content:
    print(json.load(content))

with open("json_data.json", "r") as content:
  print(json.loads(content.read()))



# Ex 1 
import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

# json.loads() returns a list of dict which we can traverse with a for loop
info = json.loads(data)
# print(info)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])


# Ex 2 - API simulation, concate url, json.load(), analyse   

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ') # enter Ann Arbor, MI
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    # concatnate serviceurl w/ parms
    # Unlike a fixed web page, the data we get depends on the parameters we send and the geographical data stored in Google’s servers.
    url = serviceurl + urllib.parse.urlencode(parms)    

    print('Retrieving', url)
# Retrieving http://py4e-data.dr-chuck.net/json?address=Ann+Arbor%2C+MI&key=42
# + is space; %2C is comma, key is the API key 42
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    # check if data is good
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # pretty print json data
    print(json.dumps(js, indent=2))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    