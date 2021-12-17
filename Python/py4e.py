friends = ['Carlos', 'Sergio', 'Joel']
for bf in friends:
    print('Cena de Navidad: estáis invitados', bf)

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

for letter in 'banana' :
    print(letter)

print("123" + "abc")    
x = 1 + 2 * 3 - 8 / 4
x = int(98.6)

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
n = parts[1]

fruit = ['Banana']
fruit[0] = 'b'
print(fruit)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])

stuff = dict()
print(stuff.get('candy',-1))

if key in counts:
    counts[key] = counts[key] + 1
else:
    counts[key] = 1
    
lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
days[2]


import re
count = 0
hand = open("regex_sum.txt")
lines = hand.read()
match = re.findall('[0-9]+',lines)
for i in match:
	number = int(i)
	count = count + number
print (count)

ca = 193 + 194 +219 +230
ax = 187.45 + 178.79 + 192.44 + 272.74

ax-ca

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

## Networking
# PY4EV
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()

# autograde 1

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

# wordurl
import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
    
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word]= counts.get(word,0)+1
print(counts)

# autograde 2

import urllib.request, urllib.parse, urllib.error
#import re
from bs4 import BeautifulSoup

text = "http://py4e-data.dr-chuck.net/comments_1422368.html"

html = urllib.request.urlopen(text).read()
soup = BeautifulSoup(html)
tags = soup("span")

sum=0
for tag in tags:
    sum = sum+int(tag.contents[0])
print(sum)

# URLLIB
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://vedia-jerezdaniel.github.io/exo/Data%20Science/"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
    
# autograde 3
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "http://py4e-data.dr-chuck.net/known_by_Lucee.html"

#to repeat 7 times#
for i in range(7):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count +1
        #make it stop at position 3#
        if count>18:
            break
        url = tag.get('href', None)

print(url)

# WEB SERVICES: XML AND JSON

## Autograder 1

from urllib import request
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_1422370.xml'
print ("Retrieving", url)
html = request.urlopen(url)
data = html.read()
print("Retrieved",len(data),"characters")

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
icount=len(results)
isum=0

for r in results:
    isum += float(r.find('count').text)
print(icount)
print(isum)

## Autograder 2

import urllib.request as ur
import json

json_url = input("Enter location: ")
print("Retrieving ", json_url)
data = ur.urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

sum = 0
total = 0

for comment in json_obj["comments"]:
    sum += int(comment["count"])
    total += 1

print('Count:', total)
print('Sum:', sum)

## Autograder 3  equal to geojson.py

import urllib.request as ur
import urllib.parse as up
import json

serviceurl = "http://py4e-data.dr-chuck.net/json?"
# This API only accepts the university in a list of its accepted ones.
# This API uses the same parameters (sensor and address) as the Google API.
# This API also has no rate limit so you can test as often as you like.
# If you visit the URL with no parameters, you get a list of all of the address values which can be used with this API.

address_input = input("Enter location: ")
params = {"sensor": "false", "address": address_input}
url = serviceurl + up.urlencode(params)
print("Retrieving ", url)
data = ur.urlopen(url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

place_id = json_obj["results"][0]["place_id"]
print("Place id", place_id)     

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
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    
   
   # DATABASES 
    
    ## Autograder 1
    
import sqlite3
conn = sqlite3.connect('emaildb2.sqlite')
cur = conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS Counts''')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
fh = open('mbox.txt', 'r')
list_1 = []

for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    dom = email.find('@')
    org = email[dom+1:len(email)]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()

## Autograder 3

import xml.etree.ElementTree as ET
import sqlite3
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()
# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'Library.xml'
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>
def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))


## Autograder 4

import json
import sqlite3
# PART 1: Creating the database
dbname = "roster.sqlite"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;
    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    );
    CREATE TABLE Member (
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY(user_id, course_id)
    )''')
# Note: if we don't add UNIQUE after "User.name" and "Course.title",
# the IGNORE statement won't work and therefore we'll have duplicates
# PART 2: DESERIALIZING THE data
# The JSON data we're going to process is stored in an array form, with each
# item being also an array of three elements: one corresponding to the username
# one corresponding to the course name, and one indicating if the user is instructor
# None of them has any field title.
filename = "roster_data.json"
jsondata = open('roster_data.json')
data = json.load(jsondata)
# PART 3: INSERTING DATA
for entry in data:
    user = entry[0]
    course = entry[1]
    instructor = entry[2]
    # Inserting user
    user_statement = """INSERT OR IGNORE INTO User(name) VALUES( ? )"""
    SQLparams = (user, )
    cur.execute(user_statement, SQLparams)
    # Inserting course
    course_statement = """INSERT OR IGNORE INTO Course(title) VALUES( ? )"""
    SQLparams = (course, )
    cur.execute(course_statement, SQLparams)
    # Getting user and course id
    courseID_statement = """SELECT id FROM Course WHERE title = ?"""
    SQLparams = (course, )
    cur.execute(courseID_statement, SQLparams)
    courseID = cur.fetchone()[0]
    userID_statement = """SELECT id FROM User WHERE name = ?"""
    SQLparams = (user, )
    cur.execute(userID_statement, SQLparams)
    userID = cur.fetchone()[0]
    # Inserting the entry
    member_statement = """INSERT INTO Member(user_id, course_id, role)
        VALUES(?, ?, ?)"""
    SQLparams = (userID, courseID, instructor)
    cur.execute(member_statement, SQLparams)
# Saving the changes
conn.commit()
# PART 4: Testing and obtaining the results
test_statement = """
SELECT hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X"""
cur.execute(test_statement)
result = cur.fetchone()
print("RESULT: " + 'XYZZY' +str(result))
# Closing the connection
cur.close()
conn.close()

## OBJECT PROGRAMMING

x=tuple()
dir(x)

class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()

#----
class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy')
m = PartyAnimal('Miya')

q.party()
m.party()
q.party()