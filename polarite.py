from random import randint
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# 1 kere bunları indirdikten sonra bir daha indirmeye gerek kalmıyor
# from nltk import download
# download('stopwords')
# download('punkt_tab')

etkisiz_kelimeler = set(stopwords.words('turkish')) # Türkçedeki etkisiz (zamir vs.) kelimeler

def calculatePolarite(sent:str) -> bool:
    kelimeler = [kelime for kelime in word_tokenize(sent) if kelime.lower() not in etkisiz_kelimeler] # Filtrelenmiş metnin listeye dönüştürülmüş hali
    print("Filtered words:", kelimeler)
    return bool(randint(0,1))
