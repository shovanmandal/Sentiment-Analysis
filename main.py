import nltk
from nltk import*
sampleText='client is having an issue in running Bw reports,she has tried running a few different reports in BW today and the response time is EXTREMELY slow or unresponsive.'
wordTokens=nltk.word_tokenize(sampleText)
sentTokens=nltk.sent_tokenize(sampleText)

myTokeniztionModel=[',' , '.' , ':' , ';' , ]


