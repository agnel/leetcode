# Set Matrix Zero
# tags: bca, math, hashing, exam-1
class SetMatrixZero:
    def __init__(self, arr):
        self.arr = arr
        
    def solve(self):
        m = len(self.arr) # rows
        n = len(self.arr[0]) # cols

        rows = set()
        cols = set()

        for i in range(m):
            # if min(self.arr[i]) == 0:
                # rows.add(i) # add row index to set
                for j in range(n):
                    if self.arr[i][j] == 0:
                        rows.add(i)
                    if self.arr[i][j] == 0 and j not in cols:
                        cols.add(j) # add col index to set
        
        for i in rows:
            for j in range(n):
                self.arr[i][j] = 0
        
        for j in cols:
            for i in range(m):
                if i not in rows:
                    self.arr[i][j] = 0

        return self.arr
