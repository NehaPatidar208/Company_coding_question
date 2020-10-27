#WAP to to count a given substring in a given string and deletethe substring once it is counted
#do this processes recursively untill no such substring is found in string
#example given_string='ababbaabbbaa' and given_substring='ba' then the output will be 5

def deleteSubstring(s,t):
    sm=0
    print(t in s)
    while(t in s !=False):
        cnt=0
        for i in range(0,len(s)-len(t)+1,1):
            print(s[i:i+len(t)])
            if(s[i:i+len(t)] == t):
                cnt+=1
                print(cnt)
        s=s.replace(t,"")
        sm=sm+cnt
    return sm


t= int(input("Enter the no of testcase"))
for _ in range(t):
    s=input("Enter the string : ")
    t=input("Enter substring : ")
    print(deleteSubstring(s,t))
