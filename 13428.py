# import sys
# input = sys.stdin.readline
 
 
def find_min():
    m=l[:]
    sorted_m = sorted(m)[m.count('0'):]
    cnt=0
     
    for i in range(len(m)):
        if i==0 and len(sorted_m)>0:
            if m[i]!=sorted_m[cnt]:
                for j in range(len(m)-1,-1,-1):
                    if m[j]==sorted_m[cnt]:
                        m[j]=m[i]
                        break
                m[i]=sorted_m[cnt]
                return m
            del sorted_m[cnt]
 
            for _ in range(m.count('0')):
                sorted_m.insert(0,'0')
        elif len(sorted_m)>0:
            if m[i]==sorted_m[cnt]:
                cnt+=1
            elif m[i]!=sorted_m[cnt]:
                for j in range(len(m)-1,-1,-1):
                    if m[j]==sorted_m[cnt]:
                        m[j]=m[i]
                        break
                m[i]=sorted_m[cnt]
                return m
         
    return m
 
def find_max():
    m=l[:]
    sorted_m = sorted(m,reverse=True)
    cnt=0
     
    for i in range(len(m)):
        if m[i]==sorted_m[cnt]:
            cnt+=1
        elif m[i]!=sorted_m[cnt]:
            for j in range(len(m)-1,-1,-1):
                if m[j]==sorted_m[cnt]:
                    m[j]=m[i]
                    break
            m[i] = sorted_m[cnt]
            return m
 
    return m
 
T=int(input())
 
for i in range(T):
    l=list(input())
    min_answer=''.join(find_min())
    max_answer=''.join(find_max())
 
    print('#{0} {1} {2}'.format((i+1),min_answer,max_answer))
 
 