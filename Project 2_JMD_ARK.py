from numpy import matrix as mat
import math
def binary(N):# hex(string) to binary(string) conversion 
    log=int(math.log(16,2))
    bits=len(N)*log
    return str(bin(int(N,16))[2:].zfill(bits))
def hexa(N):# binary(string) to hex conversion
    N=int(N,2)
    return hex(N).split('x')[1]
def xor(N,N1):# N2(string) xor N3(string)[bitlevel]; output e is string list
    e=[]
    for i,j in zip(N,N1):
        if i==j:
            c='0'
        else:
            c='1'
        e.append(c)
    return e
def lst(N):
    b=[]
    var=0
    while var<8:
        b.append(N[var])#integer
        var+=1
    return b
def nonlst(N):
    s1=map(str,N)
    s1=''.join(s1)
    return s1
#data=raw_input('Enter the data string in Hex format:')
#key=raw_input('Enter the key in Hex format:')
data='00112233445566778899aabbccddeeff'
key='000102030405060708090a0b0c0d0e0f'
def ark(data,key):
    t=0
    d=[]
    k=[]
    while t<len(data):
        a1=data[t]+data[t+1]
        d.append(a1)
        t+=2
#   print len(d)
    t=0
    while t<len(key):
        a2=key[t]+key[t+1]
        k.append(a2)
        t+=2
#   print k
    t=0
    out=[]
    while t<len(d):
        d1=d[t]
        k1=k[t]
#   d1=lst(d1) not required actually because for i,j in (N1,N2) takes one element at a time
#   k2=lst(k1) same as above
        d1=binary(d1)
        k1=binary(k1)
        temp0=xor(d1,k1)
        print temp0
        temp0=nonlst(temp0)
        print temp0
        temp0=hexa(temp0)
        if temp0=='0':
            temp0='00'
        elif temp0=='1':
            temp0='01'
        elif temp0=='2':
            temp0='02'
        elif temp0=='3':
            temp0='03'
        elif temp0=='4':
            temp0='04'
        elif temp0=='5':
            temp0='05'
        elif temp0=='6':
            temp0='06'
        elif temp0=='7':
            temp0='07'
        elif temp0=='8':
            temp0='08'
        elif temp0=='9':
            temp0='09'
        elif temp0=='a':
            temp0='0a'
        elif temp0=='b':
            temp0='0b'
        elif temp0=='c':
            temp0='0c'
        elif temp0=='d':
            temp0='0e'
        elif temp0=='e':
            temp0='0e'
        elif temp0=='f':
            temp0='0f'
        else:
            pass
        out.append(temp0)
        t+=1
#    print out
    return out
print ark(data,key)
