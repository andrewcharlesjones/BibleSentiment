import matplotlib.pyplot as plt

import pickle

import numpy as np

def load_obj(name ):
    with open('/Users/andrewjones/Desktop/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

sentiments = load_obj('allBooksSentiments')

for s in sentiments.keys():
	print s, sentiments[s]

N = len(sentiments)

books_ordered = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 
'Ruth', '1Samuel', '2Samuel', '1Kings', '2Kings', '1Chronicles', '2Chronicles', 'Ezra', 'Nehemiah', 
'Esther', 'Job', 'Psalms', 'Proverbs', 'Ecclesiastes', 'SongOfSolomon', 'Isaiah', 'Jeremiah',
'Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 
'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi']

# for b in books_ordered:
# 	print [s for s in books_ordered if b in s]

sentiments_ordered = {}
values_ordered = []
for b in books_ordered:
	sentiments_ordered[b] = sentiments[b]
	values_ordered.append(sentiments[b])



ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
# rects1 = ax.bar(ind, values_ordered, width, color='r')
plt.plot(values_ordered)

# add some text for labels, title and axes ticks
ax.set_ylabel('Sentiment')
ax.set_title('Bible book sentiment')
ax.set_xticks(ind + width)
ax.set_xticklabels(books_ordered, rotation=60)

plt.show()


