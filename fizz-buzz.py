# 412. Fizz Buzz
# Ref: https://leetcode.com/problems/fizz-buzz/
# tags: bca, day-2, assignment
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                answer.append("FizzBuzz")
            elif i % 5 == 0:
                answer.append("Buzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            else:
                answer.append(str(i))

        return answer
