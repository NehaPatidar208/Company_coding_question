def checkLongest(l,n):
    if(n==0):
        return 0
    i=0
    long_chain=1
    temp_diff=1
    diff=0
    j=1
       
    while(i<n-1):
        j=i+1
        if(l[i]-l[j]==diff):
            temp_diff+=1
        long_chain=max(long_chain,temp_diff)
        if(diff!=l[i]-l[j]):
            diff=l[i]-l[j]
            temp_diff=2
        i+=1
    
    return long_chain
            
        

t=int(input())
while t:
    n=int(input())
    l=list(map(int,input().strip().split()))
    print(checkLongest(l,n))
    t-=1
