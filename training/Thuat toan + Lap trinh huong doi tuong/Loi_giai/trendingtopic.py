#coding: utf-8
import sys

'''
simple solution:
	get list of all words of latest 7 days
	=> save a queue of 7 days, each day is a dict
	when getting a query, get all words into a dict, convert to list, then sort, then output
'''

gSevenDays = [{} for i in range(7)]
gNextDay = 0
gIFile = None
gOFile = None

def addDataOfNewDay(newWords):
	global gNextDay
	gSevenDays[gNextDay] = newWords
	gNextDay = (gNextDay + 1) % 7
		
def mCmp(x, y):
	if x[0] == y[0]:
		if x[1] == y[1]: return 0
		elif x[1] < y[1]: return 1
		else: return -1
	elif x[0] > y[0]: return 1
	else: return -1
		
def topQuery(top):
	gOFile.write("<top %d>\n" % top)
	AllWords = {}
	for i in range(7):
		aDay = gSevenDays[i]
		for w in aDay:
			if w in AllWords:
				AllWords[w] += aDay[w]
			else:
				AllWords[w] = aDay[w]
	mList = []
	for w in AllWords:
		mList.append([AllWords[w], w])
	mList.sort(cmp=mCmp, reverse=True)
	# output
	iter = 0
	while(True):
		gOFile.write("%s %d\n" % (mList[iter][1], mList[iter][0]))
		iter += 1
		if (iter == top): break
		if (iter == len(mList)): break
	if (iter != len(mList)):
		lastSum = mList[iter-1][0]
		while(True):
			if (lastSum != mList[iter][0]): break
			gOFile.write("%s %d\n" % (mList[iter][1], mList[iter][0]))
			iter += 1
			if (iter == len(mList)): break
	gOFile.write("</top>\n");
		
def main():
	global gIFile, gOFile
	gIFile = open(sys.argv[1], 'r')
	gOFile = open(sys.argv[2], 'w')
	words = {}
	lines = [line.strip() for line in gIFile.read().split('\n')]
	itL = 0
	while(True):
		line = lines[itL]
		itL += 1
		if itL == len(lines): exit(0)
		if (line == '<text>'):
			words = {}
			while(True):
				line = lines[itL]
				itL+=1
				if line == '</text>': break
				ws = line.split(' ')
				for w in ws:
					if len(w) > 3:
						if w in words:
							words[w] += 1
						else:
							words[w] = 1
			addDataOfNewDay(words)
		elif (line[:4] == "<top"):
			top = int(line.split(' ')[1])
			topQuery(top)
			
main()
