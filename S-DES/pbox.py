def pbox(p):
    temp=[]
    temp.append(p[2])
    temp.append(p[4])
    temp.append(p[1])    
    temp.append(p[6])
    temp.append(p[3])
    temp.append(p[9])
    temp.append(p[0])
    temp.append(p[8])
    temp.append(p[7])    
    temp.append(p[5])
    p=temp
    temp=[]
    return p
def pboxsh(p):
    temp=[]
    temp.append(p[5])
    temp.append(p[2])
    temp.append(p[6])    
    temp.append(p[3])
    temp.append(p[7])
    temp.append(p[4])
    temp.append(p[9])
    temp.append(p[8])
    p=temp
    temp=[]
    return p
def ip(p):
    temp=[]
    temp.append(p[1])
    temp.append(p[5])
    temp.append(p[2])
    temp.append(p[0])
    temp.append(p[3])
    temp.append(p[7])
    temp.append(p[4])
    temp.append(p[6])
    p=temp
    temp=[]
    return p
def ep(p):
    temp=[]
    temp.append(p[3])
    temp.append(p[0])
    temp.append(p[1])
    temp.append(p[2])
    temp.append(p[1])
    temp.append(p[2])
    temp.append(p[3])
    temp.append(p[0])
    p=temp
    temp=[]
    return p
def half(p):
    h1=[]
    h2=[]
    for i in range(4):
        h1.append(p[0])
        del(p[0])
    h2=p
    return h1,h2
    
def check(i,j):
    if (i==0) & (j==0):
        return 0
    if (i==0) & (j==1):
        return 1
    if (i==1) & (j==0):
        return 2
    if (i==1) & (j==1):
        return 3
def ipinv(p):
    temp=[]
    temp.append(p[3])
    temp.append(p[0])
    temp.append(p[2])
    temp.append(p[4])
    temp.append(p[6])
    temp.append(p[1])
    temp.append(p[7])
    temp.append(p[5])
    p=temp
    temp=[]
    return p
def pboxe(p):
    temp=[]
    temp.append(p[1])
    temp.append(p[3])
    temp.append(p[2])
    temp.append(p[0])
    p=temp
    temp=[]
    return p
