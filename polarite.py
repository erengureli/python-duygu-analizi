import jpype
import jpype.imports
from jpype.types import *

from nltk.tokenize import word_tokenize

from words import *
from math import prod

# Launch the JVM
try:
    jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=zemberek.jar")
except:
    try:
        jpype.startJVM("C:\Program Files\Java\jre\\bin\server\jvm.dll", "-ea", "-Djava.class.path=zemberek.jar")
    except:
        try:
            jpype.startJVM("C:\Program Files\Java\jdk-23\\bin\server\jvm.dll", "-ea", "-Djava.class.path=zemberek.jar")
        except:
            print("Hata oluştu.")
            exit(1)

# Sadece 1 kere indirmesi gerekiyor. Her çalıştığında indirilmiş mi diye kontrol ediyor.
from nltk import download
download('stopwords')
download('punkt_tab')

# import the Java modules
TurkishMorphology = JClass("zemberek.morphology.TurkishMorphology")
morphology = TurkishMorphology.createWithDefaults()

def calculatePolarite(paragraph: str) -> bool:
    print("Girdi -->", paragraph)

    words = [word for word in word_tokenize(paragraph) if word not in etkisiz_kelimeler | punction]

    weigthList = []
    for word in words:
        for yalanci in yalanci_negatif:
            word = word.replace(yalanci,"")
        weigthDecider(word,weigthList)
    print("Sonuç:", weigthList)
    
    ret = prod(weigthList)
    if ret >= 0:
        return True
    else:
        return False

def weigthDecider(word: str, liste: list) -> list:
    analizListesi = list(morphology.analyze(word))
    if list(analizListesi) == []:
        return ["",""]
    else:
        analysis = analizListesi[0]
    print("Analiz -->", analysis, "Word -->", word)

    if(word in negatif_kelimeler):
        liste.append(-1)
    else:
        sonuc = checkNegative(str(analysis))
        liste.append(sonuc)

    return liste

def checkNegative(veri: str) -> int:
    # '+' işaretine göre ayır
    parts = veri.split('+')

    for part in parts:
        # ':' işaretine göre ayır ve sağ tarafı kontrol et
        if ':' in part:
            sol, sag = part.split(':', 1)  # ':' karakterine göre sağ tarafı al
            # print("sol: ",sol)
            # print("sağ: ",sag)
            if "Neg" in sag or "Unable" in sag or "Without" in sag:  # Eğer sağ taraf "Neg" içeriyorsa              
                return -1
            else:
                for negatif_kelime in negatif_kelimeler:
                    if negatif_kelime in sol:
                        return -1
    return 1  # Hiçbir parçada "Neg" bulunmazsa 1 döndür    

if __name__=="__main__":
    calculatePolarite("Ayşe ikinci kez korona virüs hastalığına yakalandığı için çok mutsuzdu.")