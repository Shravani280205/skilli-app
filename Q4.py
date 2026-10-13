# Read a file , split it contents into word and store them in a list.
# i. Print total  number of words.
# ii. Print all unique words.

with open("sample.txt", "r") as f:
    contents = f. read()

words = contents.split()
print("Total Number of words :", len(words))
unique_word = set(words)
print("Unique Word :", unique_word)