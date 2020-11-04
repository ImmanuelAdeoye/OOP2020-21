#course: Object-oriented programming, year 2, semester 1
#academic year: 2020-21
#author: B. Schoen-Phelan
#date: 02-10-2020
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        #
        # Enter your own print statements below:
        #
        print('I love you')
        print('My name is Immanuel')
        print('I am learning how to write python code')

        # print only first and last of the sentence:
        char_1 = message[0:1]
        char_2 = message[7:8]
        print(char_1,char_2)

        # use slice notation:
        slice_notation = message[1:6]
        print(slice_notation)

        # escaping a character:
        print('He said "that\'s fantatsic"!')

        # find all a's in the input word and count how many there are:
        print(message.find('a'))
        print(message.count('a'))
        print(message.islower())

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():
        print(message.replace('a','-'))



    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:
        my_list = (list(message.split(" ")))
        print(my_list)

        # append a new element to the list and print:
        my_list.append('adeoye')
        print(my_list)

        # remove from the list in 3 ways:
        my_list.remove('adeoye')
        print(my_list)
        my_list.pop(2)
        print(my_list)
        del my_list[0]
        print(my_list)

        # check if the word cake is in your input list:
        a = message
        b = 'cake'

        if b in a:
            print('cake is present')
        else:
            print('cake is not present')

        # reverse the items in the list and print:
        my_list.reverse()
        print(my_list)

        # reverse the list with the slicing trick:
        my_list[::-1]
        print(my_list)

        # print the list 3 times by using multiplication:
        my_list*3
        print(my_list)


tas = Types_and_Strings()
tas.play_with_lists()
