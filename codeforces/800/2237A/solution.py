t = int(input())
def sumlin(l):
    sum =0
    for i in range(len(l)):
        sum+=l[i]
    return sum
        
 
for i in range(t):
    n = int(input())
    lin = input().split()
    lin = [int(x) for x in lin]
    for i in range(n):
        for j in range(i+1,n):
            if lin[i]<lin[j]:
                lin[j] = lin[i]
    print(sumlin(lin))