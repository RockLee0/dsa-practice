#Given two strings s and t, return true if t is an anagram of s, and false otherwise

def check(s,t):
    d=[]
    if len(s) == len(t):
        for i in s:
            if  s.count(i)==t.count(i) and i not in d:
                d.append(i)
            else:
                return False
        return True
    return False

print(check('anagram','anagram'));
print(check('anagram', 'nagaram'))  # Output: True
print(check('rat', 'car'))

def check1(s, t):
    d = []
    if len(s) == len(t):
        for i in s:
            if s.count(i) == t.count(i) and i not in d:
                d.append(i)
            else:
                return False
        return True  # All checks passed, so it's an anagram
    return False
print(check1('anagram', 'nagaram'))  # Output: True
print(check1('rat', 'car'))
