import file_handling

movies = file_handling.file_import()
rnd_list = []
for key in movies.items():
    for v in key:
        if 'box_office' in v:
            rnd_list.append(v['box_office'])
print(max(rnd_list))

