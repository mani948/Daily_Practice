t = int(input())   

for i in range(t):
    n = int(input())  
    temp = n           
    count = 0

    while temp > 0:
        digit = temp % 10   

        if digit != 0 and n % digit == 0:
            count = count + 1

        temp = temp // 10  

    print(count)