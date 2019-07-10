n,u=input().split()
n = int(n)
u = int(u)
a = []
for num in range(n,u):
   summ = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       summ += digit ** 3
       temp //= 10
 
   if num == summ:
       a.append(str(summ))
print(" ".join(a))
