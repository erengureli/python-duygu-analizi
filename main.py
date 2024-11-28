from pandas import read_excel
from polarite import calculatePolarite

data = read_excel('data/test.xlsx', index_col=None, header=None) # excel'i pythona aktarıyoruz
dataLen = int(data.size/2)

returnMatrix = [] # geri dönen değeri tutacak bir matrix açıyoruz. // gerçek değer / tahmini değer

# Her satırı teker teker fonksiyonumuza sokup dönen değerleri depoluyoruz.
for i in range(0, dataLen):
    temp = [data.at[i, 1] == "POZİTİF", calculatePolarite(data.at[i, 0])]
    returnMatrix.append(temp)


# Karmaşıklık Matrixi Hesaplama

karMatrix = [[0, 0],[0, 0]] # [[DP, YP],[YN, DN]]

for i in returnMatrix:
    print(i)
    if i[0] == i[1]:
        if i[0]:
            karMatrix[0][0] += 1 #DP
        else:
            karMatrix[1][1] += 1 #DN
    else:
        if i[1]:
            karMatrix[0][1] += 1 #YP
        else:
            karMatrix[1][0] += 1 #YN

dogruluk = (karMatrix[0][0] + karMatrix[1][1])/dataLen
kesinlik = (karMatrix[0][0])/(karMatrix[0][0] + karMatrix[0][1])
anma = (karMatrix[0][0])/(karMatrix[0][0] + karMatrix[1][0])
f1olc = (2*kesinlik*anma)/(kesinlik+anma)

print(karMatrix)
print(dogruluk, kesinlik, anma, f1olc)

