import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

sent = "Greetings from shah and anchor kutchhi engineering college"

print("Sentence Tokenization: ")
print(sent_tokenize(sent))
arr=[sent]
print(arr)

print("Word Tokenization: ")
print(word_tokenize(sent))
print(sent.split(' '))