# import the book and print to console

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lower_chars = text.lower()
    output = {}
    for char in lower_chars:
        if char not in output:
            output[char] = 1
        else:
            output[char] += 1
    return output

def report(text):
    char_dict = char_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(word_count(text), "words found in the document")
    for key in char_dict:
        if key.isalpha():
            print(f"The '{key}' character was found {char_dict[key]} times")
    print("--- End report ---")
         

path_to_file = "books/frankenstein.txt"

def main(path_to_file):
    text = get_book_text(path_to_file)
    report(text)

main(path_to_file)
    

