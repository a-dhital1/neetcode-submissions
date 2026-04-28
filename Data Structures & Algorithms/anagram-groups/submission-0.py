class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if not strs:
            return strs

        ana_hash = defaultdict(list)

        for s in strs:
            count_list = [0] * 26
            for c in s:
                count_list[ord(c) - ord('a')] += 1
            ana_hash[tuple(count_list)].append(s)
        return list(ana_hash.values())
