def sort_on(dict):
    return dict["num"]


character_dict = {}

with open("books/frankenstein.txt", "r") as file:
    content = file.readlines()
    print(f"line count: {len(content)}")
    wordcount = 0
    
    for line in content:
        word_split = line.split()
        wordcount += len(word_split)

        for character in line:
            if character.isalpha():
                lower_char = character.lower()
                if lower_char in character_dict:
                    character_dict[lower_char] += 1
                else:
                    character_dict[lower_char] = 1
    
file.close()

character_lists = []
for key in character_dict:
    new_entry = {}
    new_entry["char"] = key
    new_entry["num"] = character_dict[key]
    character_lists.append(new_entry)

character_lists.sort(reverse=True, key=sort_on)

print(character_lists)

print(f"Word cout: {wordcount}")

for dictionary_entry in character_lists:
    print(f"['{dictionary_entry["char"]}'] = {dictionary_entry["num"]}")

