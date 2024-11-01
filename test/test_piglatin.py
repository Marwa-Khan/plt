import string
import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):
    # user story 1
    def test_input_phrase(self):
        # Initialize the translator with a phrase
        phrase = "hello world"
        translator = PigLatin(phrase)
        self.assertEqual("hello world",translator.get_phrase(phrase))

    # user story 2
    def test_empty_phrase(self):
        phrase = " "
        translator = PigLatin(phrase)
        self.assertEqual(" ",translator.get_phrase(phrase))

    # # user story 3
    def test_word_start_vowel_end_y(self):
        phrase = "any"
        translator = PigLatin(phrase)
        self.assertEqual("anynay",translator.get_phrase(phrase)+"nay")

    # # user story 3
    def test_word_start_end_vowel(self):
        phrase = "apple"
        translator = PigLatin(phrase)
        self.assertEqual("appleyay",translator.get_phrase(phrase)+"yay")

    # # user story 3
    def test_word_start_vowel_end_consonant(self):
        phrase = " "
        translator = PigLatin(phrase)
        self.assertEqual("ask",translator.get_phrase(phrase)+"askay")

    # # user story 4
    def test_word_start_single_consonant(self):
        phrase = "hello"
        translator = PigLatin(phrase)
        phrase=phrase[phrase:1]
        self.assertEqual("ellohay",translator.get_phrase(phrase)+"hay")

    # user story 5
    def test_word_start_multiple_consonant(self):
        phrase = "known"
        translator = PigLatin(phrase)
        vowels = ['a', 'e', 'i', 'o', 'u']
        for phrase in vowels:
            for char in phrase(0, 2):
                if char == vowels:
                    phrase=phrase(char, end="kn")
        self.assertEqual("ownknay",translator.get_phrase(phrase)+"ay")

        # user story 6
    def test_word_start_multiple_consonant_whitespace(self):
        phrase = "hello world"
        str_lst=phrase.split()
        # str_lst
        translator = PigLatin(phrase)
        vowels = ['a', 'e', 'i', 'o', 'u']
        for str_lst in vowels:
            for char in str_lst:
                if char == vowels:
                    str_lst = str_lst(char, end="elloh orldw")
        self.assertEqual("oellohay orldway", translator.get_phrase(str_lst) + "ay")

    def test_word_start_multiple_consonant_composite(self):
            phrase = "well-being"
            str_lst = phrase.split("-")
            # str_lst
            translator = PigLatin(phrase)
            vowels = ['a', 'e', 'i', 'o', 'u']
            for str_lst in vowels:
                for char in str_lst:
                    if char == vowels:
                        str_lst = str_lst(char, end="ellw-eingb")
            self.assertEqual("oellohay orldway", translator.get_phrase(str_lst) + "ay")

    # user story 7
    def test_word_start_multiple_consonant_whitespace_punctuation(self):
        phrase = "hello world!"
        for i in phrase:
            if i in string.punctuation:
                pun=i
        str_lst=phrase.split()
        # str_lst
        translator = PigLatin(phrase)
        vowels = ['a', 'e', 'i', 'o', 'u']
        for str_lst in vowels:
            for char in str_lst:
                if char == vowels:
                    str_lst = str_lst(char, end="elloh orldw")
        self.assertEqual("oellohay orldway", translator.get_phrase(str_lst) +"ay"+pun)


    def test_word_start_multiple_consonant_composite_punctutaion(self):
            phrase = "well-being!"
            for i in phrase:
                if i in string.punctuation:
                    pun = i
            str_lst = phrase.split("-")
            # str_lst
            translator = PigLatin(phrase)
            vowels = ['a', 'e', 'i', 'o', 'u']
            for str_lst in vowels:
                for char in str_lst:
                    if char == vowels:
                        str_lst = str_lst(char, end="ellw-eingb")
            self.assertEqual("oellohay orldway", translator.get_phrase(str_lst) + "ay"+pun)










