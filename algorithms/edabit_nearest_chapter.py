def nearest_chapter(chapters_dictionary, page):
    nearest_chapter_name = list(chapters_dictionary.keys())[0]
    nearest_distance = abs(page - chapters_dictionary[nearest_chapter_name])
    for x, y in chapters_dictionary.items():
        current_distance = abs(page - y)
        if current_distance <= nearest_distance:
            nearest_distance = current_distance
            nearest_chapter_name = x
    return nearest_chapter_name


print(nearest_chapter({"Chapter 1": 1, "Chapter 2": 15, "Chapter 3": 37}, 10))
print(nearest_chapter({"New Beginnings": 1, "Strange Developments": 62, "The End?": 194, "The True Ending": 460}, 200))
print(nearest_chapter({"Chapter 1a": 1, "Chapter 1b": 5}, 3))
