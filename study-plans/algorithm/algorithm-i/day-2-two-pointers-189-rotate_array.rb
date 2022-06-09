# @param {Integer[]} nums
# @param {Integer} k
# @return {Void} Do not return anything, modify nums in-place instead.
def rotate(nums, k)
  return nums if k == 0
  
  k = k % nums.size
  
  popped = nums.slice!(-k..-1)
  nums.unshift(*popped)
end
