class Solution:
    def minSteps(self, s: str, t: str) -> int:
        char_set = list(set(s))
        over = 0
        under = 0
        miss_match = 0
        seen_in_t = 0
        for char in char_set:
            s_count = s.count(char)
            if char in t:
                t_count = t.count(char)
                seen_in_t += t_count
                if t_count > s_count:
                    over += t_count - s_count
                elif t_count < s_count:
                    under += s_count-t_count
        miss_match += abs(seen_in_t-len(t))
        moves= 0
        if over > under:
            moves += under
            moves += miss_match
            moves += (over-under)
        else:
            moves += over
            moves += miss_match
        return moves