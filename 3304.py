def dp():
 
    for p in range(1,len(answer)):
        for q in range(1,len(answer[0])):
            if st[0][p-1]==st[1][q-1]:
                answer[p][q]=answer[p-1][q-1]+1
            else:
                answer[p][q]=max(answer[p-1][q],answer[p][q-1])
    return
 
T=int(input())
 
for i in range(T):
    st=list(input().split())
    answer=[[0]*(len(st[1])+1) for _ in range(len(st[0])+1)]
    dp()
    print('#{} {}'.format((i+1),answer[-1][-1]))