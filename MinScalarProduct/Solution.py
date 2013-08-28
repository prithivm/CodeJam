'''
Created on Aug 28, 2013

@author: mohaprit
'''
f = open('input')
out = open('output', 'w')
cases = int(f.readline())
n = 0
while cases > 0:
    length = int(f.readline())
    x = sorted(map(int, [int(items) for items in f.readline().split()]))
    y  = reversed(sorted(map(int, [int(item) for item in f.readline().split()])))
    sv = sum(a[0]*a[1]for a in zip(x,y))
    n += 1
    output = "Case #%d: %d\n" %(n, sv)
    out.write(output)
    cases -= 1
print "Written to file"