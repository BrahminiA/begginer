def multiple(m, n):
    a = range(n, (m * n)+1, n) 
    print(*a) 
m = 5
n = int(input())
multiple(m, n) 
