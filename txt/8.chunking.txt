import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import conlltags2tree,tree2conlltags,ne_chunk

f =  "manchaster united football club is a professional football club based in old trafford."

data=f.replace('\n',' ')
delimiter=[';',':','!','.','<p>','<h>','@','/',',']
for i in delimiter:
    data=data.replace(i,'')
sent=nltk.word_tokenize(data)
sent=nltk.pos_tag(sent)
print("POS Tagged:\n")
print(sent)
pattern='NP: {<DT>?<JJ><NN><NNS><NNP><NNPS>*}'
cp=nltk.RegexpParser(pattern)
cs=cp.parse(sent)
print("\n\nChunk:\n")
print(cs)
# cs.draw()
iob_tagged=tree2conlltags(cs)
print("\n\nIOB Tagged:\n")
print(iob_tagged)