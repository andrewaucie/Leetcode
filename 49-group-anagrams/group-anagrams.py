from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            # # get word frequency
            # freq = defaultdict(int)
            # for w in word:
            #     freq[w] += 1
            # # map freq to key
            # # tuple b/c list is unhashable
            # # sorted b/c list could be different order, maintains O(1) b/c |freq| <= 26
            # key = tuple(sorted(freq.items()))
            # res[key].append(word)
            res[tuple(sorted(Counter(word).items()))].append(word)
        return [res[counter] for counter in res]