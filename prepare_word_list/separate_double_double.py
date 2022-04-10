

double_non_single_msghk = "ccs ggy lly nny ssz tty zzs".split()


def contains_none(string, values):
    for value in values:
        if value in string:
            return False
    return True


double_double_words = []
double_msgh_words = []

with open("nem_egyszeru_szavak.txt") as file:
    for line in file:
        prepared_line = line.strip().lower()
        if contains_none(prepared_line, double_non_single_msghk):
            double_msgh_words.append(prepared_line)
        else:
            double_double_words.append(prepared_line)

with open("hosszu_dupla_msghs_szavak.txt", "w") as file:
    for word in double_double_words:
        print(word, file=file)

with open("rovid_dupla_msghs_szavak.txt", "w") as file:
    for word in double_msgh_words:
        print(word, file=file)
