my_input = input()


def check3(expression):
    if len(expression) % 2 != 0:
        return 0

    opening = ("(", "[", "{")
    closing = (")", "]", "}")
    mapping = dict(zip(opening, closing))

    if expression[0] in closing:
        return 0

    if expression[-1] in opening:
        return 0

    closing_queue = []
    for letter in expression:
        if letter in opening:
            closing_queue.append(mapping[letter])
        elif letter in closing:
            if not closing_queue:
                return 0

            if closing_queue[-1] == letter:
                closing_queue.pop()
            else:
                return 0

    return 1

print(check3(my_input))