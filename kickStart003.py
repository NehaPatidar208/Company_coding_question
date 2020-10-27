def toyJoy(arr,n):
    if(n==1 and arr[0][-1]!=0):
        return "0 "+str(arr[0][0])
    for i in range(n):
        if(arr[i][-1]==0):
            return str(n-1)+" "+"INDEFINITELY"
    sm=0
    for i in range(n):
        sm+=arr[i][-1]
    temp=arr.copy()
    i=0;
    while(i!=len(temp)):
        if(temp[i][1]>sm-temp[i][0]):
            sm-=temp[i][0]
            temp.pop(i)
            i=0
        else:
            i+=1
    i=0
    while True:
        if(i==len(temp)):
            
            return str(len(arr)-len(temp)-2)+" "+"INDEFINITELY"
        elif(temp[i][1]>sm-temp[i][0]):
            break
    i=0
    sm=0
    tmp=0
    while True:
        if i<len(arr):
            sm+=arr[i%len(arr)][0]
            temp+=arr[i][0]
            i+=1
        elif(arr[i][1]<sm-arr[i][0]):
            sm+=arr[i][0]
            i+=1
        else:
            break
    return "0"+" "+str(temp)
           

t=int(input())
for i in range(t):
    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    print("Case #{}:".format(i+1),toyJoy(arr,n))
