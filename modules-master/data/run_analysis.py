from sys import argv
from iris_analysis.io.load import load
from iris_analysis.io.save import save
from iris_analysis.calculate import mean2, median2, std2


def main(fileR, fileW):
    tab = load(fileR)
    tab2 = list(map(list, zip(*tab)))
    res = []
    res.append(["function", "Mean", "Median", "STD"])
    for i in range(len(tab2)-1):
        res.append([])
        res[i+1].append(tab2[i][0])
        res[i+1].append(mean2(tab2[i][1:]))
        res[i+1].append(median2(tab2[i][1:]))
        res[i+1].append(std2(tab2[i][1:]))
    save(res, fileW)


main(argv[1], argv[2])
