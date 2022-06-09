**Logic**

We'd like to attempt this question in-place because all the space we need is already provided by our first array; there's no need to create extra space. We'd like to use a two-pointer approach but it can get quite messy dealing with certain cases. Since our extra space starts at the end of the first array, let's see if we can do this by iterating backwards!

**Three Pointers:**
Let's use three pointers for this operation:

* The main pointer, `i`, will be starting from the end of the first array and will work its way to index 0.
* The pointer for the first array, `a`, and;
* The pointer for the second array, `b`, will be used for comparing the two sorted arrays and deciding what value to place at `i` next.

We'll decide which value at index `a` or `b` is larger, place that value at index `i`, and decrement either `a` or `b` depending on which was larger. This sounds a bit confusing so I've illustrated below how this would work with two example arrays:

![Visual Explanation](https://imgur.com/d3pc86I.png)

I hope the above illustration sufficiently details the three pointer approach. In summary, we compare two values, pick the larger one, and move to the next comparison. The reason we move the pointer of the larger value is because we already know that that number is larger than (or equal to) ANY number that comes before it. So we can confidently place it at `i` and move on.

---

**But won't some values at array `A` be overridden by the main pointer?**

Good question! Yes you're right; our `i` pointer will eventually land at values of `A` that are non-zero. Is this a problem? Turns out it isn't. This is because we're guaranteed to have already used those values at `A` before they become overridden. Think about it like this:

`A` is of length `m+n`. All our meaningful values are the first `m` values. This means that the last `n` values are empty. Therefore, our `i` pointer needs to process the `nth` largest numbers in both arrays before overriding values at `A`. It's not possible for `i` to override any unused values of `A` by the time it reaches `A`.

Let's consider the two extremes:

* If the `nth` largest values are all at `A`, our pointer `a` pointer will be moving with `i` so there's no issues there.
* If the `nth` largest values are all at `B`, then our `b` pointer will trigger our exit condition `"b >= 0"` since our `b` pointer would be negative eventually. Therefore, `i` won't get a chance to override values at `A`.

If this all sounds a bit confusing, don't worry about it! Took me a while to get this explanation in order and if your interviewer expects you to spit this out in an interview, they don't want to hire you haha.

Another important point is the condition `a >= 0` indicates that there are no elements in `A` or `nums1` array if it fails.

**Time Complexity:** `O(n+m)`
**Space Complexity:** `O(1)`
