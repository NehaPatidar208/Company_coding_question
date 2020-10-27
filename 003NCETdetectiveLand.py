def result(a,b,n):
    if(a<n or b<n):
        return "New One"
    if(a!=b):
        return "Sorry"
    return "Goit it"

n=int(input())
T=int(input())
for _ in range(T):
    a=int(input())
    b=int(input())
    print(result(a,b,n))
    
