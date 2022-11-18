def solve(st):
    cnt=0
    prev_i=''
    for i in st:
        if i=='|' and prev_i=='(':
            cnt+=1
        elif i==')' and prev_i=='|':
            cnt+=1
        elif i==')' and prev_i=='(':
            cnt+=1
         
        prev_i=i
 
    return cnt
 
T=int(input())
 
for i in range(1,T+1):
    print("#%d %d"%(i,solve(input())))