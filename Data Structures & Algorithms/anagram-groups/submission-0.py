class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            ana_dict[sorted_s].append(s)
        return [v for v in ana_dict.values()]