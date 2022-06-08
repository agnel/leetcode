# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search_insert(nums, target)
  low = 0
  high = nums.size - 1
  
  while low <= high
    mid = (high + low) / 2 # dividing here returns floor value already
    
    if nums[mid] < target
      low = mid + 1
    elsif nums[mid] > target
      high = mid - 1
    else
      return mid
    end
  end
  
  target < nums[mid] ? mid : mid + 1
end
