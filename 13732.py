# import sys
# input = sys.stdin.readline
 
 
def check(r,c,cnt):
     
    if cnt==1:
        for i in range(N):
            for j in range(N):
                if l[i][j]=='#' and i!=r and j!=c:
                    return False
        return True
 
    # 내부 검사
    if cnt>1:
        for p in range(r+1,r+cnt):
            for q in range(c,c+cnt):
                if l[p][q]!='#':
                    return False
     
    # 외부 검사
    for p in range(0,r):
        for q in range(N):
            if l[p][q]=='#':
                return False
    for p in range(r,r+cnt):
        for q in range(0,c):
            if l[p][q]=='#':
                return False
        for q in range(c+cnt,N):
            if l[p][q]=='#':
                return False
    for p in range(r+cnt,N):
        for q in range(N):
            if l[p][q]=='#':
                return False
 
 
    return True
     
     
 
def solve():
    cnt=0
    prev='.'
     
    for j in range(N):
        row=0
        col=0
        for k in range(N):
            if l[j][k]=='#' and prev=='.':
                cnt+=1
                row=j
                col=k
            if l[j][k]=='#' and prev=='#':
                cnt+=1
                if cnt==2:
                    row=j
                    col=k-1
            prev=l[j][k]
 
        if cnt>0:
            if check(row,col,cnt):
                return True
            else:
                return False
 
     
 
T=int(input())
 
for i in range(T):
    N=int(input())
    l=[list(input()) for _ in range(N)]
    if solve():
        print('#{0} yes'.format(i+1))
    else:
        print('#{0} no'.format(i+1))