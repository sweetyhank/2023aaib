s='00111'
N=len(s)#長度
zero=0#等一下也要
one=0#想找出全部的1
for i in range(N):
  if s[i]=='1':one+=1#如果是1，先全部加起來  
print('一開始的時候，都在右邊，統計結果','zero',zero,'one',one)
ans=0
for i in range(N-1):
  if s[i]=='0':
    zero+=1
  if s[i]=='1':
    one-=1
  print('中間過程中''zero',zero,'one',one)
  ans = max(ans,zero+one)
print('答案出來了',ans)