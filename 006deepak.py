def result(arr):
    if(len(arr)<=3):
        return 0
    ar1=arr[0::2]
    ar2=arr[1::2]
    ar1.sort()
    ar2.sort()
    
    return ar1[-2]+ar2[1]
lst=list(map(int,input().split()))
print(result(lst))
