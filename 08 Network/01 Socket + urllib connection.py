# ----------------- Socket connection ----------------------------------------
# low level connection, manually send and receive data over HTTP

# socket, connect, send, recv

# Ex 1: Retrieved a plain text file which had newlines in the file
# and copy the data to the screen as the program ran
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
# Receives data in 512-character chunks from the socket and prints the data out 
# until there is no more data to read (i.e., the recv() returns an empty string).
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()


# encode(), decode(), converts string into bytes and back again. 
# b'' and encode() are equivalent
print(b'Hello world')
# b'Hello world'
print('Hello world'.encode())
# b'Hello world'



# Ex 2: Retrieve an image across using HTTP, accumulate the data in a string (binary format),
# trim off the headers, and then save the image data to a file 

import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
# send() vs. sendall()
# https://stackoverflow.com/questions/34252273/what-is-the-difference-between-socket-send-and-socket-sendall
# b'' is equivalent to encode()
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    # wait 0.25 sec btwn each call so that the server can “get ahead” of us and send more data to us before we call recv() again.
    # time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
# +4 because \r\n\r\n are 4 chars
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos+4].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
# mode='wb' opens the file in binary format for writing
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()



# ------------------- urllib connection ------------------------------------
# treat a webpage like a local file object, urllib handles all the HTTP protocol and header details

# Ex 1
# urllib strips off the header automatically -The headers are still sent, but the urllib code consumes the headers and only returns the data to us.
from urllib import request, parse, error 

# type fhand is <http.client.HTTPResponse object at 0x000001332E3FD520>
fhand = request.urlopen('http://data.pr4e.org/romeo.txt')
print(fhand)
# <http.client.HTTPResponse object at 0x000001332E307E80>

# read() https://stackoverflow.com/questions/35863595/what-does-read-in-urlopenhttp-read-do-urllib
# read() method you use an "string" inteface. When you are not, you're using "filehandle" interface.
binary_format = fhand.read()
print(binary_format)
# b'But soft what light through yonder window breaks\nIt is the east and Juliet is the sun\nArise fair sun and kill the envious moon\nWho is already sick and pale with grief\n'
decoded_format = binary_format.decode()
print(decoded_format)
# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief

# for loop through fhand
for line in fhand:
    print(line.decode().strip())


# Ex 2:
import urllib.request, urllib.parse, urllib.error

# open the URL and use read() to download the entire contents of the document into a string variable - in binary format (img) then write that information to a local file:
img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img)
fhand.close()


# Ex 2a: preventing memory overflow
# writing into img file 100k chars at a time. 
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    data = img.read(100_000)
    if len(data) < 1: break
    size = size + len(data)
    fhand.write(data)

print(size, 'characters copied.')
fhand.close()


