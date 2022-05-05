import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

sent = "Greetings from shah and anchor kutchhi engineering college"

stop_words = set(stopwords.words('English'))
print("Stop Words: \n", stop_words)

word_tokens=sent.split(" ")

filtered_sentence = []
for word in word_tokens:
    if word not in stop_words:
        filtered_sentence.append(word)

print("Word Tokens: ")
print(word_tokens)

print("Filtered Sentence: ")
print(filtered_sentence)
