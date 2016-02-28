#!/usr/bin/python
# http://www.pythonchallenge.com/pc/return/5808.html

from PIL import Image

filename = '11.data/cave.jpg'

with Image.open(filename, 'r') as image:
    print ("Size is (%d x %d)" % image.size)

    width, height = image.size
    newsize = (width / 2, height / 2)
    odd = Image.new(image.mode, newsize)
    even = Image.new(image.mode, newsize)

    for x in range(width):
        for y in range(height):
            if (x + y) % 2:
                # this is odd
                odd.putpixel((x / 2, y / 2), image.getpixel((x, y)))
            else:
                # this is even
                even.putpixel((x / 2, y / 2), image.getpixel((x, y)))

    odd.save("11.data/odd.jpg")
    even.save("11.data/even.jpg")
