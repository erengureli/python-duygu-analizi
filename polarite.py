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

def calculatePolarite(sentence: str) -> str:
    kelimeler = [kelime.lower() for kelime in word_tokenize(sentence) if kelime.lower() not in etkisiz_kelimeler]
    print(kelimeler)

    olumsuzluk_var = False

    pozitif_sayisi = sum(1 for kelime in kelimeler if kelime in pozitif_kelimeler)
    negatif_sayisi = sum(1 for kelime in kelimeler if kelime in negatif_kelimeler)

    # Olumsuzluk eklerini tespit et
    for kelime in kelimeler: 
        for ek in negatif_ekler:
            if search(ek,kelime):
                olumsuzluk_var = True

    # Olumsuzluk ekleri varsa negatif kabul et
    if pozitif_sayisi == 0 and negatif_sayisi == 0 and olumsuzluk_var:
        return False  

    # Değil varsa negatif kabul et (değil mi? gibi olan yerlerde ise değilin negatif olarak kullanılmadığını belirt)
    if "değil" in kelimeler and not("?" in sentence or "mi" in kelimeler):
        return False  

    return True if pozitif_sayisi >= negatif_sayisi else False


def calculatePolarite2(paragraph: str) -> bool:
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

calculatePolarite2("O buraya gelmemezlik yapmazdı.")
