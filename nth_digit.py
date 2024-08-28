# Nth Digit
# tags: bca, math, binary search, exam-1
class NthDigit:
    def __init__(self, n):
        self.n = n
        
    def solve(self):
        i = 1
        s = ''
        while len(s) <= self.n:
            s = f"{s}{i}"
            i += 1
        return s[self.n - 1]
