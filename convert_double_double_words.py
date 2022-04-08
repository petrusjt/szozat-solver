
non_single_msghk = "cs dzs dz gy ly ny sz ty zs".split()
non_single_msghk_map = {asd[1]: asd[0] for asd in enumerate(non_single_msghk)}
double_non_single_msghk = "ccs dzs dz ggy lly nny ssz tty zzs".split()
double_non_single_msghk_map = {asd[0]: asd[1]*2 for asd in zip(double_non_single_msghk, non_single_msghk)}

with open("hosszu_dupla_msghs_szavak.txt") as file, open("prepared_hosszu_dupla_szavak.txt", "w") as fout:
    for line in file:
        prepared_line = line.strip().lower()

        for key, value in double_non_single_msghk_map.items():
            prepared_line = prepared_line.replace(key, str(value))

        for key, value in non_single_msghk_map.items():
            prepared_line = prepared_line.replace(key, str(value))

        if len(prepared_line) == 5:
            out_line = prepared_line  # out_line = "".join([non_single_msghk[int(char)] if char.isdigit() else char for char in prepared_line])
            print(out_line, file=fout)
