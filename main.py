from pandas import read_excel

data = read_excel('data/test.xlsx', index_col=None, header=None)

for i in range(0, int(data.size/2)):
    print(data.at[i, 0])