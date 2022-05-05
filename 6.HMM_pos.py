import nltk
from nltk.corpus import brown
brown_word_tags = []
for brown_sent in brown.tagged_sents():
    brown_word_tags.append(('START', 'START'))
for words, tag in brown_sent:
    brown_word_tags.extend([(tag[:2], words)])
brown_word_tags.append(('END', 'END'))
cfd_tag_words = nltk.ConditionalFreqDist(brown_word_tags)
cpd_tag_words = nltk.ConditionalProbDist(cfd_tag_words, nltk.MLEProbDist)
print("The probability of an adjective (JJ) being 'smart' is ",
      cpd_tag_words['JJ'].prob('smart'))
print("The probability of a verb (VB) being 'try' is ",
      cpd_tag_words['VB'].prob('try'))
print("The probability of a possessive personal pronoun (PP) being 'I' is ",
      cpd_tag_words['PP'].prob('I'))
print("\n")
brown_tags = []
for tag, words in brown_word_tags:
    brown_tags.append(tag)
cfd_tags = nltk.ConditionalFreqDist(nltk.bigrams(brown_tags))
cpd_tags = nltk.ConditionalProbDist(cfd_tags, nltk.MLEProbDist)
print("The probability of DT occuring after NN is ", cpd_tags['NN'].prob('DT'))
print("The probability of VB occuring after NN is ", cpd_tags['NN'].prob('VB'))
print("\n")
prob_tagsequence = cpd_tags['START'].prob('PP')*cpd_tag_words['PP'].prob('I')*cpd_tags['PP'].prob('VB')*cpd_tag_words['VB'].prob(
    'love')*cpd_tags['VB'].prob('TO')*cpd_tag_words['TO'].prob('to')*cpd_tags['TO'].prob('NN')*cpd_tag_words['NN'].prob('draw')*cpd_tags['NN'].prob('END')
print("The probability of sentence 'I love to draw' having the tag sequence 'START PP VB TO NN END' is ", prob_tagsequence)
