# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 20:59:46 2023

@author: Carson
"""

import csv

sum = 0 # total distance
good = 0 # pitches with length available
bad = 0 # pitches with length unavailable
count = 0 # total ticks
unknown = [] # list of routes with no length info

# Read tick csv file
with open('ticks.csv', newline='') as tickfile:
    ticks = csv.reader(tickfile, delimiter=',', quotechar='"')
    # Check each row
    for t in ticks:
        #print(t[1], t[5])
        if t[13].isnumeric():
            sum += int(t[13]) * int(t[5])
            count += 1
            good += int(t[5])
        elif t[13] == '':
            unknown.append((t[1], t[4]))
            count += 1
            bad += int(t[5])
            
links = set(unknown) # route names and links without duplicates
average = sum / good # average distance per pitch
estimate = average * bad + sum
            
print('Minimum distance climbed: %d feet.' % sum)
print('Estimated total distance climbed: %d feet.\n' % estimate)
print('Unfortunately, %d of the %d ticks (%d pitches) had no listed length.' % (len(unknown), count, bad))
print('Here\'s a list of the route pages that can be updated:')
for l in links:
    print(l[1])