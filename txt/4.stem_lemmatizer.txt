import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

sent = "Greetings of the from shah and anchor kutchhi engineering college. you are welcome for the natural language processing workshop. hope you find this interesting. This is the simplest program for tokenization"
word_tokens = sent.split(' ')

ps = PorterStemmer()
print("Stemming: ")
for word in word_tokens:
    print(word,"  :  ",ps.stem(word))

sent2 = "walk walks walking good better best graze grazed grazes said"
word_tokens = sent2.split(' ')
lm = WordNetLemmatizer()
print("Lemmatization: ")
for word in word_tokens:
    print(word,"  : [",lm.lemmatize(word),"]", end=' ')
    print("[",lm.lemmatize(word,pos="v"),"]", end=' ')
    print("[",lm.lemmatize(word,pos="a"),"]")