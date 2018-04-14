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
	pairs = makePairs(text)
	cfb = build_dict(pairs)
	generated_text = generate(cfb, first_word, length)
	print(generated_text)

def makePairs(text):
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
		count = 0
		if word not in cfb: #Go back to the first word if we reach a dead end
			word = initial_word
			continue
		for next_word in cfb[word]:
			count += cfb[word][next_word]
		rand_count = random.randrange(count)
		word_iterator = iter(cfb[word])
		while(rand_count > 0):
			next_word = next(word_iterator)
			rand_count -= cfb[word][next_word]
		word = next_word #Pick the next word randomly based on the probability of each following word
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
