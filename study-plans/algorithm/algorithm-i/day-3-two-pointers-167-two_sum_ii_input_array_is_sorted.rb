# @param {Integer[]} numbers
# @param {Integer} target
# @return {Integer[]}
def two_sum(numbers, target)
  left = 0 # left pointer
  right = numbers.size - 1 # right pointer
  
  while numbers[left] + numbers[right] != target
    if numbers[left] + numbers[right] > target
      right -= 1 
    else
      left += 1
    end
  end
  
  [left + 1, right + 1]
end

=begin
few test cases

[2,7,11,15]
9
[2,3,4]
6
[-1,0]
-1
[5,25,75]
100

=end
