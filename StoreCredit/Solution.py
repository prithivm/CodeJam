'''
Created on Aug 22, 2013

@author: mohaprit
'''
N = int(raw_input())
for t in xrange(N):
    C = int(raw_input())
    I = int(raw_input())
    list = [int(x) for x in raw_input().split()]
    for i in xrange(I):
        for j in xrange(i+1, I):
            if (list[i]+list[j]==C):
                print "Case #%d: %d %d" % (t+1, i+1, j+1)
                break
        
        
            