def most_frequent_char(s):
    characters = {}
    first_character = s[0]
    for character in s:
        if character not in characters:
            characters[character] = 0
        characters[character] += 1
        if characters[character] > characters[first_character]:
            first_character = character
    return first_character
