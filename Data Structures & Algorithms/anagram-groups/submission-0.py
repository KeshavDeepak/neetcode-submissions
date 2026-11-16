class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = dict()

        for string in strs:
            curr_group = tuple(sorted(string))

            if curr_group in groupings:
                groupings[curr_group].append(string)
            else:
                groupings[curr_group] = [string]
        
        return list(groupings.values())