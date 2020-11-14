#Write a Python program to count the frequency of words in a file.
wordcount = {}
from collections import Counter
with open("./file.txt", "r") as f_content:
    wordcount = Counter(f_content.read().split())

print(wordcount)