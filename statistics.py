from file_handling import *
'''
    There are the tasks wich you need to make in order to pass your PA
'''


def total_box_office():
    # Calculates the total sum of every box office in the list
    money = 0
    with open("movies_data.ini", "r") as data:
        for line in data:
            line = line.strip()
            if "box_office" in line:
                money += int(line[11:])
    print(money)


def total_box_office_dict():
    sum_of_boxes = []
    sum_nums = 0
    sum_of_nums = []
    movies = file_import_dictionary()
    for key in movies.items():
        for v in key:
            if 'box_office' in v:
                sum_of_boxes.append(v['box_office'])
    for item in sum_of_boxes:
        for nums in item:
            nums = int(nums)
            sum_nums += nums
            sum_of_nums.append(sum_nums)
    print('$', sum_nums)


def highest_box_office():
    # Displays the highest grossing movie
    names = []
    directors = []
    stars = []
    release_years = []
    box_offices = []
    money = []
    with open("movies_data.ini", "r") as data:
        for line in data:
            line = line.strip()
            if "box_office" in line:
                money.append(int(line[11:]))
    biggest = max(money)
    biggest = str(biggest)
    with open("movies_data.ini", "r") as data:
        for line in data:
            line = line.strip()
            if "name" in line:
                names.append(line[5:])
            elif "director" in line:
                directors.append(line[11:])
            elif "stars" in line:
                stars.append(line[8:])
            elif "release_year" in line:
                release_years.append(line[-4:])
            elif "box_office" in line:
                box_offices.append(line[11:])
        index = box_offices.index(biggest)
        print(names[index])
        print(directors[index])
        print(stars[index])
        print(release_years[index])
        print(box_offices[index])


def highest_box_office_dict():
    movies = file_import_dictionary()
    num = 0
    a = ''
    for k in movies.items():
        for v in k:
            if 'box_office' in v:
                # print(v['box_office'])
                a = v['box_office']
                for element in a:
                    if int(element) > num:
                        num = int(element)
                        bla = k[0]
                        name = k[1]    
    print(bla, name)


def oldest_and_newest():
    # Displays the oldest and the newest movie
    names = []
    directors = []
    stars = []
    release_years = []
    box_offices = []
    with open("movies_data.ini", "r") as data:
        for line in data:
            line = line.strip()
            if "name" in line:
                names.append(line[5:])
            elif "director" in line:
                directors.append(line[11:])
            elif "stars" in line:
                stars.append(line[8:])
            elif "release_year" in line:
                release_years.append(int(line[-4:]))
            elif "box_office" in line:
                box_offices.append(line[11:])
    earliest = min(release_years)
    latest = max(release_years)
    earliest_index = release_years.index(earliest)
    latest_index = release_years.index(latest)
    print("\n")
    print(names[earliest_index])
    print(directors[earliest_index])
    print(stars[earliest_index])
    print(release_years[earliest_index])
    print(box_offices[earliest_index])
    print("\n")
    print(names[latest_index])
    print(directors[latest_index])
    print(stars[latest_index])
    print(release_years[latest_index])
    print(box_offices[latest_index])


def oldest_and_newest_dict():
    movies = file_import_dictionary()
    a = ''
    name = ''
    num = 0
    rnd_num = 4000
    its_me = ''
    for k in movies.items():
        for v in k:
            if 'release_year' in v:
                a = v['release_year']
                for element in a:
                    if int(element) > num:
                        num = int(element)
                        its_me = k[0]
                        name = k[1]
                    elif int(element) < rnd_num:
                        rnd_num = int(element)
                        title = k[0]
                        info = k[1]
    print(its_me, name, '\n')
    print(title, info)


def alphabetically_last():
    # Displays the last movie alphabetically
    names = []
    directors = []
    stars = []
    release_years = []
    box_offices = []
    with open("movies_data.ini", "r") as data:
        for line in data:
            line = line.strip()
            if "name" in line:
                names.append(line[5:])
            elif "director" in line:
                directors.append(line[11:])
            elif "stars" in line:
                stars.append(line[8:])
            elif "release_year" in line:
                release_years.append(int(line[-4:]))
            elif "box_office" in line:
                box_offices.append(line[11:])
    last = max(names)
    last_index = names.index(last)
    print(names[last_index])
    print(directors[last_index])
    print(stars[last_index])
    print(release_years[last_index])
    print(box_offices[last_index])


def alphabetically_last_dict():
    movies = file_import_dictionary()
    a = []
    for k in movies.items():
        for v in k:
            if 'name' in v:
                a.append(v['name'])
    print(max(a))

    
def average_year():
    # Calculates the average year the movies were made
    years = []
    with open("movies_data.ini", "r") as data:
        for line in data:
            line = line.strip()
            if "release_year" in line:
                years.append(int(line[-4:]))
    lenght = len(years)
    total_years = sum(years)
    print(round(total_years / lenght))


def average_year_dict():
    print("¯\_(ツ)_/¯")


def longest_director():
    # Displays the movie with the longest named director
    names = []
    directors = []
    stars = []
    release_years = []
    box_offices = []
    with open("movies_data.ini", "r") as data:
        for line in data:
            line = line.strip()
            if "name" in line:
                names.append(line[5:])
            elif "director" in line:
                directors.append(line[11:])
            elif "stars" in line:
                stars.append(line[8:])
            elif "release_year" in line:
                release_years.append(int(line[-4:]))
            elif "box_office" in line:
                box_offices.append(line[11:])
    last = max(names, key=len)
    last_index = names.index(last)
    print(names[last_index])
    print(directors[last_index])
    print(stars[last_index])
    print(release_years[last_index])
    print(box_offices[last_index])


def longest_director_dict():
    print("¯\_(ツ)_/¯")
