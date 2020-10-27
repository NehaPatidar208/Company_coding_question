def traverse(s):
    tmp=0
    i=1
    sm=''
    while(tmp!=len(s)):
        #print(" ".join(s[tmp:tmp+i]),end=' ')
        sm=sm+" ".join(s[tmp:tmp+i][::-1])+" "
        tmp=tmp+i
        i=i*2
        if(tmp>=len(s)):
            break
    
    sm=sm[:-1]
    while(sm[-1]=='-'):
        sm=sm[:-2]
        
    return sm


st=list(map(str,input().split()))
print(traverse(st))
