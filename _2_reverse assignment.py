# #
# Word = input("Input a word to revers:  " )

# for char in range(len(Word) -1,-1,-1):
#     print(Word[char], end="")
# print("\n")



str1 = input("enter the sentence: ")
words = str1.split()
reversed_str1= []
for i in words:
    reversed_str1.append(i[::-1])
print(reversed_str1)

