from user_inputs import get_content
from actions import (
    get_text_in_reverse,
    get_text_length,
    get_words_count,
    get_word_occurrences,
    get_letter_occurrences,
    get_most_frequent_word,
    get_least_frequent_word,
    export_data_to_file
)


def get_user_action():
    while True:
        chosen_action = input("Which action do you choose? \n")
        possible_actions = ["1", "2", "3", "4", "5", "6", "7", "8", "q"]
        if chosen_action == "":
            print("You need to choose the action!")
            continue
        if chosen_action not in possible_actions:
            print("The action indicated by you is not an option! Please correct the input!")
            continue
        return chosen_action


def main():
    content = get_content()

    while True:
        print("""\nHere's a list of possible actions:
        1: Text length - display a length of the given text
        2: Number of words - try to count how many words given text consists of
        3: Number of occurrences of a specific words
        4: Number of occurrences of a specific letter
        5: The most frequently occurring word - display the word that occurs in the text the most number of times
        6. The least frequently occurring word - display the word that occurs in the text the least number of times 
        7. Reverse the text - display the given text reversed
        8. Perform all of the above and save the results to a file
        (if you wish to quit, please type 'q')
        """)

        chosen_action = get_user_action()
        if chosen_action == "1":
            print(f"Your file contains {get_text_length(content)} characters.")
        elif chosen_action == "2":
            print(f"In your file there are {get_words_count(content)} words.")
        elif chosen_action == "3":
            word, occurrences = get_word_occurrences(content)
            print(f"The {word} appeared in the file {occurrences} times.")
        elif chosen_action == "4":
            letter, occurrences = get_letter_occurrences(content)
            print(f"The {letter} appeared in the file {occurrences} times.")
        elif chosen_action == "5":
            print(f"The most frequent word: {get_most_frequent_word(content)}.")
        elif chosen_action == "6":
            print(f"The least frequent word: {get_least_frequent_word(content)}")
        elif chosen_action == "7":
            print(f"Your text in revers: {get_text_in_reverse(content)}")
        elif chosen_action == "8":
            export_data_to_file(content)
        else:
            break


if __name__ == "__main__":
    main()
