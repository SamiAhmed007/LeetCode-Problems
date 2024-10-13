class Solution:
    def __init__(self):
        self.dict={0:0, 1:1, 2:1}
    def tribonacci(self, n: int) -> int:
        # if self.dict is None:
        #     self. = {}
        if n not in self.dict:
            self.dict[n]=self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3);
        return self.dict[n];
        