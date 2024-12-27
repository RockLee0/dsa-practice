#1
def patternMap(a,b):
    s={}
    t={}
    c=b.split()
    #1: check length
    if len(a)!=len(c):
        return False
    for p,q in zip(a,c):
        if (p in s and s[p]!=q) or (q in t and t[q]!=p):
            return False
        else:
            s[p]=q
            t[q]=p
    return True


print(patternMap('abba','dog cat cat dog'))

#2
def t(pattern,s):
    p_ = {}
    q_ = {}
    c = s.split()
    if len(pattern) != len(c):
        return False
    for p, q in zip(pattern, c):
        if (p in p_ and p_[p] != q) or (q in q_ and q_[q] != p):
            return False
        else:
            p_[p] = q
            q_[q] = p
    return True

print(t('abba','dog cat cat dog'))






#3
#---------------------------------------------
def patternMsap(a, b):
    s = {}
    t = {}
    c = b.split()

    # Step 1: Check length
    if len(a) != len(c):
        return False

    # Step 2: Build mappings
    for p, q in zip(a, c):
        if p in s:
            # Check if the existing mapping is consistent
            if s[p] != q:
                return False
        else:
            s[p] = q

        if q in t:
            # Check if the existing mapping is consistent
            if t[q] != p:
                return False
        else:
            t[q] = p

    print("Mapping s:", s)
    print("Mapping t:", t)
    return True

