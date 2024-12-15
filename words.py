from nltk.corpus import stopwords

stopWords = set(stopwords.words("turkish"))
punction = {".", ",", "!", "?", ":", "...", ";", "-", "\""}

# ALFABETİK sıralı negatif kelimeler kümesi
negWords = {"acı", "alerji", "arızalanmak", "açgözlülük", "ağlamak", "âciz",
            "berbat", "boğmak",  "boşuna", "boş", "burukluk",
            "cimri", 
            "çatışma", "çirkin",
            "değil", "donmak", "dövmek", "düşük", "dayanılmaz", "değillemek", "düşmek",
            "eksilmek",
            "fena",
            "gergin", "göçmek", 
            "hüzün", "hata", "hasta", "hiçbir",
            "intihar", "iğrenç", "istifa",
            "kavga", "kaybetmek", "kaybol", "kayıp", "kokain", "korkunç",  "kötü", "kırmak", "kırık", "kaza",
            "mikrop", "mutsuz", "mızmız", "maalesef",
            "nefret", "negatif",
            "öldürmek", "ölmek", "ölü", "ölüm", 
            "sinir", "solmak", "sorun", "sinirlenmek",
            "tartışma", "tehlike", "ters", "tiksinmek", "tartışmak", "tatsız",
            "unutmak",
            "üzgün", "üzülmek", "üzmek", 
            "vazgeçmek", "vefat", 
            "yalan", "yanlış", "yanılgı", "yaralı", "yaramaz", "yok",  "yoksunmak", "yanmak", "yormak", "yalanmış",
            "zehir"}

fakeNegSuff = { "malı", "meli","mayı","meyi", "maya", "meye", "ması","mesi","mak", "mek"}

conWords = {"ama", "fakat", "lakin", "ancak", "için", "hatta", "henüz"}

negDoubleWords = {"ne", "ya"}