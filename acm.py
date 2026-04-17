n, m = map(int, input().split())

topic = []
for i in range(n):
    topic.append(int(input(), 2))   # binary string to number

max_topics = 0
team_count = 0

for i in range(n):
    for j in range(i + 1, n):
        count = bin(topic[i] | topic[j]).count('1')

        if count > max_topics:
            max_topics = count
            team_count = 1
        elif count == max_topics:
            team_count += 1

print(max_topics)
print(team_count)