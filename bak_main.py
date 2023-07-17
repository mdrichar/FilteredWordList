import re
def filter_words(word_list, char_list):
    filtered_words = []
    for word in word_list:
        if all(char in char_list for char in word):
            filtered_words.append(word)
    return filtered_words

def get_list():
    word_list = []
    with open("rawwords.txt", "r") as file:
        for line in file:
            word = line.strip().lower()
            if len(word) > 6 and re.match("^[a-z]+$", word):
                word_list.append(word)
    return word_list

def get_filtered_list(letter_set):
    word_list = get_list()
    filtered_word_list = filter_words(word_list, letter_set)
    return filtered_word_list