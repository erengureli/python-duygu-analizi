'''
Güncel F-1 Değerleri:
    test  --> 0.8041714947856315
    test1 --> 0.8347826086956522
    test2 --> 0.8578199052132701
    test3 --> 0.7913978494623656
'''

from pandas import read_excel
from polarite import calculatePolarite

# excel'i pythona aktarıyoruz
data = read_excel('data/test.xlsx', index_col=None, header=None)
dataLen = int(data.size/2)

returnMatrix = [] # geri dönen değeri tutacak bir matrix açıyoruz. // gerçek değer / tahmini değer

# Her satırı teker teker fonksiyonumuza sokup dönen değerleri depoluyoruz.
for i in range(0, dataLen):
    temp = [list(filter(lambda i: i != " ", str(data.at[i, 1])))[0].lower() == "p", calculatePolarite(str(data.at[i, 0]))]
    returnMatrix.append(temp)

    # Cümle yanlış tahmin edildiyse printliyor.
    if temp[0] != temp[1]:
        print("Hatalı polarite olan cümle --> ", str(data.at[i, 0]), returnMatrix[i][0], returnMatrix[i][1])
        

# Karmaşıklık Matrixi Hesaplama Kısmı
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
    # print(data.at[index, 0] + " : " + str(i[0]) + " " + str(i[1])) # Test print

dogruluk = (karMatrix[0][0] + karMatrix[1][1])/dataLen
kesinlik = (karMatrix[0][0])/(karMatrix[0][0] + karMatrix[0][1])
anma = (karMatrix[0][0])/(karMatrix[0][0] + karMatrix[1][0])
f1olc = (2*kesinlik*anma)/(kesinlik+anma)

print()
print(karMatrix[0])
print(karMatrix[1])
print(f"Doğruluk: {dogruluk}, Kesinlik: {kesinlik}, Anma: {anma}, F1-Ölçütü: {f1olc}")