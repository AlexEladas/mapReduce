#!/usr/bin/env python
#coding: utf-8
from numpy import median, std
import sys
import dateutil.parser as parser
import collections

data = collections.defaultdict(dict)

for line in sys.stdin:
    line = line.strip()
    city,date,mdc = line.split('\t')
    year = parser.parse(date).year
    #print city,date,mdc
    if year not in data:
        data[year] = {}
    if city not in data[year]:
        data[year][city] = []
    data[year][city].append(float(mdc))
#print data

for year,value in data.iteritems():
    maximum = 0
    minimum = 0
    median1 = 0
    sdev = 0
    for city, mdc in value.iteritems():
        maximum = max(mdc)
        minimum = min(mdc)
        median1 =  median(mdc)
        sdev = std(mdc)
        print '%s\t%s\t%s\t%s\t%s\t%s' % (year,city,maximum,minimum,median1,sdev)

