def check(p,q):
    if len(q)<len(p):
        return False
    for i in p:
        if q.count(i)<p.count(i):
            return False
    return True


from collections import Counter


#best one

def canConstruct( ransomNote, magazine):
        # Count the characters in magazine and ransomNote
        magazine_count = Counter(magazine)
        ransomNote_count = Counter(ransomNote)

        print(magazine_count,ransomNote_count,magazine_count.items()) # remember this

        # Check if magazine has enough characters to construct the ransom note
        for char, count in ransomNote_count.items():
            if magazine_count[char] < count:
                return False
        return True


print(canConstruct('aa','aab'))