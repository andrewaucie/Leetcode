class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        def findNext(string, lastIndex):
            for i in range(lastIndex-1, -1, -1):
                if string[i] == ".":
                    return i
            return -1
            
        res = []
        freq = defaultdict(int)
        for cpdomain in cpdomains:
            rep, domains = cpdomain.split(" ")
            freq[domains] += int(rep)
            i = domains.rfind(".")
            while i != -1:
                curr = domains[i+1:]
                freq[curr] += int(rep)
                i = findNext(domains, i)
            
        for domain in freq:
            res.append(f"{freq[domain]} {domain}")
        
        return res