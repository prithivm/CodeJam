'''
Created on Jan 7, 2014

@author: prithiv
'''
def find_pq(n):
    n = bin(n)[3:]
    p,q = 1,1
    for i in n:
        if i =='0':
            p,q = p,p+q
        else:
            p,q = p+q,q
    return p,q

def find_n(p,q):
    n,m = 0,1
    while (p>1) or (q>1):
        if p<q:
            p,q = p,q-p
        else:
            p,q = p-q,q
            n= n+m
        m = m*2
    return str(n+m)

f = open('Input','r')
case = int(f.readline())
num = 0
while case > 0:
    inp = [int(x) for x in f.readline().split()]
    if inp[0] == 1:
        ans = find_pq(inp[1])
    else:
        ans = find_n(inp[1], inp[2])
    num += 1
    print "Case #%d:%s\n" %(num, ans)
    case -= 1