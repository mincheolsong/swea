def solve(n):
    component=list(map(int,sorted(str(n))))
    max_n=int(''.join(sorted(str(n),reverse=True)))
     
    i=2
    while n*i<=max_n:
        flag=1
        l=list(map(int,sorted(str(n*i))))
         
        for p in range(len(component)):
            if component[p]!=l[p]:
                flag=0
                break
         
        if flag==1:
            return True
 
        i+=1
     
 
    return False
 
 
T=int(input())
 
for i in range(T):
    N=int(input())
    if solve(N):
        print('#{0} possible'.format(i+1))
    else:
        print('#{0} impossible'.format(i+1))