# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)

        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3
        if len(self.user_input) > 3:
            new_word = self.user_input[0] + self.user_input[2] + self.user_input[1] + self.user_input[3:]
        elif len(self.user_input) <= 3:
            new_word = self.user_input
        else: #here we assume this word is just one character long or the space character
            print("try again")
            new_word = False

        print(new_word)

        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation
        sentence = self.user_input.strip().split()
        for index, word in enumerate(sentence):
            if len(word) > 3:
                temp_word = list(word)
                if(',' in temp_word) or ('.' in temp_word):
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-3]
                    temp_word[-3] = temp
                else:
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-2]
                    temp_word[-2] = temp

                swapped_word = ''.join(temp_word)
                sentence[index] = swapped_word
            else:
                sentence[index] = word

        the_swap = ' '.join(sentence)
        print(the_swap)

word_scrambler = WordScramble()
word_scrambler.scramble()

