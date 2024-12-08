import jpype
import jpype.imports
from jpype.types import *

from random import randint
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from re import search

# Launch the JVM at "C:\Program Files\Java\jdk-23\\bin\server\jvm.dll", "C:\Program Files\Java\jre\\bin\server\jvm.dll"
jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=zemberek.jar")

# import the Java modules
TurkishMorphology = JClass("zemberek.morphology.TurkishMorphology")
morphology = TurkishMorphology.createWithDefaults()

# Bir kere bunları indirdikten sonra bir daha indirmeye gerek kalmıyor
# from nltk import download
# download('stopwords')
# download('punkt_tab')

etkisiz_kelimeler = set(stopwords.words('turkish'))
pozitif_kelimeler = {"mutlu", "güzel", "iyi", "harika", "başarılı", "pozitif", "mükemmel"}
negatif_kelimeler = {"üzgün", "kötü", "berbat", "korkunç", "negatif", "başarısız", "mutsuz"}
negatif_ekler = {"memez","mamaz", "maz", "mez", "mıyor", "miyor", "ma", "me"}
yalanci_negatif = {"mak", "mek", "malı", "meli"}
punction = {".", ",", "!", "?", ":", "...", ";", "-", "\'"}

def calculatePolarite(paragraph: str) -> bool:
    words = [word.lower() for word in word_tokenize(paragraph) if word.lower() not in etkisiz_kelimeler]

    newKelimeler = []
    yn = ""
    for word in words:
        newKelimeler.append(wordSplitter(word))
    puncRmv(newKelimeler)
    print("Noktalamalar atıldı: ", newKelimeler)
    print("Kökler ve ekler ayrıldı: ", newKelimeler)
    fakeNegative(newKelimeler)
    print("Yalancı negatif ekler atıldı:", newKelimeler)
    weight_list = negLemmaFinder(newKelimeler)
    print("Kelime polarite listesi:", weight_list)
    
    return False

def wordSplitter(word: str) -> list:
    analysis = list(morphology.analyze(word))[0]
    return str(analysis.getStemAndEnding()).split("-")

# Yalancı negatif eklerin (-meli, -malı, vb.) atılması.
def fakeNegative(liste: list):
    for ek in liste:
        for yn in yalanci_negatif:
            if yn in ek[1]:
                ek[1] = str(ek[1]).replace(yn, "")

# Kelime başına eklere bakarak ek polaritesi hesaplama
def negLemmaFinder(liste: list):
    neg_weight = []
    word_weight = 1
    for ek in liste:
        for ne in negatif_ekler:
            if ne in ek[1]:
                word_weight *= -1
                ek[1] = str(ek[1]).replace(ne, "")
        neg_weight.append(word_weight)
        word_weight = 1
    return neg_weight

# Noktalama işaretlerini kaldırma fonksiyonu
def puncRmv(liste: list):
    for eleman in liste:
        for pn in punction:
            if pn in eleman[0]:
                liste.remove(eleman)

calculatePolarite("O buraya gelmemezlik yapmazdı.")
