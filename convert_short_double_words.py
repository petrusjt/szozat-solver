
non_single_msghk = "cs dzs dz gy ly ny sz ty zs".split()
non_single_msghk_map = {asd[1]: asd[0] for asd in enumerate(non_single_msghk)}


with open("rovid_dupla_msghs_szavak.txt") as file, open("prepared_rovid_dupla_szavak.txt", "w") as fout:
    for line in file:
        prepared_line = line.strip().lower()
        for key, value in non_single_msghk_map.items():
            prepared_line = prepared_line.replace(key, str(value))

        if len(prepared_line) == 5:
            out_line = prepared_line  # out_line = "".join([non_single_msghk[int(char)] if char.isdigit() else char for char in prepared_line])
            print(out_line, file=fout)

