students = list(map(int, input().split()))
average_height = sum(students) / len(students)
ans = filter(lambda x: x > average_height, students)
print(*ans, end=' ')
