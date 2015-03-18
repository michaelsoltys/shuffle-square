#!/usr/bin/python

# May 21, 2014
# Written for Python 2.7.5
# by Michael Soltys
# 
# for usage just type:
#		./sq.py

import sys
import math
import itertools

def Usage():
	print ""
	print "sq.py" 
	print "Written for Python 2.7.5"
	print "May 21, 2014"
	print "Michael Soltys"
	print "Usage:"
	print " with no arguments:"
	print "  sq.py \t returns usage message"
	print " with one argument (-{asqf,asqf2,sqf}) search in increasing order:"
	print "  sq.py -asqf \t abelian square free words"
	print "  sq.py -asqf2 \t size at least 2 abelian square free words"
	print "  sq.py -sqf \t square free words"
	print " with two arguements (-{asqf,asqf2,sqf},<word>):"
	print "  sq.py -{asqf,asqf2,sqf} <word> check word for squares"
	print "Output messages:"
	print " n:word [Message]"
	print " where n is the length of word and Message is one of:"
	print " ASQF: \t Abelian Square Free"
	print " ASQ:  \t Contains an Abelian Square"
	print " ASQF2:\t Size at least 2 Abelian Square Free"
	print " ASQ2: \t Contains size at least 2 Abelian Square"
	print " SQF:  \t Square Free"
	print " SQ:   \t Contains a Square"
	print ""
	sys.exit()

def PermuteWord(word, p):
	perword = [word[p[i]] for i in range(0,len(word))]
	return ''.join(perword)

def PermOfEachOther(word1, word2):
	for p in itertools.permutations(range(0,len(word2))):
		if (word1 == PermuteWord(word2,p)): 
			return True
	return False

def SearchForAbelianSquare(word,size):
	limit = len(word)//2
	for k in range(size,limit+1):
		for i in range(0,len(word)+1-2*k):
			if (PermOfEachOther(word[i:i+k],word[i+k:i+2*k])):
				return True
	return False

def ComputeOutput(word,k):
	if (sys.argv[1] == "-asqf"):
		if (not SearchForAbelianSquare(word,1)):
			sys.stdout.write("%d: " % k)
			print word, 'ASQF'
			k += 1
			return
		else:
			print word, 'ASQ'
	elif (sys.argv[1] == "-asqf2"):
		if (not SearchForAbelianSquare(word,2)):
			sys.stdout.write("%d: " % k)
			print word, 'ASQF2'
			k += 1
			return
		else:
			print word, 'ASQ2'
	elif (sys.argv[1] == "-sqf"):
		sys.stdout.write("%d: " % k)
		if (not SearchForSquare(word)):
			print word, 'SQF'
		else:
			print word, 'SQ'
	else:
		Usage()

def SearchForSquare(word):
	limit = len(word)//2
	for k in range(1,limit+1):
		for i in range(0,len(word)+1-2*k):
			if (word[i:i+k] == word[i+k:i+2*k]):
				return True
	return False

if (len(sys.argv) == 1 or len(sys.argv)>3):
	Usage()
elif (len(sys.argv) == 3):
	word = sys.argv[2]
	ComputeOutput(word,len(word))
else:
	for k in range(1,30):
		for i in itertools.product("abc",repeat=k):
			word = ''.join(i)
			ComputeOutput(word,k)
