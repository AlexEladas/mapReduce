#!/usr/bin/env python
#coding: utf-8
import sys
import csv
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

file = sys.stdin
with file as f:

    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items(): # go over each column name and value
            columns[k].append(v) # append the value into the appropriate list
workaround = []


#print columns['Collection Start/D\xe9but du pr\xe9l\xe8vement (UTC)']
   
for city, date, mdc in zip(columns['Location/Emplacement'],columns['Collection Start/D\xe9but du pr\xe9l\xe8vement (UTC)'], columns['7Be MDC/7Be CMD (mBq/m3)']):
    print '%s\t%s\t%s' % (city,date,mdc)

#Collection Start/Début du prélèvement (UTC)
