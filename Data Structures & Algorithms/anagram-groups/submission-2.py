from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = defaultdict(list)

        for string in strs:
            # build the current grouping
            curr_grouping = [0] * 26

            for char in string:
                curr_grouping[ord(char)-ord('a')] += 1
            
            curr_grouping = tuple(curr_grouping)

            # add to groupings
            groupings[curr_grouping].append(string)
        
        return list(groupings.values())