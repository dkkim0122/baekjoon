# https://leetcode.com/problems/group-anagrams

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for word in strs:
            dict[''.join(sorted(word))].append(word)

        return list(dict.values())
    