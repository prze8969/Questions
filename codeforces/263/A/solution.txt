x1=0
y1=0
 
for i in range(5):
    lin = input()
    lin = lin.split()
    lin = [int(x) for x in lin]
    for j in range(len(lin)):
        if lin[j]==1:
            x1=j
            y1=i
        upness=abs(2-y1)
        leness=abs(2-x1)
 
print(upness+leness)
 
 
 