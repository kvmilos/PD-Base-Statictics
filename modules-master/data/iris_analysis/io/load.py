def load(file):
    with open(file, "r") as f:
        tab = []
        tab2 = []
        for i in f:
            tab.append(i.split(sep=","))
        for i in range(len(tab)):
            tab2.append([])
            for j in range(len(tab[i])):
                if i == 0 or j == len(tab[i])-1:
                    tab2[i].append(tab[i][j].strip())
                else:
                    tab2[i].append(float(tab[i][j].strip()))
        return tab2
