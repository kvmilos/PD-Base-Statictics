def save(tab, file):
    with open(file, "w") as f:
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                if j != len(tab[i])-1:
                    f.write(f"{tab[i][j]},")
                else:
                    f.write(f"{tab[i][j]}")
            f.write('\n')
