# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
  hash = {}
  nums.each_index do |i|
    complement = target - nums[i]
    return [hash.fetch(complement), i] if hash.has_key?(complement)
    hash[nums[i]] = i
  end
end
