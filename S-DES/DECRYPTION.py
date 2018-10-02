import dec
f=open("cipher.txt","r")
data=f.readline()
i=0
ci=[]
pt=[]
s=""
data=data.replace("[","")
data=data.replace("]",".")
data=data.replace("'","")
data=data.replace(" ","")
while(1):
    if (data[i]=='0' or data[i]=='1') and (data[i+1]==","):
        s=s+data[i]
        ci.append(s)
        i=i+2
        s=""
    if data[i]=='0' or data[i]=='1':
        s=s+data[i]
        i=i+1
    if (data[i]=='0' or data[i]=='1') and (data[i+1]=="."):
        s=s+data[i]
        ci.append(s)
        s=""
        break
print("                      Encrypted format of message")
print("-"*80)
for i in range(0,len(ci)):
     print((chr(int(str(ci[i]),2))),end=" ")
print()
for i in ci:
    pt.append(dec.dec(i))
for i in range(0,len(pt)):
    pt[i]=(chr(int(pt[i],2)))
s=""
for i in range(0,len(pt)):
    s=s+pt[i]
print(end="\n"*2)
print("                                Plain text")
print("-"*80)
print(s)
