# import sys
# input = sys.stdin.readline
import decimal
from collections import Counter, deque
from itertools import permutations, combinations


def show():
    for p in l:
        for q in p:
            print(q, end=' ')
        print()

    print('----------')
    return


def check(row, col):
    for r in range(row - 1, -1, -1):
        if abs((col - l[r].index(1)) / (row - r)) == 1:
            return False

    return True


def backTracking(e):
    global answer

    if e == N:
        answer += 1

    for i in range(N):
        if visited[i] == False and check(e, i):
            l[e][i] = 1
            visited[i] = True
            #show()
            backTracking(e + 1)
            l[e][i] = 0
            visited[i] = False

    return


T = int(input())

for i in range(T):
    N = int(input())
    l = [[0] * N for _ in range(N)]
    visited = [False] * N  # 열 방향 체크리스트
    answer = 0
    backTracking(0)
    print('#{} {}'.format((i+1),answer))
