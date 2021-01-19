import bs4
import numpy as np

usebio = '210102122486Dreiknigspokal2021.xml'

with open(usebio, 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'xml')

# get tournament parameters
nr_boards = int(soup.find('BOARDS_PLAYED').text)
# print(nr_boards)

nr_pairs = len(soup.findAll('PAIR'))
# print(nr_pairs)

nr_tables = nr_pairs // 2
# print(nr_tables)

s_opt = nr_tables * (nr_tables - 1) * nr_boards
# print(s_opt)

bal_matrix = np.zeros([nr_pairs, nr_pairs], dtype=np.int)

boards = soup.findAll('BOARD')

for board in boards:
    ns = [int(n.text)-1 for n in board.findAll('NS_PAIR_NUMBER')]
    ew = [int(n.text)-1 for n in board.findAll('EW_PAIR_NUMBER')]

    for i in range(0, len(ns)):
        bal_matrix[min(ns[i], ew[i]), max(ns[i], ew[i])] += len(ns) - 1

        for j in range(i+1, len(ns)):
            # opposite direction
            bal_matrix[min(ns[i], ew[j]), max(ns[i], ew[j])] -= 1
            bal_matrix[min(ns[j], ew[i]), max(ns[j], ew[i])] -= 1

            # same direction
            bal_matrix[min(ns[i], ns[j]), max(ns[i], ns[j])] += 1
            bal_matrix[min(ew[i], ew[j]), max(ew[i], ew[j])] += 1

bal_matrix = bal_matrix ** 2

calibre = 100. * s_opt**2 / (.5 * nr_pairs * (nr_pairs - 1) * np.sum(bal_matrix))
print('calibre:', round(calibre))