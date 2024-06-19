'''Write a python program to find the largest number in a list'''
def find_the_largest_number_in_a_list():
    try:
        number_of_numbers_user_will_enter = int(input("Please enter the number of numbers you will enter: "))
        list_of_numbers_that_are_integers = []
        i = 1
        while i <= number_of_numbers_user_will_enter:
            number_that_the_user_has_entered = input("Please enter a number: ")
            number_that_the_user_has_entered_as_an_integer = int(number_that_the_user_has_entered)
            list_of_numbers_that_are_integers.append(number_that_the_user_has_entered_as_an_integer)
            i = i + 1

        length_of_list_of_numbers_that_are_integers = len(list_of_numbers_that_are_integers)
        j = 0
        while j < length_of_list_of_numbers_that_are_integers - 1:
            if list_of_numbers_that_are_integers[j] > list_of_numbers_that_are_integers[j + 1]:
                temporary_holder = list_of_numbers_that_are_integers[j + 1]
                list_of_numbers_that_are_integers[j + 1] = list_of_numbers_that_are_integers[j]
                list_of_numbers_that_are_integers[j] = temporary_holder
            j = j + 1

        def print_the_largest_number_in_a_list():
            print("\n")
            print(str(list_of_numbers_that_are_integers[length_of_list_of_numbers_that_are_integers - 1]) +
                  " is the largest number")

        print_the_largest_number_in_a_list()
    except ValueError:
        print("Please enter a value that is an integer")
        find_the_largest_number_in_a_list()

find_the_largest_number_in_a_list()
