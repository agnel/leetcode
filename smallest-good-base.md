# [Smallest Good Base](https://leetcode.com/problems/smallest-good-base/description/)

## Using Binary Search

To employ binary search for the "Smallest Good Base" problem, you can focus on finding the base $k$ for a fixed $m$. Here's a structured approach to how you can do this.

### Outline of the Approach

1. **Fix $m$**: Iterate over possible values of $m$ from $2$ to $\lfloor \log_2(n) \rfloor$.

2. **Binary Search for $k$**:
   - For each fixed $m$, perform a binary search on $k$ to find the smallest base that satisfies the equation:

   $$n = \frac{k^{m+1} - 1}{k - 1}$$

   This can be rearranged to:

   $$n(k - 1) = k^{m+1} - 1$$

   Which leads to:

   $$k^{m+1} - nk + n - 1 = 0$$

   This is a polynomial equation in $k$.

3. **Set Up Binary Search**:
   - The search range for $k$ will be from $2$ to $n$.
   - For each candidate $k$, compute the left side of the equation and check if it equals $n$.

### Implementation

Here’s how the code would look with binary search incorporated:

```python
import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_m = int(math.log(n, 2))  # Maximum possible value for m

        for m in range(max_m, 1, -1):
            # Binary search for k
            left, right = 2, n
            
            while left <= right:
                k = (left + right) // 2
                # Calculate the left side of the equation
                left_side = (k**(m + 1) - 1) // (k - 1)
                
                if left_side == n:
                    return str(k)
                elif left_side < n:
                    right = k - 1  # Decrease k
                else:
                    left = k + 1   # Increase k

        return str(n - 1)  # If no valid base found, return n-1
```

### Explanation of the Code

1. **Maximum $m$**: We start by calculating the maximum value of $m$ as before.

2. **Loop Over $m$**: For each value of $m$ from $\lfloor \log_2(n) \rfloor$ down to $2$:

3. **Binary Search**:
   - Initialize the left and right bounds for $k$.
   - While the bounds are valid, compute the middle value $k$.
   - Calculate the left-hand side of the equation using the formula derived earlier.
   - Adjust the search bounds based on whether the left-hand side is equal to, less than, or greater than $n$.

### Complexity Analysis

- **Time Complexity**: 
  - The outer loop runs $O(\log_2(n))$ times for $m$.
  - The inner binary search runs $O(\log_2(n))$ times to find $k$.
  - Overall, the complexity becomes $O(\log^2(n))$.

- **Space Complexity**: 
  - The space complexity remains $O(1)$ since we’re only using a constant amount of space for variables.

### Conclusion

Using binary search allows you to efficiently find the smallest base $k$ for each fixed $m$. While this method has a slightly higher complexity compared to the linear search implementation, it can provide better performance in specific cases or with optimizations.

## Using Linear Search (better than binary search, read to know more)

Let's break down the solution to the "Smallest Good Base" problem step by step, focusing on the mathematical derivations and logic.

### Problem Overview

The goal is to find the smallest integer $k$ such that the number $n$ can be expressed as:

$n = k^m + k^{m-1} + ... + k + 1$

for some integer $m \geq 1$. This sum represents a geometric series.

### Deriving the Formulas

1. **Geometric Series Representation**:
   The sum $n$ can be represented as:

   $$n = k^m + k^{m-1} + ... + k + 1$$

   This is a geometric series where the first term is $1$ and the common ratio is $k$.

2. **Transforming the Equation**:
   From the equation above, we can manipulate it:
   
   $$n - 1 = k^m + k^{m-1} + ... + k$$

   Notice that the right-hand side is again a geometric series, but it can also be factored:

   $$n - 1 = k \cdot (k^{m-1} + k^{m-2} + ... + k + 1)$$

   Thus, we have:

   $$n - 1 = k \cdot \frac{k^m - 1}{k - 1} \quad \text{(from the formula for the sum of a geometric series)}$$

   This gives us an important relationship:

   $$k \cdot (n - k^m) = n - 1$$

   Rearranging, we find:

   $$k^{m+1} - 1 = n k - n$$

   or 

   $$\frac{k^{m+1} - 1}{k - 1} = n \quad \text{(Equation [3])}$$

