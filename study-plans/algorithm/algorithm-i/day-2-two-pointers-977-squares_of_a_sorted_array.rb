# @param {Integer[]} nums
# @return {Integer[]}
def sorted_squares(nums)
  ans = [] # final sorted squares; ans means answer
  
  # using the three pointer approach
  # just like the problem in Data Structure I
  # 88. Merge Sorted Array
  
  start_idx = 0
  end_idx = nums.size - 1
  ans_idx = nums.size - 1 # similar to i in problem 88
  
  while start_idx <= end_idx
    if nums[start_idx]**2 > nums[end_idx]**2
      ans[ans_idx] = nums[start_idx]**2
      start_idx += 1
    else
      ans[ans_idx] = nums[end_idx]**2
      end_idx -= 1
    end
    ans_idx -= 1
  end
  
  ans
end
