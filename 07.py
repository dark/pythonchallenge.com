#!/usr/bin/python
# http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image

filename = '07.data/oxygen.png'

with Image.open(filename, 'r') as pngfile:
    print ("Size is (%d x %d)" % pngfile.size)
    width , height = pngfile.size
    halfheight = height / 2
    print "Reading unique values from all pixels in the middle row"
    fullstring = ""
    x = 0
    while x < width:
        pixtuple = pngfile.getpixel((x, halfheight))
        # pixtuple = (R, G, B, alpha)
        print ("%d (ASCII %s)" % (pixtuple[0], chr(pixtuple[0])))
        fullstring += chr(pixtuple[0])
        x += 7
    print fullstring
    # after printing the above....
    result = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    res_str = ""
    for n in result:
        res_str += chr(n)
    print res_str
