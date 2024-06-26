'''Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2'''

def find_if_characters_are_the_same():
    try:
        number_of_strings_that_the_user_will_enter_that_is_an_integer = int(input("Please enter the number of strings you will enter: "))
        list_of_strings_that_the_user_entered = []
        i = 1
        while i <= number_of_strings_that_the_user_will_enter_that_is_an_integer:
            string_that_the_user_entered = input("Please enter a string: ")
            list_of_strings_that_the_user_entered.append(string_that_the_user_entered)

            i = i + 1
        print("\n")
        print("Sample List: " + str(list_of_strings_that_the_user_entered))

        l = 0
        list_of_words_whose_first_and_last_letters_are_the_same = []
        while l <= number_of_strings_that_the_user_will_enter_that_is_an_integer - 1:
            word_from_the_list_of_strings_that_the_user_entered = list_of_strings_that_the_user_entered[l]
            length_of_word_from_the_list_of_strings_that_the_user_entered = len(word_from_the_list_of_strings_that_the_user_entered)
            length_of_one_word_in_the_list_of_strings_that_the_user_entered = len(list_of_strings_that_the_user_entered[l])
            if length_of_word_from_the_list_of_strings_that_the_user_entered >= 2 and  word_from_the_list_of_strings_that_the_user_entered[0] == word_from_the_list_of_strings_that_the_user_entered[length_of_one_word_in_the_list_of_strings_that_the_user_entered - 1]:
                list_of_words_whose_first_and_last_letters_are_the_same.append(word_from_the_list_of_strings_that_the_user_entered)

            l = l + 1
        print("Expected Result: " + str(len(list_of_words_whose_first_and_last_letters_are_the_same)))
    except ValueError:
        print("Please enter a value that is an integer")
        find_if_characters_are_the_same()

find_if_characters_are_the_same()