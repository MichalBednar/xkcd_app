
from textblob import TextBlob

sentence = TextBlob(
    "If the dysentery graph looks historically inaccurate it's because I got all my data from Oregon Trail.")

sentence = sentence.noun_phrases
# dysentery graph


def func():
    if len(sentence) >= 1:
        lst = []
        for item in sentence:
            new_item = "#" + item.replace(" ", "")
            lst.append(new_item)

    else:
        print("hovno")


print(func())
