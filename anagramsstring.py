def anagrams(s1,s2):
    s1=sorted(s1)
    s2=sorted(s2)
    
    
    for ch in s1[:]:
        if ch in s2:
            s2.remove(ch)
            s1.remove(ch)
            
    return len(s1)+len(s2)
    
s1=input()
s2=input()
print(anagrams(s1,s2))

            
            
           
    
    
    
