# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def intersect(nums1, nums2)
  if nums1.size < nums2.size
    left, right = nums1, nums2
  else
    left, right = nums2, nums1
  end
  
  answer = []
  left.size.times do |i|
    idx_in_right = right.find_index(left[i])
    if not idx_in_right.nil?
      answer.push(left[i])
      right.delete_at(idx_in_right)
    end
  end
  
  answer
end
