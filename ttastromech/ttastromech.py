#!/usr/local/bin/python

from __future__ import print_function
import wave
# import pyaudio
# import sys
import os
from subprocess import Popen
# import audioop  # rms audio
import time
import random
import string
import platform
# import tempfile


def print_info(f):
	info = f.getparams()
	print('Wave: {} ch, {} bits @ {} Hz'.format(info[0], info[1] * 8, info[2]))


class TTAstromech(object):
	def __init__(self, path="/sounds"):
		baseLocation = os.path.dirname(__file__)
		print('ttastromech is located:', baseLocation)
		self.root = baseLocation + path + "/{0}.wav"
		letters = [
			"a", "b", "c", "c1", "d", "e", "f", "g", "g1", "h", "i", "j", "k",
			"l", "m", "n", "o", "o1", "p", "q", "r", "s", "s1", "t", "u", "u1",
			"v", "w", "x", "y", "z"
		]

		plat = platform.system()
		if plat == 'Darwin':
			self.audio_player = 'afplay'

		elif plat == 'Linux':
			# self.audio_player = 'play'
			for play in ['play', 'aplay']:
				ret = os.system('which {}'.format(play))
				if ret == 0:
					self.audio_player = play
					break

		else:
			raise Exception('OS is unsupported')

		self.db = {}
		for key in letters:
			data = self.generate(key)
			self.db[key] = data

	def generate(self, word):
		data = b""

		for letter in word:
			letter = letter.lower()  # need this?
			if not letter.isalpha():
				continue
			try:
				f = wave.open(self.root.format(letter), "rb")
				data += f.readframes(f.getnframes())
				f.close()
			except Exception as e:
				print(e)
		return data

	def run(self):
		while True:
			word = self.getnrandom()
			print('phrase:', word)
			self.speak(word)

	def getnrandom(self, n=6):
		char_set = string.ascii_lowercase
		return ''.join(random.sample(char_set, n))

	def speak(self, phrase):
		data = b""
		for ltr in phrase:
			if ltr.isalpha():
				data += self.db[ltr]

		self._play(data)

	# def pyAud(self, data):
	# 	p = pyaudio.PyAudio()
	# 	stream = p.open(
	# 		format=p.get_format_from_width(2),
	# 		channels=1,
	# 		rate=22050,
	# 		output=True
	# 	)
	#
	# 	stream.write(data)
	# 	p.terminate()

	# def checkVolume(self, data, threshold=20):
	# 	rms = audioop.rms(data)
	# 	# db = 20*log10(rms)
	# 	if threshold > rms:
	# 		return False
	# 	else:
	# 		return True

	def _play(self, data):
		wf = wave.open("out.wav", 'wb')
		wf.setnchannels(1)
		wf.setsampwidth(2)  # 16 bits
		wf.setframerate(22050)
		wf.writeframes(data)
		wf.close()

		# set
		# -q quiet output
		# -V1 only print failure messages
		# os.system('play -q -V1 out.wav')
		Popen('{} -q -V1 out.wav'.format(self.audio_player), shell=True).wait()
