# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def intersect(nums1, nums2)
  nums1, nums2 = nums2, nums1 if nums1.size > nums2.size
  
  answer = []
  nums1.size.times do |i|
    idx_in_nums2 = nums2.find_index(nums1[i])
    if not idx_in_nums2.nil?
      answer.push(nums1[i])
      nums2.delete_at(idx_in_nums2)
    end
  end
  
  answer
end
