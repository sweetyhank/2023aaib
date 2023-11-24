a=2541215
b=21520431
def gcd(a, b):
  print(a, b)
  if a==0: return a
  if b==0: return b
  return gcd(b, a%b)

ans=gcd(a, b)
print(ans)