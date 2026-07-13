def jimOrders(orders):
    arr = []

    for i in range(len(orders)):
        order_num = orders[i][0]
        prep_time = orders[i][1]

        serve_time = order_num + prep_time

        arr.append((serve_time, i + 1))

    arr.sort()

    result = []

    for serve_time, customer in arr:
        result.append(customer)

    return result


n = int(input())

orders = []

for _ in range(n):
    a, b = map(int, input().split())
    orders.append([a, b])

answer = jimOrders(orders)

print(*answer)