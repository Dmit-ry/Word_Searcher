import re
import time

word_list_to_read = open("C:/LearnPython/venv/Scripts/WordSearcher/words_alpha.txt", "r")
lineList = [line.rstrip('\n') for line in word_list_to_read]
longestWord = max(lineList, key=len)

print (longestWord, len(longestWord), len(lineList))
print(lineList[100000])