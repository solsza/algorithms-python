def anagrams(s1, s2):
    return char_count(s1) == char_count(s2)


def char_count(s):
    count = {}
    for char in s:
        if char not in count:
            count[char] = 0
        count[char] += 1
    return count


def anagrams1(s1, s2):
    if len(s1) != len(s2):
        return False

    number_of_characters = {}
    for i in s1:
        if i not in number_of_characters:
            number_of_characters[i] = 1
    else:
        number_of_characters[i] += 1

    for i in s2:
        if i not in number_of_characters or number_of_characters[i] <= 0 :
            return False
        else:
            number_of_characters[i] -= 1
    return True
