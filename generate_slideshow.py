def read_file(file_object):
    """Function that reads the file and converts it to the data structure"""
    dataset = []
    with open(file_object) as f:
        data = f.readlines()
        tags = []
        for index, line in enumerate(data):
            if index > 0:
                words = line.split()
                current_data = {}
                current_data['id'] = index - 1
                current_data['type'] = words[0]
                current_data['number_of_tags'] = words[1]
                tag = words[2:]
                current_data['tags'] = tag
                dataset.append(current_data)
                tags.extend(tag)
    return dataset, set(tags)


def generate_slideshow(file_path):
    """
    Generates a slideshow.

    Returns:
        slideshow (list): a list of slideshow objects
    """
    dataset, tags = read_file(file_path)
    hor_category_pictures, ver_category_pictures = [], []
    hor_unique_ids, ver_unique_ids = [], []
    ver_slide = []
    for tag in tags:
        for data in dataset:
            if tag in data['tags'] and data['id'] not in hor_unique_ids and data['type'] == 'H':
                hor_category_pictures.append([data])
                hor_unique_ids.append(data['id'])

            if tag in data['tags'] and data['id'] not in ver_unique_ids and data['type'] == 'V':
                if len(ver_slide) < 2:
                    ver_slide.append(data)
                else:
                    ver_slide = []
                    ver_slide.append(data)

                if len(ver_slide) == 2:
                    ver_category_pictures.append(ver_slide)
                ver_unique_ids.append(data['id'])
    return hor_category_pictures + ver_category_pictures

def write_to_file(file_path):
    """Write the result to file"""
    results = generate_slideshow(file_path)
    with open('solution.txt', 'w') as f:
        f.write(f'{len(results)}\n')
        for data in results:
            if len(data) == 1:
                f.write(str(data[0]['id']) + "\n")
            else:
                f.write(str(data[0]['id']) + " " + str(data[1]['id']) + "\n")

    return 'All done!'

if __name__ == '__main__':
    print(write_to_file('b_lovely_landscapes (1).txt'))
