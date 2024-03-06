path_to_file = "./books/frankenstein.txt"

def count_words(words: str):
     return len(words.split())

def sort_on(dict):
     return dict["count"]

def count_letters(words:str):
    lowered_words = words.lower()
    dic = {}
    for letter in lowered_words:
        if letter.isalpha():
            if letter in dic:
                dic[letter] = dic[letter] + 1
            else:
                dic[letter] = 1
    lis = []
    for keyval in dic:
        lis.append({"letter": keyval, "count": dic[keyval]})
 
    lis.sort(reverse= True, key=sort_on)
    return lis

with open(path_to_file) as f:
    file_contents = f.read()    
    letters_dict = count_letters(file_contents)
    word_count = count_words(file_contents)
    print(f'--- Begin report of {path_to_file} ---')
    print(f'{word_count} words found in the document')
    print("")
    for letter in letters_dict:
        print(f"the '{letter['letter']}' character was found {letter["count"]} times")