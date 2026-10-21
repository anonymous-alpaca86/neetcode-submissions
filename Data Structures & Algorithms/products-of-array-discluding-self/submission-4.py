class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        lst=[]
        product=1
        for num in nums:
            if num!=0:
                product*=num
        if 0 in nums:
            for num in nums:
                if num==0:
                    lst.append(product)
                else:
                    lst.append(0)
        else:
            for num in nums:
                lst.append(int(product/num))
        return lst
        """
        lst=[0]*len(nums)

        left=1
        for i in range(len(nums)):
            lst[i]=left
            left*=nums[i]
        right=1
        for i in range(len(nums)-1,-1,-1):
            lst[i]*=right
            right*=nums[i]
        return lst
            

            