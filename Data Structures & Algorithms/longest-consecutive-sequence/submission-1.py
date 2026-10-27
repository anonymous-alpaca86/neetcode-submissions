class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNum=set(nums)
        result=0
        for num in setNum:
            if num-1 not in setNum:
                pointer=num
                length=1
                consec=True
                while consec==True:
                    if pointer+1 in setNum:
                        length+=1
                        pointer=pointer+1
                    else:
                        consec=False
                if length>result:
                    result=length
        return result

        





            
            


