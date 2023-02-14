# Cloud Computing - Project #3: Docker

import socket
import functions

# 4a: List name of all the text file at location
dir_path = "./data"
txt_files_list = functions.get_txt_files(dir_path)

# 4b: Read the two text files and count total number of words in each text files
txt_path_1 = "./data/Limerick.txt"
txt_path_2 = "./data/IF.txt"
word_count_1 = functions.word_count(txt_path_1)
word_count_2 = functions.word_count(txt_path_2)

# 4c: Add all the number of words to find the grand total (total number of words in both files)
grand_count = word_count_1 + word_count_2

# 4d: List the top 3 words with maximum number of counts in "IF.txt." Include the word counts for the top 3 words.
top_three_words = functions.top_three_words(txt_path_2)

# 4e: Find the IP address of your machine
ip_addr = functions.get_ip_addr(socket.gethostname())

# 4f: Write all the output to a text file at location
output_file = open("./output/result.txt", "w+")

output_file.write("List of all text files:\n")
for file in txt_files_list:
    output_file.write(file + "\n")
output_file.write("\n")

output_file.write("Word Count of File 1: " + str(word_count_1) + "\n")
output_file.write("Word Count of File 2: " + str(word_count_2) + "\n")
output_file.write("Word Count of Both Files: " + str(grand_count) + "\n")
output_file.write("\n")

output_file.write("Top Three Words of File 2 and Their Count:\n")
for word in top_three_words:
    output_file.write(word[0] + ", " + str(word[1]) + "\n")
output_file.write("\n")

output_file.write("IP Address of Machine: " + ip_addr + "\n")

output_file.close()
output_path = "./output/result.txt"

# 4g: Upon running your container, it should do all the above stated steps and print the information on console from
#     result.txt file and exit
functions.print_results(output_path)
