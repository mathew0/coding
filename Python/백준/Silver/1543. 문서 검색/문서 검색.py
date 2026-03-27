import sys
input = sys.stdin.readline

s = input().strip()
find = input().strip()

count = 0
i =0

while i <= len(s) - len(find):
    if s[i:i+len(find)] == find:
        count +=1
        i += len(find)
    else:
        i += 1

print(count)