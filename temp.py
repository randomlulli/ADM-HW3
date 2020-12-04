# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


S="CADFECEILGJHABNOPSTIRYOEABILCNR"

w = 0
result = ''


def find_substrings(string):
    global w
    global result
    
    a = [char for char in string]
    l = [a[0]]

    for i in range(len(string) - 1):   
        if ord(string[i+1]) > ord(l[-1]) and string[i+1] not in l:
            l.append(a[i+1])
        
    if len(l) > w:
        w = len(l)
        result = ''.join(l)
        
        
find_substrings(S)
        
print(w)
print(result)
