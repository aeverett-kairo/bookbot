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
   text_lowered = list(characters)
   characters_name = 
   for character in text_lowered:
      if character not in characters_name:
         characters_name["name"] = character
         characters_name["num"] = 1
      else:
         characters_name["num"] += 1
      return characters_name
