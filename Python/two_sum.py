'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Constraints:

    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.

'''


class Solution:

    # INPUT
    #   nums: a list of integers
    #   target: the number (int) sum that we want
    # OUTPUT
    #    
    def twoSum_test(self, nums, target):
        
        index_list = [0, 1]
        n = len(nums)

        print("target:", target)

        # i = 0
        # found = False
        # while (~found) and (i < n):
        #   # print(nums[i])

        #   i += 1


        iteration = 0
        found = False
        for i in range (0, n):
            if (found == True):
                break
            else:
                # print ("i =", i)
                for j in range (i+1, n):
                    # print ("\tj =", j)
                    val = nums[i] + nums[j]

                    iteration += 1
                    print(iteration, val)

                    if (val == target):
                        # print("break!")
                        found = True
                        index_list = [i, j]
                        break
                        # print(i, j)
                        # print(nums[i] + nums[j])

        return index_list

    def twoSum2(self, nums, target):
        
        # index_list = [0, 1]
        n = len(nums)

        # found = False
        for i in range (0, n):
            # if (found == True):
            #     break
            # else:
            for j in range (i+1, n):
                val = nums[i] + nums[j]
                if (val == target):
                    # found = True
                    index_list = [i, j]
                    # break
                    return index_list

        # return index_list


    # LeetCode Submission
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range (0, n):
            for j in range (i+1, n):
                val = nums[i] + nums[j]
                if (val == target):
                    return [i, j]



soln = Solution()

nums = [2, 11, 15,-1, -3, 5, 7]
target = 9

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6

# index_list = soln.twoSum_test(nums, target)
# print(index_list)



# FINAL ANSWER

nums = [2,7,11,15]
target = 9
print(soln.twoSum(nums, target))

nums = [3,2,4]
target = 6
print(soln.twoSum(nums, target))

nums = [3,3]
target = 6
print(soln.twoSum(nums, target))

