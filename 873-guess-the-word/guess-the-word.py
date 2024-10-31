class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        place_counts = defaultdict(lambda: defaultdict(int))
        for word in wordlist:
            for i, char in enumerate(word):
                place_counts[i][char] += 1
        
        def word_uniqueness(word):
            score = 0
            for i, char in enumerate(word):
                score += place_counts[i][char]
            return score
        
        # wordlist will be sorted from most to least unique.
        wordlist.sort(key=word_uniqueness)
        
        def word_is_possible(guess_word, word, matches):
            if guess_word == word:
                return False
            match_count = 0
            for a, b in zip(guess_word, word):
                if a == b:
                    match_count += 1
            return match_count == matches
        while True:
            guess_word = wordlist[-1]
            matches = master.guess(guess_word)
            if matches == 6:
                break
            elif matches == 0:
                wordlist = [w for w in wordlist if not any(a==b for a, b in zip(guess_word, w))]

            else:
                wordlist = [w for w in wordlist if word_is_possible(guess_word, w, matches)]
