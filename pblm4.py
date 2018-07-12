def rev(m):
  rev = 0
  d = m
  while(m>0):
    rev *= 10
    rev += m%10
    m = int(m/10)
  if d== rev:
    return 1
  else:
    return 0

c=[]
for i in range(999,99,-1):
  for j in range(999,99,-1):
    if(rev(i*j)):
      c.append(i*j)
      break
print(max(c))
