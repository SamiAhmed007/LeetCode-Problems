class RecentCounter:

    def __init__(self):
        self.counter = 0 
        self.request = []

    def ping(self, t: int) -> int:
        self.request.append(t)
        while self.request[0] < t-3000: 
            self.request.pop(0)
        return len(self.request)

        # self.counter = 0 
        # self.request.append(t)
        # diff = t - (t-3000)
        # for i in self.request:
        #     if i in range(t-3000,t+1):
        #         self.counter+=1
        # return self.counter



        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


    # -2999 to 1
    # -2900 to 100