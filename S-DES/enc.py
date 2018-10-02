import keygen as kg
import shift as sf
import copy
import pbox as pb
ci=[]
key=[]
temp=[]
enkey=[]
sb1=[['01','00','11','10'],['11','10','01','00'],['00','10','01','11'],['11','01','11','10']]
sb2=[['00','01','10','11'],['10','00','01','11'],['11','00','01','00'],['10','01','00','11']]
print("                     WELCOME TO S-DES ENCRYPTION")
print("="*80)
for i in range(3):
    print()
print("                    ~~~:KEY GENERATION PHASE:~~~")
print("Enter the master key of DES  ",end=" ")
mk=input()
f=open("dfkeysend.txt","r")
key=f.readline()
f.close()
#print(key)
#print(type(key))
msk=list(mk)
#print(len(msk))

for i in range(0,len(msk)):
    enkey.append((int(msk[i])^int(key[i])))   
#print(enkey)
f=open("key.txt","w")
f.write(str(enkey))
f.close()
k1,ke1=kg.keygen(mk)
print(k1)
k2,ke2=kg.keygen2(ke1)
print(k2)
print("                    ~~~:Round Keys generated:~~~")
for i in range(2):
    print()
def enc(data):
    data=pb.ip(data)
    data=fun(data,1)
    for i in range(0,len(data)):
        data[i]=str(data[i])
    #print(data)
    l=data
        
    data=(fun(l,2))
    #print(data)
    sf.shift(data,4)
    #print(data)
    data=pb.ipinv(data)
    #print(data)
    s=""
    for i in range(0,len(data)):
        s=s+str(data[i])
    return s
def fun(data,ct):
    #print("pranav")
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
    if (ct==1):
        while(i<len(rd)):
            if(rd[i]==k1[i]):
                temp.append(0)
                i=i+1
            else:
                temp.append(1)
                i=i+1
    if (ct==2):
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
    
