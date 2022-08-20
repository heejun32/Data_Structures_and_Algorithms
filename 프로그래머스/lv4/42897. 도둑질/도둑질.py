def solution(nums):
    answer = 0
    
    if len(nums) <= 2:
        return max(nums)
    
    def simple_rob(nums):
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            
        return dp[-1]
        
    return max(simple_rob(nums[1:]), simple_rob(nums[: -1]))