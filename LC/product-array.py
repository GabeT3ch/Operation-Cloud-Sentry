class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left = []
        right = [0] * n
        answer = []

        # Left pass: running product of everything to the left
        product = 1
        for i in range(n):
            left.append(product)
            product = product * nums[i]

        # Right pass: running product of everything to the right
        product = 1
        for i in range(n - 1, -1, -1):
            right[i] = product
            product = product * nums[i]

        # Combine
        for i in range(n):
            answer.append(left[i] * right[i])

        return answer


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]