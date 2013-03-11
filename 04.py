#!/usr/bin/python
# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib
import re

url_base='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
# url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
# then should be manually reset to...
url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'

r = re.compile('[0-9]*$')

while True:
    res = urllib.urlopen(url)
    str = res.read()
    print "  [%s] >>>\n%s" %(url, str)
    url = url_base + r.findall(str)[0]
