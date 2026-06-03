q=int(input())
for _ in range(q):
    s=input()
    delete=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            delete+=1
    print(delete)
        
    