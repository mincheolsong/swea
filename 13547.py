# import sys
# input = sys.stdin.readline
 
 
def solve():
    cnt=0
 
    for i in s:
        if i=='o':
            cnt+=1
     
    if 15-len(s) >= 8-cnt:
        return True
     
    return False
 
T=int(input())
 
for i in range(T):
    s=input()
    solve()
    if solve():
        print('#{0} YES'.format(i+1))
    else:
        print('#{0} NO'.format(i+1))