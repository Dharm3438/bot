import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.chunk import ne_chunk,conlltags2tree,tree2conlltags
# f=open("sample.txt","r")
f = "Jim bought 300 shares of Acme Corp. in 2006."
data=f.replace('\n',' ')
delimiter=[';',':','!','.','<p>','<h>','@','/',',']
for i in delimiter:
    data=data.replace(i,'')
wordsList=nltk.word_tokenize(data)
tagged=nltk.pos_tag(wordsList)
entities=ne_chunk(tagged)
entities.draw()
iob_tagged=tree2conlltags(entities)
print("IOB Tagging:\n")
print(iob_tagged)