import string

class Answer:
    def mostCommonWord(self, paragraph, banned):
        # Lowercase the whole paragraph so "BALL" and "ball" count as the same word
        paragraph = paragraph.lower()

        # Strip punctuation: replace each punctuation mark with a space
        # so "ball," becomes "ball " and "hit." becomes "hit "
        for char in string.punctuation:
            paragraph = paragraph.replace(char, " ")

        # Split into a list of words (no-argument split handles extra spaces)
        words = paragraph.split()

        # Count how many times each word appears (same tally pattern as Valid Anagram)
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        # Find the most frequent word that isn't banned
        max_word = ""
        max_count = 0
        for word, count in word_count.items():
            if word not in banned and count > max_count:
                max_word = word
                max_count = count

        return max_word


solution = Answer()
print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
    
                