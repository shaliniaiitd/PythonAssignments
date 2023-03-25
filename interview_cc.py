def find_match(txt):

    in_dict = { "a": { "b": 3 }, "c": { "d": { "f": 6 } } }

    elements = txt.split('.')

    for i in elements:

        if i not in in_dict.keys():
            return "None"
        else:
            in_dict = in_dict[i]

    return in_dict

print(find_match("x"))











