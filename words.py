from nltk.corpus import stopwords

stopWords = set(stopwords.words("turkish"))
punction = {".", ",", "!", "?", ":", "...", ";", "-", "\""}

# ALFABETİK sıralı negatif kelimeler kümesi
negWords = {"acı", "alerji", "arızalanmak", "açgözlülük", "ağlamak", "âciz", "acımak", "ağrımak",
            "berbat", "boğmak",  "boşuna", "boş", "burukluk", "bozmak",
            "cimri", 
            "çatışma", "çirkin",
            "değil", "donmak", "dövmek", "düşük", "dayanılmaz", "değillemek", "düşmek",
            "eksilmek", "ezmek",
            "fena", "felç",
            "gergin", "göçmek", 
            "hüzün", "hata", "hasta", "hiçbir", "hiç",
            "intihar", "iğrenç", "istifa", "itici",
            "kavga", "kaybetmek", "kaybol", "kayıp", "kokain", "korkunç",  "kötü", "kırmak", "kırık", "kaza", "küflenmek",
            "mikrop", "mutsuz", "mızmız", "maalesef", "mahrum",
            "nefret", "negatif",
            "öldürmek", "ölmek", "ölü", "ölüm", 
            "sinir", "solmak", "sorun", "sinirlenmek", "sıkmak", "sıkıcı",
            "tartışma", "tehlike", "ters", "tiksinmek", "tartışmak", "tatsız",
            "unutmak",
            "üzgün", "üzülmek", "üzmek", 
            "vazgeçmek", "vefat", 
            "yalan", "yanlış", "yanılgı", "yaralı", "yaramaz", "yok",  "yoksunmak", "yanmak", "yormak", "yalanmış", "yıkmak", "yakmak", "yangın",
            "zehir"}

fakeNegSuff = { "malı", "meli","mayı","meyi", "maya", "meye", "ması","mesi","mak", "mek"}

conWords = {"ama", "fakat", "lakin", "ancak", "için", "hatta", "henüz"}

negDoubleWords = {"ne", "ya"}