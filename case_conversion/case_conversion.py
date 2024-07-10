def to_camel_case(string_snake: str) -> str:
    words = string_snake.split('_')
    for i in range(1, len(words)):
        words[i] = words[i].capitalize()
    return ''.join(words)


def to_snake_case(string_camel: str) -> str:
    words = ['']
    i = 0
    for letter in string_camel:
        if letter.isupper():
            i += 1
            words.append(letter.lower())
        else:
            words[i] += letter
    return '_'.join(words)
