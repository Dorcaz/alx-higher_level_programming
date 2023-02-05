#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if (i != chr('q') and i != chr('e')):
        print("{:c}".format(i), end=' ')
