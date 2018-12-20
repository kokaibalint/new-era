
def file_import_dictionary():
    with open('movies_data.ini', 'r') as f:
        all_movies = {}
        current_movie = None
        for line in f:
            line = line.strip()
            if line[0] == '[':
                all_movies[line] = {}
                current_movie = line
            else:
                k, v = line.split('=')
                all_movies[current_movie][k] = [v]
        return all_movies


def file_import_list():
    with open("movies_data.ini", "r") as data:
        for line in data:
            line = line.strip()
            return data