def pangrams(s):
    s = s.lower()
    
    for ch in "abcdefghijklmnopqrstuvwxyz":
        if ch not in s:
            return "not pangram"
    
    return "pangram"


s = input()
print(pangrams(s))