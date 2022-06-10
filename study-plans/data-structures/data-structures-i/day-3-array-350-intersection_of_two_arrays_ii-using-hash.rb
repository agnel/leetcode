# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def intersect(nums1, nums2)
  nums1, nums2 = nums2, nums1 if nums1.size > nums2.size
  
  hash1, hash2 = {}, {}
  
  for i in nums1
    if hash1.has_key?(i)
      hash1[i] += 1
    else
      hash1[i] = 1
    end
  end
  
  for j in nums2
    if hash2.has_key?(j)
      hash2[j] += 1
    else
      hash2[j] = 1
    end
  end
  
  answer = []
  for k in hash1.keys
    answer += [k] * [hash1[k], hash2[k]].min if hash2.has_key?(k)
  end
  
  answer
end
