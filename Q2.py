#  Read all lines from a file into a list. Print the total numbers of lines and display the 2nd and 4th line


with open("sample.txt", "r") as f:
    li1 = f.readlines()
    print(li1)

    print("Total Lines in file Sample.txt :", len(li1))
    print("2nd Line :", li1[1])
    print("4th Line :", li1[3])
