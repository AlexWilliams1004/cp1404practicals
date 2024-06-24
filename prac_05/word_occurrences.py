"""
CP1404/CP5632 Practical 5
Word Occurrences
Alex Williams

Estimate: 15 minutes
Actual: 30
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

word_to_count = dict(sorted(word_to_count.items()))

for word, count in word_to_count.items():
    longest_word = max(len(word) for word in word_to_count.keys())
    print(f"{word:{longest_word}} : {count}")
