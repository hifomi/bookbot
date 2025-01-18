def word_count(text):
    count = text.split() 
    return len(count)

def character_count(letters):
    frank_letters = {}
    lowered_string = letters.lower()
    for letter in lowered_string:
        if letter in frank_letters:
            frank_letters[letter] += 1
        else:
            frank_letters[letter] = 1
    return frank_letters

def sort_on(dict):
    return dict["count"]

def report(char_count_dict, num_words):
    chars = []
    for char, count in char_count_dict.items():
         if char.isalpha():
            chars.append({"char": char, "count": count})
            
    chars.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    
    for char_dict in chars:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_num = word_count(file_contents)
        chars = character_count(file_contents)
        report(chars, word_num)

main()