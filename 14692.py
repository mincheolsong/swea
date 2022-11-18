def solve(n):
    if n%2==0:
        return 'Alice'
    else:
        return 'Bob'
 
 
N=int(input())
 
for i in range(N):
    num = int(input())
    print('#'+str(i+1)+' '+ solve(num))