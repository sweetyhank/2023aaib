a=12345
ans=0 #用來組合的
while a>0:
  ans= ans*10+ a%10 #ans仙台生10倍，在加個位數的a%10
  print('現在a:',a,'現在a%10',a%10,'現在的ans:',ans)
  a=a//10
print('ans:',ans)