def merge(stripped_txt,input_arr):

    appnd = stripped_txt.format(*input_arr)
    return appnd

print(merge('It was a {} and {} {}.',['dark', 'stormy', 'night']))

