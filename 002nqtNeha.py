n=int(input())
l=[]
while True:
    try:
        t=int(input())
        if t<0:
            break
        l.append(t)
    except:
        break
if n!=len(l):
    print("Wrong Input")
else:
    l.sort()
    for i in range(1,n):
        if l[i]==l[i-1]:
            l[i]+=1
    print(sum(l))
        
