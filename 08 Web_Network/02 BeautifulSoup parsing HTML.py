# --------- parsing HTML w/ Regular Expression ------------------------------

# Regex works well if HTML is well written and not broken. 
# BeautifulSoup is a robut HTML parsing library, so that you don't have to write your own regex and tolerates highly flawed HTML. 

#Ex 1: find all the links in a webpage 
import urllib.request, urllib.parse, urllib.error
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# read() method returns HTML source code as a bytes object instead of returning
# an HTTPResponse object
html = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm', context=ctx).read()
print(html)
# b'<h1>The First Page</h1>\n<p>\nIf you like, you can switch to the \n<a href="http://www.dr-chuck.com/page2.htm">\nSecond Page</a>.\n</p>\n'

# NB! read() returns a binary string, i.e. regex arg should match binary i.e. b''
# strings start with "http:// or "https:// followed by >= 1 char, followed by another double quote " - (sub) is what is extracted
# re.findall() extracts substring into a list of strings
links = re.findall(b'href="(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())
    
    

# -------------- BeautifulSoup HTML parsing ---------------------------------
# documentation https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
# BS creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner.

# Ex 1 HTML parsing w/ BS
# This list is much longer because some HTML anchor tags are relative paths (e.g., tutorial/index.html) or in-page references (e.g., ‘#’) that do not include “http://” or “https://”, which was a requirement in our regular expression.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# html.read() is redundant here b/c BS can handle filehandle interface instead of string interface
# https://stackoverflow.com/questions/35863595/what-does-read-in-urlopenhttp-read-do-urllib
html = urllib.request.urlopen('https://docs.python.org', context=ctx)
# html.parser is the HTML parser included in the standard Python 3 library
# for other parsers, https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, 'html.parser')
print(soup)     

tags = soup('a')

# Retrieve all of the anchor tags
# anchor text is <a href="www.google.com">link here</a>
# tag.get() is like dict.get() method, returns None by default
for tag in tags:
    print(tag.get('href', None))    

# Look at parts of a tag
for tag in tags:
    print('TAG:', tag)
    print('URL:', tag.get('href', None)) # this gives the url -  get href key, or return None is there isn't any
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)


# Ex 2a HTML parsing w/ BS
from urllib import request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url1 = 'http://py4e-data.dr-chuck.net/comments_42.html'
url2 = 'http://py4e-data.dr-chuck.net/comments_1629781.html'

def span_getter(url):
    html = request.urlopen(url, context=ctx)
    soup = BeautifulSoup(html, 'html.parser')
    
    tags = soup('span')    # returns a list of all span tags
    
    total = 0
    
    for tag in tags:
        # li = li.append(int(tag.contents[0]))
        # print(tag.contents[0])
        total += int(tag.contents[0])
    
    return total

sum1 = span_getter(url1)
print(sum1)
sum2 = span_getter(url2)
print(sum2)
