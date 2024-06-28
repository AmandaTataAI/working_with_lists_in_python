'''Write a python program to find the largest number in a list'''
def find_the_largest_number_in_a_list():
    try:
        number_of_numbers_that_the_user_will_enter_that_is_an_integer = int(input("Please enter the number of numbers you will enter: "))
        list_of_numbers_that_the_user_entered_that_are_integers = []

        def get_user_input(i):
            try:
                while i <= number_of_numbers_that_the_user_will_enter_that_is_an_integer:
                    number_that_the_user_has_entered = int(input("Please enter a number: "))
                    list_of_numbers_that_the_user_entered_that_are_integers.append(number_that_the_user_has_entered)
                    i = i + 1
            except ValueError:
                print("Please enter a value that is an integer")
                get_user_input(i + 1)


        get_user_input(1)

        length_of_list_of_numbers_that_are_integers = len(list_of_numbers_that_the_user_entered_that_are_integers)
        j = 0
        while j < length_of_list_of_numbers_that_are_integers - 1:
            if list_of_numbers_that_the_user_entered_that_are_integers[j] > list_of_numbers_that_the_user_entered_that_are_integers[j + 1]:
                temporary_holder = list_of_numbers_that_the_user_entered_that_are_integers[j + 1]
                list_of_numbers_that_the_user_entered_that_are_integers[j + 1] = list_of_numbers_that_the_user_entered_that_are_integers[j]
                list_of_numbers_that_the_user_entered_that_are_integers[j] = temporary_holder
            j = j + 1

        def print_the_largest_number_in_a_list():
            print("\n")
            print(str(list_of_numbers_that_the_user_entered_that_are_integers[length_of_list_of_numbers_that_are_integers - 1]) + " is the largest number")

        print_the_largest_number_in_a_list()
    except:
        print("Please enter a value that is an integer")
        find_the_largest_number_in_a_list()

find_the_largest_number_in_a_list()
