#!/usr/bin/env python
# coding: utf-8

f=open("day3.txt","r")
codes=f.readlines()
f.close()
codes=[s.replace("\n","") for s in codes]

from collections import Counter
def power_consumption(codes):
    gamma = ''
    epsilon = ''
    somme_gamma=0
    somme_eps=0
    for i in range(len(codes[0])):
        bits = [bit[i] for bit in codes]
        count = Counter(bits)               # Counter({'0': occ_0, '1': occ_1})
        gamma += max(count, key=count.get)  # get key qui a plus d'occurrences(count)
        epsilon += min(count, key=count.get)
    for ind,el in enumerate(reversed(gamma)):
        if el=="1":
            somme_gamma+=2**ind
    for ind,el in enumerate(reversed(epsilon)):
        if el=="1":
            somme_eps+=2**ind
    return somme_gamma*somme_eps
    #return int(gamma, 2) * int(epsilon, 2)  # direct convertit gamma & epsilon en un nombre entier
print(power_consumption(codes))