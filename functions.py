import os
import socket


def get_txt_files(path):
    files = []
    for file in os.listdir(path):
        if file.endswith(".txt"):
            files.append(file)

    return files


def word_count(txt_file):
    count = 0
    file = open(txt_file, "r")
    contents = file.read()
    lines = contents.split()
    count += len(lines)
    file.close()

    return count


def top_three_words(txt_file):
    word_frequencies = {}
    file = open(txt_file, "r")

    # Count the frequencies of each word
    for line in file:
        for word in line.split():
            if word.lower() in word_frequencies:
                word_frequencies[word.lower()] += 1
            else:
                word_frequencies[word.lower()] = 1

    # Sort dictionary
    sorted_word_frequencies = sorted(word_frequencies.items(), key=lambda x: x[1])

    top_three = [sorted_word_frequencies[-1], sorted_word_frequencies[-2], sorted_word_frequencies[-3]]
    return top_three


def get_ip_addr(hostname):
    return socket.gethostbyname(hostname)


def print_results(txt_file):
    results_file = open(txt_file, "r")
    result_lines = results_file.readlines()

    for line in result_lines:
        print(line)

    results_file.close()