3. **Divisibility Condition**:
   From the above manipulations, we note that $n - 1$ must be divisible by $k$. This is a key insight that will help us reduce the search space.

### Understanding $m$ and $k$

4. **Range for $m$**:
   We need to find valid values for $m$:
   - Since $n > k^m$, we can deduce that:

   $$k < \sqrt[m]{n}$$

   - Additionally, using the binomial theorem, we can say:

   $$n < (k+1)^m \quad \text{(Equation [5])}$$

   This leads to:

   $$k + 1 > \sqrt[m]{n} > k$$

   Therefore, the only candidate $k$ to check is around $\lfloor \sqrt[m]{n} \rfloor$.

5. **Finding $m$**:
   The maximum value of $m$ can be set to $\lfloor \log_2(n) \rfloor$ because, in the worst case, $k$ could be as small as $2$ (the smallest base) and can lead to the largest $m$.

### Implementing the Code

Now we can implement this logic in the code. We iterate $m$ from $\lfloor \log_2(n) \rfloor$ down to $2$ (since for $m = 1$, the base would just be $n-1$):

1. Calculate $k$ as $\lfloor n^{1/m} \rfloor$.
2. Check if this $k$ satisfies the equation $\frac{k^{m+1} - 1}{k - 1} = n$.

### Complete Code

Here’s the provided implementation:

```python
import math

class Solution(object):
    def smallestGoodBase(self, n):
        n = int(n)
        max_m = int(math.log(n, 2))  # Maximum possible value of m
        for m in range(max_m, 1, -1):
            k = int(n**(1/m))  # Calculate k
            if (k**(m + 1) - 1) // (k - 1) == n:  # Check if it satisfies the condition
                return str(k)
        
        return str(n - 1)  # If no valid base found, return n-1
```

### Conclusion

This approach systematically narrows down the search space for valid bases $k$ and exponent $m$ based on mathematical insights derived from geometric series properties. The complexity is efficient due to logarithmic bounds on $m$, making it feasible for large values of $n$.


## Why the maximum value of 𝑚 can be set to ⌊ log2(𝑛)⌋ ?

The decision to set the maximum value of $m$ to $\lfloor \log_2(n) \rfloor$ comes from understanding the relationship between $n$, $k$, and $m$ in the context of the geometric series representation of $n$.

### Reasoning Behind the Bound on $m$

1. **Geometric Series Representation**:
   We know that $n$ can be expressed as:

   $$n = k^m + k^{m-1} + ... + k + 1$$

   This means that $n$ is the sum of a geometric series. The value of this series grows exponentially with increasing $m$.

2. **Minimum Value of $k$**:
   The smallest base $k$ we consider is $2$. Therefore, for $k = 2$:

   $$n \approx 2^m \quad \text{(for large } m\text{)}$$

   This indicates that as $m$ increases, $n$ must also increase exponentially.

3. **Finding Maximum $m$**:
   To find the maximum $m$ that satisfies this relation with $k = 2$:

   $$n \geq 2^m$$

   Taking the logarithm base 2 of both sides gives:

   $$m \leq \log_2(n)$$

   Thus, the maximum integer value of $m$ that still allows the equation $n = k^m + k^{m-1} + ... + k + 1$ to hold is:

   $$m_{\text{max}} = \lfloor \log_2(n) \rfloor$$

### Summary

- The maximum value of $m$ is derived from the fact that if $m$ were larger than $\lfloor \log_2(n) \rfloor$, the expression $k^m$ (with $k$ being at least 2) would exceed $n$, making it impossible for the equation to hold.
- This logarithmic relationship helps limit the range of $m$ we need to check, allowing for an efficient solution to the problem. 

This reasoning ensures that we are only considering feasible values for $m$ that can realistically correspond to valid bases $k$ such that $n$ can be expressed in the required form.
