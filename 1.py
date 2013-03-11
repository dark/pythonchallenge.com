#!/usr/bin/python

import string

str="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

rot2 = string.maketrans(
 "abcdefghijklmnopqrstuvwxyz",
 "cdefghijklmnopqrstuvwxyzab")

print string.translate(str, rot2)
print string.translate('map', rot2)
