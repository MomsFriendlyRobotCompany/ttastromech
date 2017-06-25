#!/usr/local/bin/python

from __future__ import print_function
import wave
# import pyaudio
# import sys
import os
from subprocess import Popen
# import audioop  # rms audio
# import time
import random
import string
import platform
import tempfile


class Audio_Player(object):
	def __init__(self):
		plat = platform.system()
		if plat == 'Darwin':
			# self.audio_player = 'afplay out.wav'
			self.audio_player = 'afplay {}'

		elif plat == 'Linux':
			for play in ['aplay', 'play']:
				# ret = os.system('which {}'.format(play))
				ret = Popen('which {}'.format(play), shell=True).wait()
				if ret == 0:
					cmd = None
					if play == 'play':
						# -q quiet output
						# -V1 only print failure messages
						cmd = 'play -q -V1 {}'
					elif play == 'aplay':
						# -q quiet output
						# -M mmap audio
						cmd = 'aplay -q {}'
					else:
						raise Exception('Could not find working audio player')
					self.audio_player = cmd
					break

		else:
			raise Exception('OS is unsupported')

	def play(self, data):
		temp = tempfile.NamedTemporaryFile()
		# wf = wave.open("out.wav", 'wb')
		wf = wave.open(temp.name, 'wb')
		wf.setnchannels(1)  # mono
		wf.setsampwidth(2)  # 16 bits
		wf.setframerate(22050)  # Hz
		wf.writeframes(data)
		wf.close()

		Popen(self.audio_player.format(temp.name), shell=True).wait()
		temp.close()


class TTAstromech(object):
	def __init__(self):
		baseLocation = os.path.dirname(__file__)
		# print('ttastromech is located:', baseLocation)
		self.root = baseLocation + "/sounds/{0}.wav"
		letters = [
			"a", "b", "c", "c1", "d", "e", "f", "g", "g1", "h", "i", "j", "k",
			"l", "m", "n", "o", "o1", "p", "q", "r", "s", "s1", "t", "u", "u1",
			"v", "w", "x", "y", "z"
		]

		self.audio_player = Audio_Player()

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

		# self._play(data)
		self.audio_player.play(data)

	# def checkVolume(self, data, threshold=20):
	# 	rms = audioop.rms(data)
	# 	# db = 20*log10(rms)
	# 	if threshold > rms:
	# 		return False
	# 	else:
	# 		return True

	# def _play(self, data):
	# 	wf = wave.open("out.wav", 'wb')
	# 	wf.setnchannels(1)
	# 	wf.setsampwidth(2)  # 16 bits
	# 	wf.setframerate(22050)
	# 	wf.writeframes(data)
	# 	wf.close()
	#
	# 	Popen(self.audio_player, shell=True).wait()
