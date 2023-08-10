#!/usr/bin/env python
# coding: utf-8

f=open("day1.txt","r")
lines=f.readlines()
f.close()
lines=[int(s.replace("\n","")) for s in lines]

### PART 1
increase=0
for i in range(1,len(lines)):
    previous=lines[i-1]
    current=lines[i]
    if current>previous:
        increase+=1
print(increase)

### PART 2
inc2=0
for i in range(len(lines)):
    previous2=lines[i:i+3]
    current2=lines[i+1:i+4]
    if sum(current2)>sum(previous2):
        inc2+=1
print(inc2)