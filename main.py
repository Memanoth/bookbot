def main():
    url = "books/frankenstein.txt"
    with open(url) as f:
        file_contents = f.read()

    # Calculate number of words in the book
    words = len(file_contents.split())

    #Calculate number of times characters appear in the book
    char_count = {}
    lowered_string = file_contents.lower()
    
    #add dictionary of character to the string
    for char in lowered_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    ##Sort characters in descending order by count
    # Add characters to a list
    character_list = []
    for char in char_count:
        if char.isalpha():
            character_object = {}
            character_object["character"] = char
            character_object["count"] = char_count[char]
            character_list.append(character_object)
    
    def sort_on(dict):
        return dict["count"]
    
    character_list.sort(reverse=True, key=sort_on)
    #Report generation

    print(f"--- Begin report of {url} ---")
    print(f"{words} words found in the document")
    print()

    for item in character_list:
        print(f"The '{item['character']}' character was found {item['count']} times")
    print(f"--- End of report ---")
    
main()