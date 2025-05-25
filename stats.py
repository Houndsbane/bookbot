def count_words(text_from_book):
    split_words=text_from_book.split()
    words=len(split_words)
    return words

def count_characters(text_from_book):
    characters=text_from_book.lower()
    character_count={}
    for char in characters:
        character_count[char] = character_count.get(char, 0) + 1
    return character_count

def sort_dict(from_count_characters):
    dict_list=[]
    for char, count in from_count_characters.items():
        char_dict = {"char": char, "count": count}
        dict_list.append(char_dict)
    
    dict_list.sort(reverse=True, key=lambda dict_item: dict_item["count"])
    return dict_list