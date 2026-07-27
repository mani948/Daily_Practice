def minimumLoss(price):
    pos = {}

    for i in range(len(price)):
        pos[price[i]] = i

    price.sort()

    ans = float('inf')

    for i in range(1, len(price)):
        lower = price[i - 1]
        higher = price[i]

        if pos[higher] < pos[lower]:
            ans = min(ans, higher - lower)

    return ans


n = int(input())
price = list(map(int, input().split()))

print(minimumLoss(price))
