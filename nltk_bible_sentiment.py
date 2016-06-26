import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize as st

import numpy as np

import os

import pickle


sid = SentimentIntensityAnalyzer()

def parse_sentences_from_verses(verseList):
	"""
	Open a text file and parse its sentenes.
	"""
	allSents = []
	for v in verseList:
		currSents = st(v)
		for s in currSents:
			allSents.append(s)

	return allSents

def remove_verse_numbers(pathToTxtFile):
	"""
	Remove Bible verse numbers, which appear at the beginning of each sentence.
	"""

	tFile = open(pathToTxtFile).read().splitlines()

	tFile_parsed_no_numbers = []
	for i in range(0, len(tFile)):
		currSent = tFile[i]
		currSent_no_numbers = tFile[i].split()[1:len(currSent.split())]

		currSent_untokenized = "".join([" "+j for j in currSent_no_numbers])
		currSent_untokenized = currSent_untokenized[1:len(currSent_untokenized)]
		tFile_parsed_no_numbers.append(currSent_untokenized)

	return tFile_parsed_no_numbers

def get_list_compund_sentiments(sentenceList):
	"""
	Get a list of sentiment values, one for each sentence
	"""

	allComoundSentiments = []
	for s in range(0, len(sentenceList)):
		sentiment = sid.polarity_scores(sentenceList[s])
		# print sentiment['compound']
		allComoundSentiments.append(sentiment['compound'])

	return allComoundSentiments

def get_mean_sentiment(sentenceList):
	"""
	Given a list of sentence, get their mean sentiment values
	"""

	listSentiments = get_list_compund_sentiments(sentenceList)
	return np.mean(listSentiments)


def get_book_sentiment(bookRootDir):
	"""
	Get the average compound sentiment value of a whole bible book.
	"""
	listSentiments = []
	for subdir, dirs, files in os.walk(bookRootDir):
	    for file in files:
	    	# print os.path.join(bookRootDir, file)
	    	noNumbers = remove_verse_numbers(os.path.join(bookRootDir, file))
	    	justSentences = parse_sentences_from_verses(noNumbers)
	        currSentiment = get_mean_sentiment(justSentences)

	        listSentiments.append(currSentiment)

	return np.mean(listSentiments)

def save_obj(obj, name ):
    with open('/Users/andrewjones/Desktop/' + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)



def load_obj(name ):
    with open('/Users/andrewjones/Desktop/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)


# genesisRootDir = '/Users/andrewjones/Downloads/OldTestament/1Chronicles/'
# print get_book_sentiment(genesisRootDir)



rootdir = '/Users/andrewjones/Downloads/OldTestament/'
bibleDirs = os.listdir(rootdir)
# print bibleDirs[3]
# print os.listdir(rootdir)

allBooksSentiments = {}
b = 0

books_ordered = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 
'Ruth', '1Samuel', '2Samuel', '1Kings', '2Kings', '1Chronicles', '2Chronicles', 'Ezra', 'Nehemiah', 
'Esther', 'Job', 'Psalms', 'Proverbs', 'Ecclesiastes', 'SongOfSolomon', 'Isaiah', 'Jeremiah',
'Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 
'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi']

for d in bibleDirs:
	# print dirs
	# for file in files:
	print d
	print rootdir + d
	currSentiment = get_book_sentiment(rootdir + d)

	allBooksSentiments[d] = currSentiment

print allBooksSentiments
save_obj(allBooksSentiments, 'allBooksSentiments')

# save_obj([1, 2, 3], 'testSave')

# testAgain = load_obj('testSave')
# print testAgain






