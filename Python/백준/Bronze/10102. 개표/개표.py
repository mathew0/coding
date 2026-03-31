import sys
input = sys.stdin.readline

num = int(input().strip())

s = input().strip()

count = 0
count2 = 0

for i in range(num):
    if s[i] == 'A':
        count += 1
    else:
        count2 +=1

if count == count2:
    print('Tie')
else:
    if count > count2:
        print("A")
    else:
        print('B')
