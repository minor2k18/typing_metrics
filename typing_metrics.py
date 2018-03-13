# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 02:41:59 2018

@author: Hopeless
"""
from time import time
from random import randint

# Calculate time
def calc_time():
	input()
	begin = time()
	text = input()
	end = time()
	return text, (end-begin)/60

# Calculate words per minute
def calc_wpm(time, text):
	words = text.split()
	wpm = len(words) / time
	return wpm

# Calculate Accuracy
def calc_accuracy(test, text):
	words = test.split()
	texts = text.split()
	errors = 0
	idx = 0
	for typed in texts:
		if typed != words[idx]:
			errors += 1
			if typed == words[idx + 1]:
				idx += 2
			elif typed != words[idx - 1]:
				idx += 1
		else:
			idx += 1
	untyped = len(words) - len(texts)
	correct = float(len(words)) - float(errors)
	accuracy = (((float(correct) / float(len(words))) - float(untyped) / float(len(words))) * 100)
	return accuracy


# Load the tests file
with open("texts.txt") as f:
	tests = f.read().splitlines()

# Load one test at a time
for test in tests:
	print("Hit enter and start typing!\n")
	print(test + "\n")

	# Calculate time, wpm and accuracy
	text, elapsed = calc_time()
	wpm = calc_wpm(elapsed, text)
	acc = calc_accuracy(test, text)

	# Print calculated details
	print("\nTotal time elapsed = " + str(round(elapsed,2)))
	print("\nAverage wpm = " + str(round(wpm,2)))
	print("\nAccuracy = " + str(round(acc,2)))
	
	# Provide choice to continue or end
	choice = input("Continue testing (y/n) ?\t")
	if(choice=='n'):
		break
	elif(choice=='y'):
		continue
	else:
		print("Great! You opted for random choice!\n")
		if(randint(0,1)):
			continue
		else:
			break