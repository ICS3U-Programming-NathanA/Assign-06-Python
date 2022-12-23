#!/usr/bin/env python3

# Created By: Nathan
# Date: Dec. 21, 2022
# This program finds the even numbers of a list it then displays it

# Function for finding the average of even numbers
def average_even(even_list_num):
    # set sum to 0
    sum = 0
    # for each loop to calculate the sum of all the numbers
    for counter in even_list_num:
        sum = sum + counter
    # sum divided by the length to find the average
    average = sum / len(even_list_num)
    # return the average
    return average


# Function for finding the average of odd numbers
def average_odd(odd_list_num):
    # set sum to 0
    sum = 0
    # for each loop to calculate the sum of all the numbers
    for counter in odd_list_num:
        sum = sum + counter
    # sum divided by the length to find the average
    average = sum / len(odd_list_num)
    # return the average
    return average


# function that finds the odd numbers inside the list
def odd_list(num_list):
    # Create a new list to store the odd integers
    odd_num_list = []

    # for each loop to determine all the odd numbers
    for counter in num_list:
        # if the number is odd then add it to a new list
        if counter % 2 != 0:
            odd_num_list.append(counter)

    # Return the list of odd integers
    return odd_num_list


def even_list(num_list):
    # Create a new list to store the even integers
    even_num_list = []

    # Iterate through the list of integers
    for counter in num_list:
        # If the integer is even, append it to the even_num_list list
        if counter % 2 == 0:
            even_num_list.append(counter)

    # Return the list of even integers
    return even_num_list


def main():
    # set user_num_list to an empty list
    user_num_list = []
    # while true loop so the user can enter multiple integers
    while True:
        # Ask the user to enter a list of integers``
        user_num_str = input("Enter a integer or type stop: ")
        # if user_num_str is "STOP"
        if user_num_str.upper() == "STOP":
            # Asks the user if they want to see the even integers, odd integers or both in the list
            even_or_odd = input("Type e for even and type o for odd: ")
            # if even_or_odd is "E"
            if even_or_odd.upper() == "E":
                # call even_list(user_num_list)
                even_integers = even_list(user_num_list)
                # Print the even integers
                print(f"The even integers are: {even_integers}")
                # Asks the user if they want to find the average of the new list
                average_question_even = input(
                    "Would you like to find the average of these numbers? (y or n): "
                )
                # if they answer with Y
                if average_question_even.upper() == "Y":
                    # call average_even(even_integers)
                    average = average_even(even_integers)
                    # print the average
                    print(f"The average of all the numbers is {average}")
                # break out of the loop
                break
            # elif even_or_odd is "O"
            elif even_or_odd.upper() == "O":
                # call odd_list(user_num_list)
                odd_integers = odd_list(user_num_list)
                # Print the odd integers
                print(f"The odd integers are: {odd_integers}")
                # Asks the user if they want to find the average of the new list
                average_question_odd = input(
                    "Would you like to find the average of these numbers? (y or n): "
                )
                # if they answer with Y
                if average_question_odd.upper() == "Y":
                    # call average_even(odd_integers)
                    average = average_odd(odd_integers)
                    # print the average
                    print(f"The average of all the numbers is {average}")
                # break out of the loop
                break
            else:
                # You must enter either E , O or BOTH
                print("Enter either 'E', 'O' ")
                # break out of the loop
                break
        # Call the positive_list function to get a list of even integers
        try:
            user_num_int = int(user_num_str)
        except:
            # If they entered a invalid input then display this
            print("You must enter a valid number.")
            # break out of the loop
            break
        else:
            # add user_num_int to user_num_list
            user_num_list.append(user_num_int)
            # print saying it was added
            print("Added the integer to the list")


if __name__ == "__main__":
    main()
