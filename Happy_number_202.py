def isHappy(n):
    def cal(n):
        c=0
        d=''
        for i in str(n):
            c+=int(i)*int(i)
        return c
    seen=set()
    while n!=1 and n not in seen:
        seen.add(n)
        n=cal(n)
    return n==1
'''
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

print(isHappy(2))