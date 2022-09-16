#Write a Python program that accepts a word from the user and reverse it.

Word = input("Input a word to reverse:  " )

for char in range(len(Word) -1,-1,-1):
    print(Word[char], end="")
print("\n")




