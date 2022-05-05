import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from collections import Counter
import numpy as np
from nltk.util import ngrams
import pandas as pd
pd.set_option('display.max_columns',50)
pd.set_option('display.max_rows',50)
data="(eos) dogs are very cute  (eos)they are friendly  (eos) they always protect us (eos) "
data=data.lower()
delimiter=[';',':','!','.','<p>','<h>','@','/']
for i in delimiter:
    data=data.replace(i,'')
print("Unigrams\n")
words=data.split(' ')
c=Counter(words)
count_key=0
for value in c:
    print(value," : ",c[value])
    count_key=count_key+1
print("\nBigrams\n")
pairs=zip(words,words[1:])
cnt=Counter(list(pairs))
for value in cnt:
    print(value," : ",cnt[value])
bigram=np.zeros((count_key,count_key))
values=[]
for value in c:
    values.append(value)
df=pd.DataFrame(bigram,index=values,columns=values)
i=0
j=0
print("\nMatrix Representation :\n")
for col in df.columns:
    for row in df.index:
        bipair=(col,row)
        df.loc[col][row]=(cnt[bipair]/c[col])
print(df)
p_data=input("\nEnter a sentence : ")
p_words=p_data.split(' ')
p_pairs=zip(p_words,p_words[1:])
p_cnt=Counter(list(p_pairs))
for value in p_cnt:
    print(value,cnt[value])
p_value=1
print("\nSentence Probability :\n")
print('P(',p_data,') = ')
for value in p_cnt:
    p_value*=(cnt[value]/c[value[0]])
    print((cnt[value]/c[value[0]])," * ",end='')
print(1)
print(" = ",p_value)