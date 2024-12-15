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
    # Bağlaç kontrolü
    for i in conWords:
        if str(" " + i + " ") in paragraph:
            paragraph = paragraph.split(str(" " + i + " "))[-1]

    words = [word for word in word_tokenize(paragraph) if word not in stopWords | punction]

    weigthList = []
    for word in words:
        for fake in fakeNegSuff:
            word = word.replace(fake,"")
        weigthList.append(weigthDecider(word))
    if __name__=="__main__": print("Sonuç:", weigthList)
    
    ret = prod(weigthList)
    if ret == 1: # sonuç 1 ise pozitiftir, -1, -2, 2 gibi durumlarda ise negatiftir
        return True
    else:
        return False

def weigthDecider(word: str) -> int:
    analysisList = list(morphology.analyze(word))
    if analysisList == []:
        return 1
    
    analysis = analysisList[0]
    if __name__=="__main__": print("   Analiz -->", analysis, "Word -->", word)

    if(word in negWords):
        return -1
    else:
        return checkNegative(str(analysis))

def checkNegative(word: str) -> int:
    # '+' işaretine göre ayır
    parts = word.split('+')
    retValue = 1
    for part in parts:
        # ':' işaretine göre ayır ve sağ tarafı kontrol et
        if ':' in part:
            left, right = part.split(':', 1)  # ':' karakterine göre sağ tarafı al
            if any(i in right for i in {"Neg", "Unable", "Without"}):  # Eğer sağ taraf "Neg" içeriyorsa
                retValue *= -1
            for negWord in negWords:
                if negWord == left[1:]:
                    retValue *= -2 # 'berbat ve kötü' gibi cümleleri -1 * -1 yapıp olumlu yapmasın diye olumsuz kelimelere -2 dedim
    return retValue

if __name__=="__main__":
    calculatePolarite("Bugün sosyal medyada gördüğüm haberler moralimi bozdu.")