class Solution:
    def hammingWeight(self, n: int) -> int:
        ans=0 #迴圈前面ans=0
        while n>0: #剝皮法 依次剝一層皮(第7周)
            ans += n%2 #剝下來的屑屑，收集起來
            n=n//2 #洋蔥剝皮法後,變小了
        return ans #迴圈後面 ans拿來用ED