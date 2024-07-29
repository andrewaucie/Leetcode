class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        g = [[] for _ in range(26)]
        in_degree = {}
        for w in words:
            for c in w: in_degree[ord(c) - ord("a")] = 0
        
        for i in range(1, n):
            w1, w2 = words[i - 1], words[i]
            j = 0
            while j < len(w1) and j < len(w2):
                w1_idx, w2_idx = ord(w1[j]) - ord("a"), ord(w2[j]) - ord("a")
                if w1_idx != w2_idx:
                    g[w1_idx].append(w2_idx)
                    in_degree[w2_idx] += 1
                    break
                j += 1
            if j == len(w2) and j < len(w1): return ""
        
        pq = collections.deque()
        for i in in_degree:
            if in_degree[i] == 0: pq.append(i)
        
        res = []
        while pq:
            cur = pq.popleft()
            res.append(chr(cur + ord("a")))
            for nxt in g[cur]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0: pq.append(nxt)
        return "".join(res) if sum(in_degree.values()) == 0 else ""