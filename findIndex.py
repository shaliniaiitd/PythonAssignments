txt = "the quick brown fox jumps over the lazy dog"
# txt = "The quick brown fox jumps over the lazy dog"
str1 = "the"

first_match = txt.find(str1)
second_match = txt.find(str1, first_match+1)
print("Search first_match:", first_match)
print("Search second_match:", second_match)  # 31 or -1

first_match = txt.index(str1)
print("Search first_match:", first_match)
second_match = txt.index(str1, first_match+1)
print("Search second_match:", second_match)  # 31 or ValueError: substring not found