# 768. Max Chunks To Make Sorted II
# Ref: https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
# tags: bca, day-3, assignment
# Solution Ref: https://leetcode.com/problems/max-chunks-to-make-sorted-ii/solutions/1498733/easy-to-understand-98-faster-well-explained
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        st = []

        for n in arr:
            # Each time we encounter a arr[i] i.e. n
            # that is bigger than or equal to 
            # the previous chunk max, we push
            # it to the stack.
            if len(st) == 0 or st[-1] <= n:
                st.append(n)
            # If we encounter a smaller number, 
            # we must combine this number with 
            # the previous chunks. 
            else:
                # We do this by comparing with 
                # the top chunk in the stack and
                # popping them off until we
                # encounter a chunk with max
                # number that is smaller than arr[i] i.e. n.
                m = st[-1]
                # the condition st and ... checks
                # if the st is not empty due continual
                # popping of elements
                while st and st[-1] > n:
                    m = max(m, st.pop())
                
                # Then, we update the new combined
                # chunk with the new max by pushing
                # it back onto the stack. 
                st.append(m)

        # The number of elements in this stack at the
        # end is the number of chunks.
        return len(st)
