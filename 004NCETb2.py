import math
def isPrime(num):
    if (num==1):
        return False
    if(num==2 or num==3):
        return True
    for i in range(2,math.floor(num/2)+1):
        if(num%i==0):
            return False
    return True

def b2Pottykrgai(s,n):
    
    l1=[]
    l2=[]
    for i in s:
        t=ord(i)
        if(isPrime(t)==True):
            l1.append(i)
        else:
            l2.append(i)
    l1.sort()
    l2.sort(reverse=True)
    str=''.join(l1)
    str+=''.join(l2)

    return str

n=int(input())
s=input()
print(b2Pottykrgai(s,n))
