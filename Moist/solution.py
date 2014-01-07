'''
Created on Oct 9, 2013

@author: mohaprit
'''
f = open('small','r')
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
    print "Done"
    
    
#ANOTHER SOLUTION

'''
def read_N_Lines(f,n):
    lines = []
    for x in range(0,n):
        lines.append(f.readline())
    return lines
    
f = open('CSmall','r')
case = int(f.readline())
while case > 0:
    cnt = 0
    num = int(f.readline())
    items = read_N_Lines(f,num)
    m = items[0]
    for item in items:
        if item >= m:
            m = item
        elif item < m:
            cnt += 1
    print cnt
    case -= 1
             
'''   