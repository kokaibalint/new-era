from file_handling import *
'''
    There are the tasks wich you need to make in order to pass your PA
'''
def total_box_office():
    # Calculates the total sum of every box office in the list
    #Bálint
    sum_of_boxes = []
    sum_nums = 0
    sum_of_nums = []
    movies = file_import()
    for key in movies.items():
        for v in key:
            if 'box_office' in v:
                sum_of_boxes.append(v['box_office'])
    for item in sum_of_boxes:
        for nums in item:
            nums = int(nums)
            sum_nums += nums
            sum_of_nums.append(sum_nums)
    print('$',sum_nums)

def highest_box_office():
    # Displays the highest grossing movie
    #Bálint
    movies = file_import()
    smth = 0
    box_offices = []
    biggest_num = []
    for key in movies.items():
        for v in key:
            if 'box_office' in v:
                box_offices.append(v['box_office'])
    # print(box_offices)
    for item in box_offices:
        for nums in item:
            biggest_num.append(int(nums))
    x = max(biggest_num)
    if x in:
        print('jéé')
    else:
        print('ohh')
    #         if nums > smth:
    #             smth = nums
    #             biggest_num.append(smth)
    #             if str(biggest_num[0]) in movies:
    #                 print('lol')
    #             else:
    #                 print('XDD')
    # # print(biggest_num[0],v['name'])



def oldest_and_newest():
    # Displays the oldest and the newest movie
    #Dani
    print("work in progress")


def alphabetically_last():
    # Displays the last movie alphabetically
    #Bálint
    print("work in progress")


def average_year():
    # Calculates the average year the movies were made
    #Dani
    print("work in progress")


def longest_director():
    # Displays the movie with the longest named director
    #Dani
    print("work in progress")
