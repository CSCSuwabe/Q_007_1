n, x = input().split()
a = list(map(str, input().split()))
bug = 0

for i in range(int(n)):
    if(x in a[i]):
        bug += 1

print(bug)