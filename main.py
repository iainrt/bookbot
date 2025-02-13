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
         

path_to_file = "books/frankenstein.txt"

def main(path_to_file):
    text = get_book_text(path_to_file)
    #print(text)
    #count = word_count(text)
    #print(f"word count is {count}")
    input = char_count(text)
    print(input)

main(path_to_file)
    

