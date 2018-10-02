def shift(p,k):
    for i in range(0,k):
        p.append(p[0])
        del(p[0])
    return p

    

