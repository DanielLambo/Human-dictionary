dictionary = {}

def lookup(dictionary, word):
    if word in dictionary:
        return dictionary[word]
    else:
        return ""

def add_definition(dictionary, word, definition):
    if word not in dictionary:
        dictionary[word] = [definition]
        return 1
    elif word in dictionary:
        dictionary[word].append(definition)
        return 2

def remove_definition(dictionary, word, index):
    if word in dictionary:
        try:
            element = dictionary[word][index]
            dictionary[word].pop(index)
            return True
        except IndexError:
            return False
    return False

def remove_word(dictionary, word):
    if word in dictionary:
        del dictionary[word]
        return True
    else:
        return False
