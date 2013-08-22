'''
Created on Aug 22, 2013

@author: mohaprit
'''
#print ' '.join( [ word[::-1] for word in s.split() ] )[::-1]

f = open("large.in")
out = open('output', 'w')
cases = int(f.readline())
n = 0
#output = ''
for i in range(0, cases):
    while cases >0:
        n += 1
        s = f.readline()
        rev_words = ' '.join( [ word[::-1] for word in s.split() ] )[::-1]
        
        output = "Case# %d: %s\n" %(n, rev_words)
        out.write(output)
        cases -= 1
        

print "Written to File Output"