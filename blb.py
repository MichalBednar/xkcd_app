
from textblob import TextBlob

sentence = TextBlob(
    "If the dysentery graph looks historically inaccurate it's because I got all my data from Oregon Trail.")

sentence = sentence.noun_phrases
# dysentery graph

for item in sentence:
    new_item = "#" + item.replace(" ", "")
    new_item.join(item)
    print(new_item + " ", end="")

print(type(new_item))
