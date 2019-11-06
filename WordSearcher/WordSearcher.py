import re
import time
start = time.time()

counter = 0
characters_to_search_string = "pterodaptylpterodaptyl"
characters_to_search_string = characters_to_search_string.lower()
line_length = 7

result_output_file = open("results.txt", "w")

characters_to_search_tuple = tuple(characters_to_search_string)
characters_to_search = list(characters_to_search_tuple)


# word_list_to_read = open("short_english.txt", "r")
word_list_to_read = open("words_alpha.txt", "r")

for line in word_list_to_read.readlines():
    line = line.strip('\n')
    characters_to_search = list(characters_to_search_tuple)
    if any(x in line for x in characters_to_search) and len(line) == line_length:
        for line_character in line:
            continue_flag = 0
            try:
                characters_to_search_index = characters_to_search.index(line_character)
                characters_to_search.pop(characters_to_search_index)
            except:
                continue_flag = 1
                break

        if continue_flag == 0:
            print(line, "\t", len(line), file=result_output_file)
            print(line, "\t", len(line))
            counter = counter + 1
print("Number of matching words is:", counter)
print("Number of matching words is:", counter, file=result_output_file)


word_list_to_read.close()
end = time.time()
print("Time taken:", end - start)
print("Time taken:", end - start, file=result_output_file)
result_output_file.close()

#pyinstaller --onefile --add-data C:\LearnPython\venv\Scripts\WordSearcher\toAdd;. WordSearcher.py