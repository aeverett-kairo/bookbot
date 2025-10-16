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
       

def sort_characters_by_count(characters):
   char_list_dict = []
   for letters in characters:
      letter =  letters
      number = characters[letters]
      char_dict = {"char": letter, "num": number}
      char_list_dict.append(char_dict)
   return char_list_dict

#def sort_on(char_list):
#   return