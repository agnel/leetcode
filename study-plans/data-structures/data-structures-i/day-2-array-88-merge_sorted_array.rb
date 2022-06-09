# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.
def merge(nums1, m, nums2, n)
  return nums1 if n == 0

  i = m + n - 1
  a = m - 1
  b = n - 1
  
  while b >= 0
    if a >= 0 && nums1[a] > nums2[b]
      nums1[i] = nums1[a]
      a -= 1
    else
      nums1[i] = nums2[b]
      b -= 1
    end
    i -= 1
  end
    
  nums1
end
