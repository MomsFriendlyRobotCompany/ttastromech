#!/usr/bin/env python

from __future__ import print_function
from ttastromech import TTAstromech
import sys
import argparse


def handleArgs():
	parser = argparse.ArgumentParser(description='Text to Astromech, creates astromech (R2-D2) sounds from text')
	# parser.add_argument('-v', '--version', help='print version number', version=__version__)
	# parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
	parser.add_argument('phrase', help='phrase to speak', type=str)
	# parser.add_argument('--stdin', help='allows you to pipe string into ttastromech')
	parser.add_argument('-s', '--size', help='how much of the input text phrase should be turned into astromech. The input phase will be trimmed to: phrase[:size]', type=int, default=10)
	# parser.add_argument('-p', '--path', help='path to write ar markers to, default is current directory', default='.')

	args = vars(parser.parse_args())
	return args


if __name__ == '__main__':
	# create an r2
	r2 = TTAstromech()

	args = handleArgs()
	# print(args)

	# allow a sting to be pipped in:
	# echo "hi how are you" | astromech-speak.py
	# if args['stdin']:
	# 	# print(sys.stdin)
	# 	for i in sys.stdin:
	# 		r2.speak(i)
	# 		exit(0)

	size = args['size']
	phrase = args['phrase']
	phrase = phrase[:size]
	print('Saying:', phrase)

	r2.speak(phrase)
