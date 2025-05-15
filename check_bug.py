n, x = input().split()
a = list(map(str, input().split()))
bug = 0

for i in range(int(n)):
    if(a[i] == x):
        bug += 1

print(bug)
