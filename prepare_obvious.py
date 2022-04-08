

obvious_words = []
non_obvious_words = []

non_single_msghk = "cs dz dzs gy ly ny sz ty zs".split()


def contains_none(string, values):
    for value in values:
        if value in string:
            return False
    return True


with open("magyar_szavak.txt") as file:
    for line in file:
        prepared_line = line.strip().lower()
        if contains_none(prepared_line, non_single_msghk):
            obvious_words.append(prepared_line)
        else:
            non_obvious_words.append(prepared_line)

with open("egyszeru_szavak.txt", "w") as file:
    for word in [word for word in obvious_words if len(word) == 5]:
        print(word, file=file)

with open("nem_egyszeru_szavak.txt", "w") as file:
    for word in [word for word in non_obvious_words if 5 <= len(word) <= 8]:
        print(word, file=file)
