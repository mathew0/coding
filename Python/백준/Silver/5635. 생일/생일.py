import sys
input = sys.stdin.readline

num = int(input().strip())

data = []

for i in range(num):
    name, day, month, year = input().split()
    data.append([name,int(day),int(month),int(year)])

data.sort(key=lambda x: (x[3], x[2], x[1]))

print(data[num-1][0])
print(data[0][0])