# ----------- Web Crawling with Recursion ------------------------------

from urllib import request, parse, error
from bs4 import BeautifulSoup
import ssl

def crawler(url, position=1, repeat=0):
    html = request.urlopen(url, context=ctx)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')    # returns a list of all anchor tags
    
    if not repeat:
        return tags[position-1].contents[0]
    else:
        url = tags[position-1].get('href', None)    #position==1, -1 => 0
        print(tags[position-1].contents[0])
        crawler(url, position, repeat-1)    # recursion

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url1 = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url2 = 'http://py4e-data.dr-chuck.net/known_by_Etiene.html'

crawler(url1, 3, 4)
crawler(url2, 18, 7)