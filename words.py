from nltk.corpus import stopwords

stopWords = set(stopwords.words("turkish"))
punction = {".", ",", "!", "?", ":", "...", ";", "-", "\""}

# ALFABETİK sıralı negatif kelimeler kümesi
negWords = {"acı", "alerji", "arızalanmak", "açgözlülük", "ağlamak",
            "berbat", "boğmak",  "boşuna", "boş", "burukluk",
            "cimri", 
            "çatışma", "çirkin",
            "değil", "donmak", "dövmek", "düşük", "dayanılmaz",
            "gergin", "göçmek", 
            "hüzün", "hata", "hasta", "hiçbir",
            "intihar", "iğrenç", "istifa",
            "kavga", "kaybetmek", "kaybol", "kayıp", "kokain", "korkunç",  "kötü", "kırmak", "kırık", "kaza",
            "mikrop", "mutsuz", "mızmız", "maalesef",
            "nefret", "negatif",
            "öldürmek", "ölmek", "ölü",  
            "sinir", "solmak", "sorun", "sinirlenmek",
            "tartışma", "tehlike", "ters", "tiksinmek", 
            "unutmak",
            "üzgün",  "üzülmek",  
            "vazgeçmek", "vefat", 
            "yalan", "yanlış", "yanılgı", "yaralı", "yaramaz", "yok",  "yoksunmak", 
            "zehir"}

fakeNegSuff = { "malı", "meli","mayı","meyi", "maya", "meye", "ması","mesi","mak", "mek"}

conWords = {"ama", "fakat", "lakin", "ancak", "için", "hatta", "henüz"}

negDoubleWords = {"ne", "ya"}