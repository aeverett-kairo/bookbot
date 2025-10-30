def word_count(text):
    word_list = text.split()
    count = 0
    for word in word_list:
     count += 1
    return count

def character_count(characters):
    text_lowered = list(characters)
    character_count = {}
    for character in text_lowered:
      if character not in character_count:
        character_count[character] = 1
      else:
        character_count[character] += 1
    return character_count
       
def sort_on(items):
    return items["num"]

def sort_characters_by_count(characters):
<<<<<<< HEAD
    char_list_dict = []
    for letters in characters:
        letter =  letters
        number = characters[letters]
        char_dict = {"char": letter, "num": number}
        char_list_dict.append(char_dict)
    char_list_dict.sort(reverse=True, key=sort_on)
    return char_list_dict
=======
   text_lowered = list(characters)
   char_count = []
   char_dict = {"char": char, "num": num}
   for character in text_lowered:
      if character not in characters_name:
         characters_name["name"] = character
         characters_name["num"] = 1
      else:
         characters_name["num"] += 1
      return characters_name
>>>>>>> 9fd2329 (complete)
