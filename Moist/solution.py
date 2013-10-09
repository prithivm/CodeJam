'''
Created on Oct 9, 2013

@author: mohaprit
'''
f = open('CSmall','r')
out = open('out','w')
t = int(f.readline())
for i in range(t):
    n = int(f.readline())
    
    cnt = 0
    Max = f.readline()
    
    for j in range(n-1):
        line = f.readline()
        
        if line >= Max:
            Max = line
        else:
            cnt += 1
    output="Case #"+str(i+1)+": "+str(cnt)+'\n'
    out.write(output)
             
    