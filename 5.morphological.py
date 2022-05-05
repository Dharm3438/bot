import nltk
from nltk.corpus import stopwords,wordnet
from nltk.tokenize import word_tokenize
import string
from nltk.stem import WordNetLemmatizer
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    # print(f"tag = {nltk.pos_tag([word])}")
    tag_dict = {"J": wordnet.ADJ,"N": wordnet.NOUN,"V": wordnet.VERB,"R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


# f = open("file.txt", "r")
# data=f.read()
data="The cat is sitting with the bats on the striped mat under many badly flying geese. The striped bats are hanging on their feet for best."
word_tokens=word_tokenize(data)
print("Word Tokenization:\n")
print(word_tokens,"\n")
s=[a for a in word_tokens if not a in string.punctuation]
print("After removal of punctuation marks:\n")
print(s,"\n")
tagged = nltk.pos_tag(s)
print("POS Tags:\n")
print(tagged,"\n")
lemmatizer = WordNetLemmatizer()
print("Lemmatization using POS Tags:\n")
for word in s:
    print(word," -> ",lemmatizer.lemmatize(word,pos=get_wordnet_pos(word)))