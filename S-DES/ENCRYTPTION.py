import enc as sd
print("                               plain text")
print("-"*80)
data=input()
ct=[]
j=[]
l=[]
for i in range(0,len(data)):
     j.append(ord(data[i]))
#print(j)
for i in range(0,len(j)):
    temp=[]
    l=format(j[i],'08b')
    #print(l)
    ct.append(sd.enc(l))
#print(str(ct))
f=open("cipher.txt","w")
f.write(str(ct))
f.close()
print("                               cipher text")
print("-"*80)
cip=[]
for i in range(0,len(ct)):
     print((chr(int(str(ct[i]),2))),end=" ")
     k=(chr(int(str(ct[i]),2)))
     cip.append(k)
print()

cp=str(cip)
cp=cp.replace("[","")
cp=cp.replace("]","")
cp=cp.replace(",","")
cp=cp.replace("'","")
f=open("cip.txt","w")
f.write(cp)
f.close()
print("You have completed the ENCRYPTION")
    
