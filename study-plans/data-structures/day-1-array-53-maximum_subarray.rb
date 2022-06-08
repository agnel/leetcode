# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)
  largest_sum = nums[0]
  current_sum = nums[0]
  
  1.upto(nums.size - 1) do |i|
    current_sum = [current_sum + nums[i], nums[i]].max
    largest_sum = [current_sum, largest_sum].max
  end
  
  largest_sum
end
