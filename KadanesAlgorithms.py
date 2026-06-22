# Brute force : O(n^2)

def bruteForce(nums):
    maxSum = nums[0]  # initialize our maxSum to the first index of nums array

    for i in range(len(nums)): # for each index in nums
        curSum = 0 # initialize our current number to 0, so it will always be larger than negivative numbers
        for j in range(i, len(nums)): # setup the second pointer
            curSum += nums[j] # add our current with the second pointer
            maxSum = max(maxSum, curSum) # set for the max
    return maxSum

listNum = [4,-1,2,-7,3,4]
print(bruteForce(listNum))



# Kadane's Algorithm : O(n)

def kadanes(nums):
    maxSum = nums[0] # initialize our maxSum to the first index of nums array
    curSum = 0 # initialize our current num

    for n in nums: # for each index in nums
        curSum = max(n, curSum + n) # set the max for the curSum
        maxSum = max(maxSum,curSum) # set the max for the maxSum
    return maxSum


# Return the left and right index of the max subarray sum
# assuming there's exactly one result (no ties).
# sliding window variation of Kadane's :  O(n)

def slidingWindow(nums):
    maxSum = nums[0] # initialize our maxSum to be the first index of nums array
    curSum = 0 # initialize our current num to zero
    maxL,maxR = 0,0 # initialize the left max and the right max
    L = 0 # initialize the left

    for R in range(len(nums)): # for each index in nums
        if curSum < 0: # if the current sum is less than zero
            curSum = 0 # we set curSum equal to zero
            L = R 

        curSum += nums[R] # add index of that number into curSum
        if curSum > maxSum: # if our cur number is greater than the max number, then we want to set our max to curSum
            maxSum = curSum
            maxL, maxR = L,R
    
    return [maxL,maxR]