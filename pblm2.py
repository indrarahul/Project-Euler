def fib(n):
  if n==1:
    return 1
  if n==2:
    return 2
  else:
    return fib(n-1)+fib(n-2)
    
sum = 0
c= []
for i in range(1,34):
  if fib(i) > 4000000:
    break
  else
    c.append(fib(i))
   
for i in c:
  if i%2 == 0:
    sum+= i

print(sum)
