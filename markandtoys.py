def maximumToys(prices, k):
    prices.sort()
    count, total = 0, 0

    for price in prices:
        if total + price <= k:
            total += price
            count += 1
        else:
            break
    return count


n, k = map(int, input().split())
prices = list(map(int, input().split()))
    
result = maximumToys(prices, k)
print(result)