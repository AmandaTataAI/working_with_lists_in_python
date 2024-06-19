'''Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]'''

def sort_tuples_in_list_in_increasing_order_by_the_last_element():
    try:
        number_of_tuples_user_will_enter = int(input("How many tuples are you going to enter: "))
        print("\n")
        i = 1
        list_of_tuples_user_entered = []
        while i <= number_of_tuples_user_will_enter:
            value_at_index_one_of_tuple = input("Please enter a value at index one of tuple: ")
            value_at_index_two_of_tuple = input("Please enter a value at index two of tuple: ")
            print("\n")
            tuple_of_value_at_index_one_and_two = (value_at_index_one_of_tuple, value_at_index_two_of_tuple)
            list_of_tuples_user_entered.append(tuple_of_value_at_index_one_and_two)
            i = i + 1
        print("Sample List : " + str(list_of_tuples_user_entered))
        length_of_list_of_tuples_user_entered = len(list_of_tuples_user_entered)
        j = 0
        k = 1
        l = length_of_list_of_tuples_user_entered - 1
        while j <= length_of_list_of_tuples_user_entered - 1:
            while l > 0:
                if list_of_tuples_user_entered[l][k] < list_of_tuples_user_entered[l - 1][k]:
                    temporary_holder = list_of_tuples_user_entered[l - 1]
                    list_of_tuples_user_entered[l - 1] = list_of_tuples_user_entered[l]
                    list_of_tuples_user_entered[l] = temporary_holder

                l = l - 1
            l = length_of_list_of_tuples_user_entered - 1
            k = 1
            j = j + 1
        print("Expected Result : " + str(list_of_tuples_user_entered))

    except ValueError:
        print("Please enter a number that is an integer")
        sort_tuples_in_list_in_increasing_order_by_the_last_element()

sort_tuples_in_list_in_increasing_order_by_the_last_element()
