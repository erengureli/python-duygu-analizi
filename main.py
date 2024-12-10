from pandas import read_excel
from polarite import calculatePolarite

# excel'i pythona aktarıyoruz
data = read_excel('data/test1.xlsx', index_col=None, header=None)
dataLen = int(data.size/2)

returnMatrix = [] # geri dönen değeri tutacak bir matrix açıyoruz. // gerçek değer / tahmini değer

# Her satırı teker teker fonksiyonumuza sokup dönen değerleri depoluyoruz.
for i in range(0, dataLen):
    temp = [str(data.at[i, 1]) == "POZİTİF", calculatePolarite(str(data.at[i, 0]))]
    returnMatrix.append(temp)


# Karmaşıklık Matrixi Hesaplama
karMatrix = [[0, 0],[0, 0]] # [[DP, YP],[YN, DN]]

for index,i in enumerate(returnMatrix):
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
    # print(data.at[index, 0] + " : " + str(i[0]) + " " + str(i[1]))
  
dogruluk = (karMatrix[0][0] + karMatrix[1][1])/dataLen
kesinlik = (karMatrix[0][0])/(karMatrix[0][0] + karMatrix[0][1])
anma = (karMatrix[0][0])/(karMatrix[0][0] + karMatrix[1][0])
f1olc = (2*kesinlik*anma)/(kesinlik+anma)

print()
print(karMatrix[0])
print(karMatrix[1])
print(f"Doğruluk: {dogruluk}, Kesinlik: {kesinlik}, Anma: {anma}, F1-Ölçütü: {f1olc}")

