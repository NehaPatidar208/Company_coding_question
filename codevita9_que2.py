def factors(n):
    fact_l=[]
    i=1
    while(n!=i):
        if n%i==0:
            n=n//i
            i=1
            fact_l.append(n)
        i+=1
    fact_l.append(1)
    fact_l.sort(reverse=True)
    #print(fact_l)
    return fact_l
def function(num1,num2):
    if(num1==num2):
        return 0
    a=factors(num1)
    b=factors(num2)
    count_res=0
    i=j=0
    while(True):
        if(a[i]<b[j]):
            count_res+=1
            j+=1
        elif(b[j]<a[i]):
            count_res+=1
            i+=1
        elif(b[j]==a[i]):
            break
    return count_res
a,b=map(int,input().split())

print(function(a,b))
