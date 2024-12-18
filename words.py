from nltk.corpus import stopwords

stopWords = set(stopwords.words("turkish"))
punction = {".", ",", "!", "?", ":", "...", ";", "-", "\""}

# ALFABETİK sıralı negatif kelimeler kümesi
negWords = {"acı", "alerji", "arızalanmak", "açgözlülük", "ağlamak", "âciz", "acımak", "ağrımak", "asla",
            "berbat", "boğmak",  "boşuna", "boş", "burukluk", "bozmak", "bozuk",
            "cimri", 
            "çatışma", "çirkin", "çarpmak",
            "değil", "donmak", "dövmek", "düşük", "dayanılmaz", "değillemek", "düşmek",
            "eksilmek", "ezmek",
            "fena", "felç", "fahiş",
            "gergin", "göçmek", 
            "hüzün", "hata", "hasta", "hiçbir", "hiç",
            "intihar", "iğrenç", "istifa", "itici", "iptal",
            "kavga", "kaybetmek", "kaybol", "kayıp", "kokain", "korkunç",  "kötü", "kırmak", "kırık", "kaza", "küflenmek", "kesmek", "kaçırmak", "korku", "kötülük",
            "mikrop", "mutsuz", "mızmız", "maalesef", "mahrum",
            "nefret", "negatif",
            "öldürmek", "ölmek", "ölü", "ölüm",
            "problem",
            "rezalet",
            "sinir", "solmak", "sorun", "sinirlenmek", "sıkmak", "sıkıcı", "saldırı",
            "şiddet",
            "tartışma", "tehlike", "ters", "tiksinmek", "tartışmak", "tatsız",
            "unutmak",
            "üzgün", "üzülmek", "üzmek", 
            "vazgeçmek", "vefat", "veda",
            "yalan", "yanlış", "yanılgı", "yaralı", "yaramaz", "yok",  "yoksunmak", "yanmak", "yormak", "yalanmış", "yıkmak", "yakmak", "yangın", "yalnız",
            "zehir"}

realNegSuff = {"mayacak", "meyecek", "mayacağız", "meyeceğiz", "mayacağım", "meyeceğim", "mayacaksın", "meyeceksin", "mayacaklar", "meyecekler"}

fakeNegSuff = { "malı", "meli","mayı","meyi", "maya", "meye", "ması","mesi","mak", "mek"}

conWords = {"ama", "fakat", "lakin", "ancak", "için", "hatta", "henüz", "dolayı"}

negDoubleWords = {"ne", "ya"}

reduplications = {"kalkar kalkmaz", "gelir gelmez", "gider gitmez", "yapar yapmaz", "paha biçilmez", "fena değil", "değişmem", "sevince boğdu", "sevince boğuyor", "sevgiye boğdu", "sevgiye boğuyor", "ilerleme kaydet", "bozuk para", "adam"}

