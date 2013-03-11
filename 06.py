#!/usr/bin/python
# http://www.pythonchallenge.com/pc/def/channel.html

import re
import zipfile

r = re.compile('[0-9]*$')

zipfilename = '06.data/channel.zip'
compressed_path = '90052.txt'

with zipfile.ZipFile(zipfilename, 'r') as zfile:
    while True:
        f = zfile.open(compressed_path, 'r')
        str = f.read()
        # print "  [%s] >>>\n%s" %(compressed_path, str)
        print zfile.getinfo(compressed_path).comment ,
        # proceed with the next iteration
        compressed_path = r.findall(str)[0] + '.txt'
