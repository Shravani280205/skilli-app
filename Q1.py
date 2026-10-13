# 1.  Write a program to read a file and count how many vowels are present in its content.

count = 0
with open("sample.txt", "r") as f:
    contents = f.read()

    for ch in contents:
        if ch.lower() in "aeiou":
            count += 1
        
print("Total Vowels :", count)