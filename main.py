def count_characters(text):
    char_counts = {}
    for character in text:
        lowercase_char = character.lower()
        if lowercase_char.isalpha():
            if lowercase_char in char_counts:
                char_counts[lowercase_char] = char_counts[lowercase_char] + 1
            else:
                char_counts[lowercase_char] = 1
    return char_counts

def get_char_list(char_counts):
    char_list = []
    for char, num in char_counts.items():
        char_list.append({"char": char, "num": num})
    return char_list

def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        char_counts = count_characters(file_contents)
        char_list = get_char_list(char_counts)
        char_list.sort(reverse=True, key=sort_on)
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(file_contents.split())} words found in the document\n")
        
        for char_dict in char_list:
            print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")

if __name__ == "__main__":
    main()
