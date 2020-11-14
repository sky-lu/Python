#Write a python program to find the longest words
def longest_word(filename):
    with open(filename,"r") as f_content:
        words = f_content.read().split()
    max_len = max(len(w) for w in words)
    
    return [word for word in words if len(word) == max_len]
print(longest_word('./file.txt'))