class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0]*len(nums)
        post = [0]*len(nums)
        res = [0]*len(nums)
        for i in range(len(nums)):
            if (i == 0):
                pre[i] = nums[0] 
                post[-1] = nums[-1]
            else:
                pre[i] = nums[i] * pre[i-1]
                post[-i-1] = nums[-i-1] * post[-i]
        # print(pre)
        # print(post)
        for i in range(len(nums)):
            if(i==0):
                res[i] = 1*post[i+1]
            elif(i==len(nums)-1):
                res[i] = pre[i-1]*1
            else:
                res[i] = pre[i-1]*post[i+1]
        return res


