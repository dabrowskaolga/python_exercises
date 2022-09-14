import unittest
from unittest.mock import patch
from text_processing.src.actions import get_text_length, get_words_count, get_word_occurrences, \
    get_most_frequent_word, get_least_frequent_word, get_text_in_reverse


class TestActions(unittest.TestCase):
    CONTENT = "This is a test text with repeated text word."
    
    def test_get_text_length_will_return_correct_text_length(self):
        txt_length = get_text_length(self.CONTENT)
        self.assertEqual(txt_length, len(self.CONTENT))

    def test_get_words_count_will_return_correct_number_of_words(self):
        words_count = get_words_count(self.CONTENT)
        self.assertEqual(words_count, 9)

    @patch("text_processing.src.actions.input", return_value="text")
    def test_get_word_occurrences_will_return_particular_word_occurrences(self, _):
        word_to_check, occurrences = get_word_occurrences(self.CONTENT)
        self.assertEqual(word_to_check, "text")
        self.assertEqual(occurrences, 2)

    def test_get_most_frequent_word_will_return_most_frequent_word_in_text(self):
        most_frequent_word = get_most_frequent_word(self.CONTENT)
        self.assertEqual(most_frequent_word, "text")

    def test_get_least_frequent_word_will_return_first_least_frequent_word_in_text(self):
        least_frequent_word = get_least_frequent_word(self.CONTENT)
        self.assertEqual(least_frequent_word, "This")

    def test_get_text_in_reverse_will_return_reversed_text(self):
        reversed_txt = get_text_in_reverse(self.CONTENT)
        self.assertEqual(reversed_txt, ".drow txet detaeper htiw txet tset a si sihT")
