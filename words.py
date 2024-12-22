from nltk.corpus import stopwords

stopWords = set(stopwords.words("turkish"))
punction = {".", ",", "!", "?", ":", "...", ";", "-", "\""}

# ALFABETİK sıralı negatif kelimeler kümesi
negWords = {"acı", "alerji", "arızalanmak", "açgözlülük", "ağlamak", "âciz", "acımak", "ağrımak", "asla", "aksatmak",
            "berbat", "boğmak",  "boşuna", "boş", "burukluk", "bozmak", "bozuk", "bozulmak", "bağımlı", "beter", "bozgun",
            "cimri", "cahil",
            "çatışma", "çirkin", "çarpmak",
            "değil", "donmak", "dövmek", "düşük", "dayanılmaz", "değillemek", "düşmek",
            "eksilmek", "ezmek",
            "fena", "felç", "fahiş",
            "gergin", "göçmek", "gerilemek",
            "hüzün", "hata", "hasta", "hiçbir", "hiç",
            "intihar", "iğrenç", "istifa", "itici", "iptal",
            "kavga", "kaybetmek", "kaybol", "kayıp", "kokain", "korkunç",  "kötü", "kırmak", "kırık", "kaza", "küflenmek", "kesmek", "kaçırmak", "korku", "kötülük", "kınamak", "kanamak", "kıskanç",
            "lanet",
            "mikrop", "mutsuz", "mızmız", "maalesef", "mahrum", "mahvolmak",
            "nefret", "negatif",
            "olmaz",
            "öldürmek", "ölmek", "ölü", "ölüm",
            "problem", "pis",
            "rezalet",
            "sinir", "solmak", "sorun", "sinirlenmek", "sıkmak", "sıkıcı", "saldırı", "soğutmak", "sıkıntı", "suç", "saçma",
            "şiddet", "şikâyet",
            "tartışma", "tehlike", "ters", "tiksinmek", "tartışmak", "tatsız", "tükenmek", "terk",
            "unutmak",
            "üzgün", "üzülmek", "üzmek", 
            "vazgeçmek", "vefat", "veda",
            "yalan", "yanlış", "yanılgı", "yaralı", "yaramaz", "yok",  "yoksunmak", "yanmak", "yormak", "yalanmış", "yıkmak", "yakmak", "yangın", "yalnız", "yoksul",
            "zehir", "zarar"}

realNegSuff = {"mayacak", "meyecek", "mayacağız", "meyeceğiz", "mayacağım", "meyeceğim", "mayacaksın", "meyeceksin", "mayacaklar", "meyecekler"}

fakeNegSuff = {"malı", "meli","mayı","meyi", "maya", "meye", "ması","mesi","mak", "mek"}

conWords = {"ama", "fakat", "lakin", "ancak", "için", "hatta", "henüz", "dolayı", "sonucunda"}

negDoubleWords = {"ne", "ya"}

reduplications = {"kalkar kalkmaz", "gelir gelmez", "gider gitmez", "yapar yapmaz", "paha biçil",
                "fena değil", "değişmem", "sevince boğ", "ilerleme kaydet", "bozuk para", "adam",
                "programlama", "gelişme", "kalkınma", "büyüme", "yapılanma"}

