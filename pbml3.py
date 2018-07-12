def prime(n):
  c = []
  while n%2==0:
    c.append(2)
    n /= 2
  for i in range(3,n**(1/2.0),2):
    if n%i==0:
      c.append(i)
      n = int(n/i)
  if n>2 :
    c.append(n)
  return c

a = prime(600851475143)
print(max(a))
    
