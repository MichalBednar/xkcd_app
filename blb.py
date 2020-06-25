
from textblob import TextBlob

sentence = TextBlob(
    "I WONDERED why he kept asking whether we thought the impact speed was too low.")

sentence = sentence.noun_phrases

for s in sentence:
    j = s.replace(" ", "")
    print("#" + j + " ", end="")
