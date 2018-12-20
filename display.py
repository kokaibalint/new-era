from statistics import *
import file_handling

'''
    Here you need to make a simple menu printing
'''



def menu():
    print("""
Main menu

1. Total box office
2. Total box office (dict)
3. Highest box office
4. Highest box office (dict)
5. Oldest and newest movies
6. Oldest and newest movies (dict)
7. Last movie in alphabetical order
8. Last movie in alphabetical order (dict)
9. Average release year
10. Average release year (dict)
11. Movie with the longest named director
12. Movie with the longest named director (dict)
13. Exit
""")
    option = input("Choose a function: ")
    if option == "1":
        total_box_office()
    elif option == "2":
        total_box_office_dict()
    elif option == "3":
        highest_box_office()
    elif option == "4":
        highest_box_office_dict()
    elif option == "5":
        oldest_and_newest()
    elif option == "6":
        oldest_and_newest_dict()
    elif option == "7":
        alphabetically_last()
    elif option == "8":
        alphabetically_last_dict()
    elif option == "9":
        average_year()
    elif option == "10":
        average_year_dict()
    elif option == "11":
        longest_director()
    elif option == "12":
        longest_director_dict()
    elif option == "13":
        exit()
    else:
        print("Choose an option from 1 to 7!")
        menu()


'''
    Here you need to print out the result of the function
'''
