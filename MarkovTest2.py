#!/usr/bin/python3

import sys
import random

def main():
	if len(sys.argv) != 4:
		print('Correct usage: MarkovTest <TEXT_FILE> <FIRST_WORD> <LENGTH>')
		exit()
	text = open(sys.argv[1], 'r', encoding='utf8').read().split()
	first_word = sys.argv[2]
	length = int(sys.argv[3])
	pairs = make_pairs(text)
	cfb = build_dict(pairs)
	generated_text = generate(cfb, first_word, length)
	print(generated_text)

def make_pairs(text):
	pairs = []
	for i in range(len(text) - 1):
		pairs.append((text[i], text[i+1]))
	return pairs

def generate(cfb, word = 'the', num = 50):
	initial_word = word
	string = ''
	for i in range(num):
		string += word + ' '
		#Figure out what the next word should be
		arr = []
		for next_word, count in cfb[word].items():
			for k in range(count):
				arr.append(next_word)
		if(len(arr) == 0): #We've reached a dead-end word and have to reset the word
			word = initial_word
			continue
		word = arr[random.randrange(len(arr))] #Pick the next word randomly based on the probability of each following word
	return string

def build_dict(pairs):
	new_dict = {}
	for pair in pairs:
		if pair[0] not in new_dict:
			new_dict[pair[0]] = {}
		if pair[1] not in new_dict[pair[0]]:
			new_dict[pair[0]][pair[1]] = 0
		new_dict[pair[0]][pair[1]] += 1
	return new_dict

if __name__ == '__main__':
	main()
