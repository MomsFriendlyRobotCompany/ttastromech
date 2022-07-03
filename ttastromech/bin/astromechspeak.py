#!/usr/bin/env python3
from ttastromech import TTAstromech
import sys
import argparse


def handleArgs():
    parser = argparse.ArgumentParser(description='Text to Astromech, creates astromech (R2-D2) sounds from text')
    parser.add_argument('phrase', help='phrase to speak', type=str)
    parser.add_argument('-s', '--size', help='how much of the input text phrase should be turned into astromech. The input phase will be trimmed to: phrase[:size]', type=int, default=10)

    args = vars(parser.parse_args())
    return args


if __name__ == '__main__':
    # create an r2
    r2 = TTAstromech()

    args = handleArgs()

    size = args['size']
    phrase = args['phrase']
    phrase = phrase[:size]
    print('Saying:', phrase)

    r2.speak(phrase)
