

with open("usable_words.txt", "w") as fout:
    with open("egyszeru_szavak.txt") as file:
        for line in file:
            print(line.strip(), file=fout)

    with open("prepared_rovid_dupla_szavak.txt") as file:
        for line in file:
            print(line.strip(), file=fout)

    with open("prepared_hosszu_dupla_szavak.txt") as file:
        for line in file:
            print(line.strip(), file=fout)
