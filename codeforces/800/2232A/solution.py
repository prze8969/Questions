t = int(input())
 
def findmed(arr):
    n = len(arr)
    if n%2!=0:
        return arr[n//2]
    else:
        mid1 = arr[n//2 - 1]
        mid2 = arr[n//2]
        return mid1
 
for i in range(t):
    n = int(input())
    lin = input().split()
    less=[]
    more=[]
    lin = [int(x) for x in lin]
    lin = sorted(lin)
    l = len(lin)
    m = findmed(lin)
    for i in range(len(lin)):
        if lin[i] < m:
            less.append(lin[i])
        elif lin[i] > m:
            more.append(lin[i])
    ans = max(len(less), len(more))
    print(ans)
 