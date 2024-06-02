def commatize(lst):
    if not lst:
        return ""
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return " and ".join(lst)
    else:
        return ", ".join(lst[:-1]) + ", and " + lst[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
print(commatize(spam))  # Output: 'apples, bananas, tofu, and cats'

empty_list = []
print(commatize(empty_list))  # Output: ""