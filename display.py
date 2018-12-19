from statistics import *
import file_handling

'''
    Here you need to make a simple menu printing
'''

# your code


def menu():
    print("""
Main menu

1. Total box office
2. Highest box office
3. Oldest and newest movies
4. Last movie in alphabetical order
5. Average release year
6. Movie with the longest named director
7. Exit  """)
    option = input("Choose a function: ")
    if option == "1":
        total_box_office()
    elif option == "2":
        highest_box_office()
    elif option == "3":
        oldest_and_newest()
    elif option == "4":
        alphabetically_last()
    elif option == "5":
        average_year()
    elif option == "6":
        longest_director()
    elif option == "7":
        exit()
    else:
        print("Choose an option from 1 to 7!")
        menu()

'''
    Here you need to print out the result of the function
'''
#your code