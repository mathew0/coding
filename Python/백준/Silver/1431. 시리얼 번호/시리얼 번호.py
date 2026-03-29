import sys
input = sys.stdin.readline

num = int(input())

r = []

for _ in range(num):
    word = input().strip()

    count = 0
    for k in range(len(word)):
        if word[k].isdigit():
            count += int(word[k])

    r.append((word, count))

r.sort(key=lambda x: (len(x[0]), x[1], x[0]))

for word, count in r:
    print(word)