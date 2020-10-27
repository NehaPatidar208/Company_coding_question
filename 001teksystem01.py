#WAP to count the no of swaps to sort a given array using bubble sort

def countSwap(arr):
    for i in range(0,len(arr)):
        c=0
        for j in range(1,len(arr)-1):
            if arr[j]>arr[j+1]:
                c+=1
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return c

arr=list(map(int,input().split()))
print(countSwap(arr))
