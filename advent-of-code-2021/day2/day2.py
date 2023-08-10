#!/usr/bin/env python
# coding: utf-8

f=open("day2.txt","r")
lines=[]
for line in f:
    line_split = (line.rstrip('\n')).split(" ")
    lines.append(line_split)
f.close()

sum_forward=0
sum_down=0
sum_up=0
for i in range(len(lines)):
    if lines[i][0]=="forward":
        sum_forward+=int(lines[i][1])
    elif lines[i][0]=="down":
        sum_down+=int(lines[i][1])
    elif lines[i][0]=="up":
        sum_up+=int(lines[i][1])      
depth=sum_down-sum_up
print(depth)
print(sum_forward)
print(depth*sum_forward)

### PART 2
aim=0
horizontal_pos=0
depth=0
for i in range(len(lines)):
    if lines[i][0]=="down":
        aim+=int(lines[i][1])
    elif lines[i][0]=="up":
        aim-=int(lines[i][1])
    elif lines[i][0]=="forward":
        horizontal_pos+=int(lines[i][1])
        depth+=aim*int(lines[i][1])
print(horizontal_pos)
print(depth)
print(horizontal_pos*depth)