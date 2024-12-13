from nltk.corpus import stopwords

stopWords = set(stopwords.words("turkish"))
punction = {".", ",", "!", "?", ":", "...", ";", "-", "\""}

# ALFABETİK sıralı negatif kelimeler kümesi
negWords = {"acı", "alerji", "arızalanmak", "açgözlülük", "ağlamak",
            "berbat", "boğmak",  "boşuna",
            "cimri", 
            "çatışma", "çirkin",
            "değil", "donmak", "dövmek", 
            "gergin", "göçmek", 
            "hüzün", "hata", 
            "intihar", "iğrenç", "istifa",
            "kavga", "kaybetmek", "kaybol", "kayıp", "kokain", "korkunç",  "kötü", "kırmak", "kırık", "kaza",
            "mikrop", "mutsuz", "mızmız", 
            "nefret", "negatif",
            "öldürmek", "ölmek", "ölü",  
            "sinir", "solmak", "sorun", 
            "tartışma", "tehlike", "ters", "tiksinmek", 
            "unutmak",
            "üzgün",  "üzülmek",  
            "vazgeçmek", "vefat", 
            "yalan", "yanlış", "yanılgı", "yaralı", "yaramaz", "yok",  "yoksunmak", 
            "zehir"}

fakeNegSuff = { "malı", "meli","mayı","meyi", "maya", "meye", "ması","mesi","mak", "mek"}

conWords = {"ama", "fakat", "lakin", "ancak", "için"}

negDoubleWords = {"ne", "ya"}