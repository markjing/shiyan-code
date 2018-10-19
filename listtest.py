#!/usr/bin/env python3

import sys

list1 = []
list2 = []
for item in sys.argv[1:]:
    if len(item) >3:
        list1.append(item)
    else:
        list2.append(item)

print(' '.join(list1))
print(' '.join(list2))
