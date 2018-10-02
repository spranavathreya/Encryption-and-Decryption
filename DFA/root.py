def root(a,q):
    lis=[]
    se={}
    for  i in range(1,q):
        j=1
        while(j<q):
            l=(a**j)%q
            lis.append(l)   
            j=j+1
        se=set(lis)    
        if(len(lis)==len(se)):
            return a
        else:
            return 0

