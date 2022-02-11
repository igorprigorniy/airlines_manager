# Парсер csv-файла
def csv_parser(file_name):
    airports_info_list = []

    with open(file_name) as file:
        line = file.readline()
        while line:
            TAG, COUNTRY, CATEGORY = line.strip().split(',')
            airports_info_list.append({'TAG': TAG, 'COUNTRY': COUNTRY, 'CATEGORY': int(CATEGORY)})

            line = file.readline().strip()

    return airports_info_list

# Парсер группы html-страниц
def html_parser(file_names):

    def file_skip(n):
        for m in range(n): file.readline()

    airports_list = []
    airports_info_list = csv_parser('data/airports.csv')

    for file_name in file_names:
        with open(file_name) as file:
            line = file.readline()

            while line:
                if 'lineColorBox' in line.strip():
                    HUB, TAG = file.readline().strip()[:-2].replace(' ', '').split('/')
                    file_skip(3)
                    DISTANCE = int(file.readline().strip()[4:-8].replace(',', ''))
                    E    = int(file.readline().strip()[4:-9].replace(' ', ''))
                    B = int(file.readline().strip()[4:-9].replace(' ', ''))
                    F = int(file.readline().strip()[4:-9].replace(' ', ''))

                    for airports in airports_info_list:
                        if airports['TAG'] == TAG:
                            CATEGORY = airports['CATEGORY']
                            COUNTRY = airports['COUNTRY']
                            break

                    airports_list.append({'HUB': HUB, 'TAG': TAG, 'CATEGORY': CATEGORY, 'DISTANCE': DISTANCE, 'E': E, 'B': B, 'F': F, 'COUNTRY': COUNTRY})

                line = file.readline()

    return airports_list