def file_import():
    with open('movies_data.ini', 'r') as f:
        all_movies = {}
        current_movie = None
        for line in f:
            line = line.strip()
            if line[0] == '[':
                all_movies[line] = {}
                current_movie = line
            else:
                k,v = line.split('=')
                all_movies[current_movie][k] = [v]
        return all_movies
file_import()