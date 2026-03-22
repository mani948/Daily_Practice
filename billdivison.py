n,k = map(int,input().split())
bill = list(map(int,input().split()))
b = int(input())

total = sum(bill)

actual_share = (total - bill[k]) // 2

if b == actual_share:
    print("Bon Appetit")
else:
    print(b - actual_share)