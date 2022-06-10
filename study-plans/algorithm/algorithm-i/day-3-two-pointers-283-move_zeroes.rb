# @param {Integer[]} nums
# @return {Void} Do not return anything, modify nums in-place instead.
def move_zeroes(nums)
  return nums if nums.size == 1
  
  last = -1 # index pointing to last found non-zero value
  nums.size.times do |i|
    if nums[i] != 0
      nums[last + 1], nums[i] = nums[i], nums[last + 1]
      last += 1
    end
  end
  
  nums
end
