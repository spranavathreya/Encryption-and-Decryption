import shift as sf
import keygen as kg
import pbox as pb
def dec(p):
    p=pb.ip(p)
    p=fun(p,1)
    for i in range(0,len(p)):
        p[i]=str(p[i])
    #print(data)
    l=p
    p=(fun(l,2))
    #print(data)
    sf.shift(p,4)
    #print(data)
    p=pb.ipinv(p)
    s=""
    for i in range(0,len(p)):
        s=s+str(p[i])
    return s
def keys():
    mk=""
    f=open("key.txt","r")
    enkey=f.readline()
    f.close()
    f=open("dfkeyrec.txt","r")
    dfkey=f.readline()
    f.close()
    enkey=enkey.replace(",","")
    enkey=enkey.replace(" ","")
    enkey=enkey.replace("[","")
    enkey=enkey.replace("]","")
    dfkey=list(dfkey)
    enkey=list(enkey)
    #print(dfkey,end=" ")
    #print(type(dfkey))
    #print(enkey,end=" ")
    #print(type(enkey))
    for i in range(0,len(enkey)):
        mk=mk+str((int(enkey[i])^int(dfkey[i])))
    k1,ke1=kg.keygen(mk)
    k2,ke2=kg.keygen2(ke1)    
    return k1,k2
k1,k2=keys()
#print(k1)
#print(k2)
def fun(data,ct):
    sb1=[['01','00','11','10'],['11','10','01','00'],['00','10','01','11'],['11','01','11','10']]
    sb2=[['00','01','10','11'],['10','00','01','11'],['11','00','01','00'],['10','01','00','11']]
    ld=[]
    rd=[]
    swl=[]
    swr=[]
    temp=[]
    ld,rd=pb.half(data)
    swl=rd.copy()
    #print(ld)
    #print(rd)
    rd=pb.ep(rd)
    #print(rd)
    i=0
    if (ct==2):
        while(i<len(rd)):
            if(rd[i]==k1[i]):
                temp.append(0)
                i=i+1
            else:
                temp.append(1)
                i=i+1
    if (ct==1):
        while(i<len(rd)):
            if(rd[i]==k2[i]):
                temp.append(0)
                i=i+1
            else:
                temp.append(1)
                i=i+1                
    rd=temp
    #print(rd)
    rd1,rd2=pb.half(rd)
    #print(rd1)
    row1=pb.check(rd1[0],rd1[3])
    #print(row1)
    col1=pb.check(rd1[1],rd1[2])
    #print(col1)
    row2=pb.check(rd2[0],rd2[3])
    #print(row2)
    col2=pb.check(rd2[1],rd2[2])
    #print(col2)
    rd=((sb1[row1][col1])+(sb2[row2][col2]))
    rd=pb.pboxe(rd)
    i=0
    temp=[]
    while(i<len(rd)):
        if(rd[i]==ld[i]):
            temp.append(0)
            i=i+1
        else:
            temp.append(1)
            i=i+1
    swr=temp
    sw=swl+swr
    return sw



