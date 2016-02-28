#!/usr/bin/python
# http://www.pythonchallenge.com/pc/return/bull.html

# Image link leads to:
#
# http://www.pythonchallenge.com/pc/return/sequence.txt
#
# with content:
#
# a = [1, 11, 21, 1211, 111221,

idx = 1
prev= "1"
while idx < 31:
    new = ""
    lastchar = 0
    cnt = 0
    for x in prev:
        if not lastchar:
            lastchar = x
            cnt = 1
        elif lastchar == x:
            cnt = cnt + 1
        else:
            new += ("%d%s" % (cnt, lastchar))
            lastchar = x
            cnt = 1
    # for the last, unterminated sequence
    new += ("%d%s" % (cnt, lastchar))

    print "%d: (%d) [%s]" % (idx, len(new), new)
    prev = new
    idx = idx + 1
