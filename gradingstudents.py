n = int(input())

for i in range(n):
    grade = int(input())

    if grade >= 38:
        next_multiple = grade + (5 - grade % 5)

        if next_multiple - grade < 3:
            grade = next_multiple

    print(grade)