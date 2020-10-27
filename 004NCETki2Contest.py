
def contest(a,b):
    a1,a2=map(int,a.split(":"))
    b1,b2=map(int,b.split(":"))
    a=(a1*60)+a2
    b=(b1*60)+b2
    c=(a+b)//2
    c1,c2=(c)//60,(c)%60
    c=str(c1)+":"+str(c2)
    return c


a=input()
b=input()
print(contest(a,b))
