# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
  counts = {}
  nums.each do |n|
    if counts.has_key?(n)
      counts[n] += 1
      break
    else
      counts[n] = 1
    end
  end
  counts.values.any?{ |n| n > 1 }
end

# Runtime: 164 ms, faster than 49.62% of Ruby online submissions for Contains Duplicate.
# Memory Usage: 218.8 MB, less than 70.87% of Ruby online submissions for Contains Duplicate.
