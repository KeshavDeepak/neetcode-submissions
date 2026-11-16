class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = dict()

        for string in strs:
            # build the current grouping
            curr_grouping = [0] * 26

            for char in string:
                curr_grouping[ord(char)-ord('a')] += 1
            
            curr_grouping = tuple(curr_grouping)

            # find in groupings
            if curr_grouping in groupings:
                groupings[curr_grouping].append(string)
            else:
                groupings[curr_grouping] = [string]
        
        return list(groupings.values())