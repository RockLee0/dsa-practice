def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    d = {}
    p=[]
    for i,l in enumerate(s):
        if l in d and t[d[l]]==t[i]:
            print(t[d[l]],t[i])
            p.append((d[l],i))
            print(p)
        else:d[l]=i
    return False


def iso(p,q):
    s={}
    t={}
    for a,b in zip(p,q):  #touple of set: {(e,a), (g,d),(g,d),(r,r),(r,r),(r,r)}
        print(a,b,s,t)
        if (a in s and s[a]!=b) or (b in t and t[b]!=a):
            return False
        s[a]=b
        t[b]=a

    print(type(zip(p,q)),s,t)
    print()
    return True
print(iso('eggrrr','addrpr'))
