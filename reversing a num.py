class Solution:
    def __init__(self, target, nums=[]):
        self.nums = []
        self.target = target

    def add_nums(self):
        while True:
            y = input("Enter a no.: ")
            if y == "Stop":
                break
            self.nums.append(int(y))
        return self.nums

    def target(self):
        for i in self.nums:
            for j in self.nums:
                if i + j == self.target:
                    return [self.nums[i], self.nums[j]]


a = Solution(9)
