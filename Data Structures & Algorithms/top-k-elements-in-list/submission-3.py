class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1

        buckets=[[] for _ in range(len(nums)+1)]
        for key, value in d.items():
            buckets[value].append(key)
        result=[]
        for freq in range(len(nums)+1):
            result.extend(buckets[freq])
        return result[-k:]
        