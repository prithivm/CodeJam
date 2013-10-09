'''
Created on Oct 9, 2013

@author: mohaprit
'''
import re
alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
time = ["0","1","double","triple","quadruple","quintuple","sextuple","septuple","octuple","nonuple","decuple"]
f = open('largeip', 'r')
out = open('output', 'w')
no_Case = int(f.readline())
n = 0
while no_Case > 0:
    x,y = f.readline().split(' ')
    pat = [int(z) for z in y.split('-')]
    num_Split = []
    tot = 0
    for i in pat:
        num_Split.append(x[tot:tot+i])
        tot += i
    no_Case -= 1
    
    #prev_Val = -1
    list_Res = []
    
    def convert_Operation(items):
        prev_Val = -1
        rep_Cnt = 0
        for digits in items:
            digit = int(digits)
            if digit == prev_Val:
                rep_Cnt += 1
            else:
                if prev_Val != -1:
                    if rep_Cnt > 10:
                        for i in xrange(rep_Cnt):
                            list_Res.append(alpha[prev_Val])
                    elif rep_Cnt == 1:
                        list_Res.append( alpha[prev_Val])
                        
                    else:
                        list_Res.append(time[rep_Cnt])
                        list_Res.append(alpha[prev_Val])
                prev_Val = digit
                rep_Cnt = 1
           
        if prev_Val != -1:
            if rep_Cnt > 10:
                for i in xrange(rep_Cnt):
                    list_Res.append(alpha[prev_Val])
            elif rep_Cnt == 1:
                list_Res.append(alpha[prev_Val])
            else:
                list_Res.append(time[rep_Cnt])
                list_Res.append(alpha[prev_Val])

    for ent in num_Split:
        convert_Operation(ent)
    n += 1
    #output = 'Case %d: %s\n' (n, ' '.join(list_Res))
    print 'Case %d:' %n, ' '.join(list_Res)
    #out.write(output)
no_Case -= 1

            
    

     
