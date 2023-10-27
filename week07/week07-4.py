#1 2 4 8 16 32 64
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #如果n是負的,就錯了
        if n<=0: return False
        while n>1 : #因為1是2的0次方
            if n%2 !=0: #竟然餘數不是0
                return False
            n=n//2
        #經過樓上的檢查,都沒有出錯的話
        return True   #就是成功 