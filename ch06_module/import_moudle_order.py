import sys

i = 0
for lt in sys.path:
    print("%2d 순위 > %s" % (i, lt))
    i += 1