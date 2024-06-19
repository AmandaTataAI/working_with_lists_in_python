'''Write a Python program to sum all the items in a list'''
def sum_of_all_the_items_in_a_list():
    try:
        number_of_times_user_will_input = int(input("Please enter the number of times you will enter a value: "))
        i = 1
        list_of_values_that_are_integers = []

        while i <= number_of_times_user_will_input:
            value_that_is_an_integer = int(input("Please enter a value: "))
            list_of_values_that_are_integers.append(value_that_is_an_integer)
            i = i + 1
        length_of_list_of_values_that_are_integers = len(list_of_values_that_are_integers)

        if(length_of_list_of_values_that_are_integers == 1):
            print(list_of_values_that_are_integers[0])
        else:
            i = 0
            j = 1
            while i < length_of_list_of_values_that_are_integers - 1:
                result = list_of_values_that_are_integers[i] + list_of_values_that_are_integers[i + 1]
                list_of_values_that_are_integers[i + 1] = result
                i = i + 1

        print("The sum of all items in the list is: " + str(list_of_values_that_are_integers[length_of_list_of_values_that_are_integers - 1]))
    except ValueError:
        print("Please enter a value that is an integer")
        sum_of_all_the_items_in_a_list()

sum_of_all_the_items_in_a_list()
