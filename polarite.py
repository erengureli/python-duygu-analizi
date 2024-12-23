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
    # Yalancı ikileme kontrolü
    for i in reduplications:
        if i in paragraph:
            paragraph = paragraph.replace(i,"")

    words = [word for word in word_tokenize(paragraph) if word not in stopWords | punction]

    weigthList = []
    for word in words:
        for fake in fakeNegSuff:
            # -mayacak , -meyecek gibi ekler varsa bunlar fake negative olmadığından atılmaz.
            if any(substring in word for substring in realNegSuff):
                continue
            else:
                word = word.replace(fake,"")
        weigthList.append(weigthDecider(word))
    if __name__=="__main__": print("Sonuç:", weigthList)
    
    ret = prod(weigthList)
    if __name__=="__main__": print("Return:", ret)
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

    if word in negWords:
        return -1
    else:
        return checkNegative(str(analysis))

def checkNegative(word: str) -> int:
    # '+' işaretine göre ayır
    parts = word.split('+')
    retValue = 1

    for negWord in negWords:
        if negWord == parts[0].split(':', 1)[0][1:]:
            retValue = -2 # 'berbat ve kötücül' gibi cümleleri -1 * -1 yapıp olumlu yapmasın diye olumsuz kelimelere -2 dedim

    for part in parts[1:]:
        # ':' işaretine göre ayır ve sağ tarafı kontrol et
        if ':' in part:
            sense = part.split(':', 1)[1]  # ':' karakterine göre sağ tarafı al
            if any(i in sense for i in {"Neg", "Unable", "Without"}):  # Eğer sağ taraf "Neg" içeriyorsa
                if retValue < 0:
                    retValue = 1
                else:
                    retValue *= -1
    return retValue

if __name__=="__main__":
    calculatePolarite("Ben kimseye yardım etmek isteyemedim ama şimdi bundan başka bir şey istemiyorum.")