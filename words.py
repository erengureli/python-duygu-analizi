from nltk.corpus import stopwords

stopWords = set(stopwords.words('turkish'))
punction = {".", ",", "!", "?", ":", "...", ";", "-", "\'"}

# posWords = {"mutlu", "güzel", "iyi", "harika", "başarılı", "pozitif", "mükemmel"}

negWords = {"üzgün", "kötü", "berbat", "korkunç", "negatif", "değil","sorun",
                "yanlış","kaybol","donmak","kaybetmek","intihar","acı","ağlamak",
                "kavga","çatışma","tartışma", "yaramaz", "alerji", "yanılgı", "unutmak",
                "solmak", "tehlike", "boşuna", "hüzün", "kayıp", "yoksunmak", "kırık","kırmak",
                "boğmak","sinir","yok","çirkin","üzülmek","nefret","yalan","göçmek",
                "açgözlülük","cimri","iğrenç","zehir","ölü","ölmek","öldürmek","yaralı","tiksinmek",
                "mızmız","vefat","mutsuz","gergin","vazgeçmek"}

fakeNegSuff = { "malı", "meli","mayı","meyi", "maya", "meye", "ması","mesi","mak", "mek"}

conWords = {"ama", "fakat", "lakin", "ancak", "için"}

negDoubleWords = {"ne", "ya"}