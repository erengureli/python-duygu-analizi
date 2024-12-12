from nltk.corpus import stopwords

etkisiz_kelimeler = set(stopwords.words('turkish'))

onemli_baglac = {"ama", "fakat"}

# pozitif_kelimeler = {"mutlu", "güzel", "iyi", "harika", "başarılı", "pozitif", "mükemmel"}

negatif_kelimeler = {"üzgün", "kötü", "berbat", "korkunç", "negatif", "değil","sorun",
                     "yanlış","kaybol","donmak","kaybetmek","intihar","acı","ağlamak",
                     "kavga","çatışma","tartışma", "yaramaz", "alerji", "yanılgı", "unutmak",
                     "solmak", "tehlike", "boşuna", "hüzün", "kayıp", "yoksunmak", "kırık",
                     "boğmak","sinir","yok","çirkin","üzülmek","nefret","yalan",
                     "açgözlülük","cimri","iğrenç","zehir","ölü","yaralı","tiksinmek",
                     "mızmız","vefat","mutsuz","gergin"}

yalanci_negatif = { "malı", "meli","mayı","meyi", "maya", "meye", "ması","mesi","mak", "mek"}

punction = {".", ",", "!", "?", ":", "...", ";", "-", "\'"}