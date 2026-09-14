n = int(input())
x_sum=0
y_sum=0
z_sum=0
for i in range(n):
    lin = input().split()
    num = [int(x) for x in lin]
    x_sum+=num[0]
    y_sum+=num[1]
    z_sum+=num[2]
 
if(x_sum == 0 and y_sum==0 and z_sum==0):
    print("YES")
else:
    print("NO")