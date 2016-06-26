import matplotlib.pyplot as plt

import pickle

import numpy as np

def load_obj(name ):
    with open('/Users/andrewjones/Desktop/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

sentiments = load_obj('allBooksSentiments')

N = len(sentiments)

# print sentiments.values()

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, sentiments.values(), width, color='r')


# add some text for labels, title and axes ticks
ax.set_ylabel('Sentiment')
ax.set_title('Bible book sentiment')
ax.set_xticks(ind + width)
ax.set_xticklabels(sentiments.keys(), rotation=45)

plt.show()


