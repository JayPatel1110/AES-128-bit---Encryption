#####shift row function#######
def shift(l2,n2): # for left shift operation
    return l2[n2:] + l2[:n2]
r3=['63', 'ca', 'b7', '04', '09', '53', 'd0', '51', 'cd', '60', 'e0', 'e7', 'ba', '70', 'e1', '8c']
print 'Input:',r3
def sr(r3in):
    rpt=0
    r4=[]
    while rpt<(len(r3in)/4):
        for i in xrange(rpt,len(r3in),4):
            r4.append(r3in[i])
        rpt+=1
#    print r4####column results
    r5=[]
    temp=[]
    rpt=rpt1=gain=0
    var2=len(r4)/4
    while rpt<(var2):
        for i in xrange(rpt1,(var2+gain)):
            temp.append(r4[i])
        temp=shift(temp,rpt)
        r5=r5+temp
        temp=[]
        rpt1+=var2
        gain+=var2
        rpt+=1
#    print r5
    rpt=0
    out=[]
    while rpt<(len(r5)/4):
        for i in xrange(rpt,len(r5),4):
            out.append(r5[i])
        rpt+=1
    return out
print 'Output:',sr(r3)
