class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        count = Counter(nums) #dicatnary
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
            
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                
        return result[:k]
