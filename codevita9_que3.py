from itertools import permutations
def result(start,end,length):
    res_count=0
    temp=list(permutations([i for i in range(start,end+1)],length))
    
    for i in list(temp):
        if sum(i)%2==0:
            res_count+=1
    return res_count

a=list(map(int,input().strip().split()))
l=int(input())
print(result(a[0],a[1],l))
