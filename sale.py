p, d, m, s = map(int, input().split())

count = 0
price = p

while s >= price:
    s = s - price
    count = count + 1
    
    price = price - d
    
    if price < m:
        price = m

print(count)