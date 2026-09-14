def withoutai(n,x,y):
    hr = 0
    while(n>0):
        lin = x+y
        n-=lin
        hr+=1
    return hr
 
def withai(n,x,y,z):
    hr = 0
    while(n>0):
        if(z<=0):
            lin = x+10*y
            n-=lin
        else:
            lin = x
            n-=lin
            z-=1
        hr+=1
    return hr
 
 
t = int(input())
 
for i in range(t):
    l = input()
    l = l.strip().split()
    l = [int(x) for x in l]
    n = l[0]
    x = l[1]
    y = l[2]
    z = l[3]
    woai = withoutai(n,x,y)
    wai = withai(n,x,y,z)
    if(woai>wai):
        print(wai)
    else:
        print(woai)