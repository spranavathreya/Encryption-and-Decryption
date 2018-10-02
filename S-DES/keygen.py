import pbox as pb
import shift as sft
def keygen(p):
    h1=[]
    h2=[]
    p=pb.pbox(p)
    for i in range(5):
        h1.append(p[0])
        del(p[0])
    h2=p
    h1=sft.shift(h1,1)
    h2=sft.shift(h2,1)
    p=h1+h2
    ke1=p
    p=pb.pboxsh(p)
    return p,ke1
def keygen2(p):
    h1=[]
    h2=[]
    for i in range(5):
        h1.append(p[0])
        del(p[0])
    h2=p
    h1=sft.shift(h1,2)
    h2=sft.shift(h2,2)
    p=h1+h2
    ke2=p
    p=pb.pboxsh(p)
    return p,ke2
    
    
    
