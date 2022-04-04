

def thesaurus(*args):
    dict_name = {}
    for i in args:
        first_letter = i[0].capitalize()
        if first_letter not in dict_name:
            dict_name[first_letter] = []
        dict_name[first_letter].append(i)
    return dict_name



print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))
