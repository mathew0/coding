import sys
input = sys.stdin.readline

a,b = map(int,input().split())

d = {}

for _ in range(a):
    s=input().strip()

    if len(s)<b:
        continue
    
    if s in d:
        d[s][0] += 1
    else:
        d[s] = [1, len(s)]

result = sorted(d.items(), key=lambda x: (-x[1][0],-x[1][1],x[0]))

for r,k in result:
    print(r)