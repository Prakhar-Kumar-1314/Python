def caesar_cipher(string, offset):
    string2 = ""
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    for elements in string:
        x = letters.index(elements)
        y = x - offset
        letter2 = letters[y]
        string2 += letter2
    return string2


print(caesar_cipher("hello", 3))
