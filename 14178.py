def solve(n,d):
    d=2*d+1
 
    if n%d>0:
        return n//d + 1
    else:
        return n//d
 
T=int(input())
 
for i in range(T):
    N,D = map(int,input().split())
    print('#{0} {1}'.format(i+1,solve(N,D)))