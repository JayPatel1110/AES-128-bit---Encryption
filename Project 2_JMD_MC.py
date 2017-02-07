##### mix column #######
import numpy as np
import math
cnn=['c5','4c','c5','4c','c5','4c','c5','4c','c5','4c','c5','4c','c5','4c','c5','4c']
#cnn=['a7', 'be', '1a', '69', '97', 'ad', '73', '9b', 'd8', 'c9', 'ca', '45', '1f', '61', '8b', '61']
#cnn=['63', '53', 'e0', '8c', '09', '60', 'e1', '04', 'cd', '70', 'b7', '51', 'ba', 'ca', 'd0', 'e7']
print'Input:',cnn
const=['0','0','0','1','1','0','1','1']

def lshift(N,N1):return N[(len(N)-N1):]+N[:(len(N)-N1)]
#############repeat function##############
def binary(N):# hex(string) to binary(string) conversion 
    log=int(math.log(16,2))
    bits=len(N)*log
    return str(bin(int(N,16))[2:].zfill(bits))
def seg(N):
    oseg=[]
    for i in N:
        oseg.append(i)
    return oseg
def left(N):
    lft=N[1:]
    lft.append('0')
    return lft
def nonlst(N):#####repeat######
    s1=map(str,N)
    s1=''.join(s1)
    return s1
#####repeat function######
def xor(N,N2):# N2(string) xor N3(string)[bitlevel]; output e is string list
    e=[]
    for i,j in zip(N,N2):
        if i==j:
            c='0'
        else:
            c='1'
        e.append(c)
    return e
def hexa(N):# binary(string) to hex(string) conversion
    N=int(N,2)
    return hex(N).split('x')[1]
def fix(N):
    if N=='0':
        tempfix='00'
    elif N=='1':
        tempfix='01'
    elif N=='2':
        tempfix='02'
    elif N=='3':
        tempfix='03'
    elif N=='4':
        tempfix='04'
    elif N=='5':
        tempfix='05'
    elif N=='6':
        tempfix='06'
    elif N=='7':
        tempfix='07'
    elif N=='8':
        tempfix='08'
    elif N=='9':
        tempfix='09'
    elif N=='a':
        tempfix='0a'
    elif N=='b':
        tempfix='0b'
    elif N=='c':
        tempfix='0c'
    elif N=='d':
        tempfix='0d'
    elif N=='e':
        tempfix='0e'
    elif N=='f':
        tempfix='0f'
    else:
        tempfix=N
    return tempfix
def poly(N,N1):#input:N-strings(4 hex nos.) N1-required shift for mc, output:strings(4 hex nos.)
    rpt=0
    opoly=[]
    mc=['2','3','1','1']
    mc=lshift(mc,N1)
    while rpt<len(N):
        num=N[rpt]
        num=binary(num)###converts hex(string) to binary(string)
        num=seg(num)# converts '1110 0001' in to '1','1','1','0','0','0','0','1'
        if mc[rpt]=='2':
            buf=num
            num=left(num)#left shift operation; '1','1','1','0','0','0','0','1'==>'1','1','0','0','0','0','1','0'
            if buf[0]=='1':
                num=xor(num,const)# bitwise xor operation; both in:string, one out: string
            num=nonlst(num)
            num=hexa(num)
            num=fix(num)
            opoly.append(num)

        if mc[rpt]=='3':
            buf=num
            num=left(num)
            if buf[0]=='1':
                num=xor(num,const)# bitwise xor operation; both in:string, one out: string
            num=xor(num,buf)
            num=nonlst(num)
            num=hexa(num)
            num=fix(num)
            opoly.append(num)
            
        if mc[rpt]=='1':
            num=nonlst(num)
            num=hexa(num)
            num=fix(num)
            opoly.append(num)
        rpt+=1
    otemp=[]
    for i in opoly:
        num=binary(i)
        otemp.append(num)
    omc=xor(otemp[0],otemp[1])
    omc=xor(omc,otemp[2])
    omc=xor(omc,otemp[3])
    omc=nonlst(omc)
    omc=hexa(omc)
    return omc
def MC(N):
    mcf=[]
    rpt=gain=0
    jump=len(N)/4
    while rpt<(len(N)):
        idnn=N[rpt:(jump+gain)]
        idnn1=poly(idnn,0)
        mcf.append(idnn1)
        idnn1=poly(idnn,1)
        mcf.append(idnn1)
        idnn1=poly(idnn,2)
        mcf.append(idnn1)
        idnn1=poly(idnn,3)
        mcf.append(idnn1)
        rpt+=jump
        gain+=jump
    return mcf
dnn=MC(cnn)
print'Output:',dnn
