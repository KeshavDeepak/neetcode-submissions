from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build a frequency map
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1
        
        # push nums into buckets
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in freqs.items():
            buckets[freq].append(num)
        
        # go through in reverse to find answer
        answer = []

        for i in range(len(buckets)-1, -1, -1):
            answer.extend(buckets[i][:k-len(answer)])

            if len(answer) >= k:
                break

        #
        return answer