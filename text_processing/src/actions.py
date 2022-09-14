from statistics import mode
import datetime
import os
import json


def get_text_length(content):
    return len(content)


def get_words_count(content):
    return len(content.split())


def get_word_occurrences(content):
    while True:
        word_to_check_occurrences = input("Input a word to count: ")
        if word_to_check_occurrences == "":
            print("You need to introduce the word you want to check! Please input the word again!")
            continue
        return word_to_check_occurrences, content.count(word_to_check_occurrences)


def get_letter_occurrences(content):
    while True:
        letter_to_check_occurrences = input("A letter to check: ")
        if letter_to_check_occurrences == "":
            print("You need to introduce the letter you want to check! Please input the letter again!")
            continue
        if len(letter_to_check_occurrences) > 1:
            print("You need to input ONLY ONE letter! Please introduce the letter again!")
            continue
        return letter_to_check_occurrences, content.count(letter_to_check_occurrences)


def get_most_frequent_word(content):
    words_list = content.split()
    return mode(words_list)


def get_least_frequent_word(content):
    words_list = content.split()
    frequency = {}
    for word in words_list:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    min_key = words_list[0]
    min_value = frequency[min_key]
    for key, value in frequency.items():
        if value < min_value:
            min_value = value
            min_key = key
    return min_key


def get_text_in_reverse(content):
    return content[::-1]


def export_data_to_file(content):
    all_actions_dictionary = {}
    # 1
    all_actions_dictionary["1. file length"] = get_text_length(content)
    # 2
    all_actions_dictionary["2. number of words in the file"] = get_words_count(content)
    # 3
    word, occurrences = get_word_occurrences(content)
    all_actions_dictionary[f'3. occurrences of "{word}"'] = occurrences
    # 4
    letter, occurrences = get_letter_occurrences(content)
    all_actions_dictionary[f'4. occurrences of "{letter}" letter'] = occurrences
    # 5
    all_actions_dictionary["5. the most frequent word in the file"] = get_most_frequent_word(content)
    # 6
    all_actions_dictionary["6. the least frequent word in the file"] = get_least_frequent_word(content)
    # 7
    all_actions_dictionary["7. reversed file content"] = get_text_in_reverse(content)

    now = datetime.datetime.now()
    now = str(now)
    now = now.replace(" ", "_")
    current_directory = os.getcwd()
    new_file_name = f"{current_directory}/results_{now}.json"
    with open(new_file_name, "w") as file:
        json.dump(all_actions_dictionary, file)
    print(f"Results have been saved to {new_file_name}")
