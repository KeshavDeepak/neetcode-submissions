from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build a frequency map
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1
        
        # push everything into min-heap while maintaining size of k
        heap = []

        for num, freq in freqs.items():
            heapq.heappush(heap, (freq, num))
        
            if len(heap) > k:
                heapq.heappop(heap)
        
        # remaining whatever is in heap is the answer
        answer = []

        while heap:
            answer.append(heapq.heappop(heap)[1])
        
        #
        return answer