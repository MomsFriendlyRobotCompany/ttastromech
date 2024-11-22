#!/usr/local/bin/python
"""A simple, for-fun Text-to-Speech-like renderer
intended to seem like an authentic interaction with
a certain beloved autonomous robotic entity.
"""

import wave
# import sys
import os
from subprocess import Popen
# import audioop  # rms audio
# import time
import random
import string
import platform
import tempfile


class AudioPlayer:
    """Limited cross-platform playing of the rendered wav audio."""
    def __init__(self):
        plat = platform.system()
        if plat == 'Darwin':
            # self.audio_player = 'afplay out.wav'
            self.audio_player = 'afplay {}'

        elif plat == 'Linux':
            for play in ['aplay', 'play']:
                # TODO: research/consider paplay , ffplay , and mplayer as well?
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

                #TODO: plat == 'Windows':
                #use start, but only after cd to file dir
        else:
            raise Exception('OS is unsupported')

    def play(self, data):
        """Attempt audible playing of pre-rendered wav file in storage."""
        temp = tempfile.NamedTemporaryFile()
        wav_file = wave.open(temp.name, 'wb')
        wav_file.setnchannels(1)  # mono
        wav_file.setsampwidth(2)  # 16 bits
        wav_file.setframerate(22050)  # Hz
        wav_file.writeframes(data)
        wav_file.close()

        Popen(self.audio_player.format(temp.name), shell=True).wait()
        temp.close()


class TTAstromech:
    """Interface and 'language' programming."""
    def __init__(self):
        base_location = os.path.dirname(__file__)
        # print('ttastromech is located:', base_location)
        self.root = base_location + "/sounds/{0}.wav"
        letters = [
            "a", "b", "c", "c1", "d", "e", "f", "g", "g1", "h", "i", "j", "k",
            "l", "m", "n", "o", "o1", "p", "q", "r", "s", "s1", "t", "u", "u1",
            "v", "w", "x", "y", "z"
        ]

        self.audio_player = AudioPlayer()

        # At startup, pregenerate the syllabary in memory
        # with the audio data for later quick render.
        self.syllabary = {}
        for key in letters:
            data = self.generate(key)
            self.syllabary[key] = data

    def generate(self, syllable):
        """Pull the audio data off of disk corresponding to the syllable."""
        audio_data = b""

        if not syllable.isalnum():
            print("skipping unsupported syllable/letter" + syllable)
        else:
            syllable = syllable.lower()  # need this?
            try:
                wav_file = wave.open(self.root.format(syllable), "rb")
                audio_data += wav_file.readframes(wav_file.getnframes())
                wav_file.close()
            except Exception as fs_ex:
                print(fs_ex)
        return audio_data

    def run(self):
        """Demo, quick test only. Infinite loop."""
        while True:
            word = self.getnrandom()
            print('phrase:', word)
            self.speak(word)

    def getnrandom(self, n=6):
        """Quick and dirty random letter set for effect."""
        char_set = string.ascii_lowercase
        return ''.join(random.sample(char_set, n))

    def speak(self, phrase):
        """Concatenate wave audio data corresponding to input
        and invoke the audio render."""
        data = b""
        previous_ltr= b""
        double_letters = [letter[0] for letter in self.syllabary if '1' in letter]
        for ltr in phrase:
            if ltr.isalpha():
                if ltr == previous_ltr and ltr in double_letters:
                    data += self.syllabary[ltr+"1"]
                    #print("Double-letter syllable invoked")
                else:
                    data += self.syllabary[ltr]
                previous_ltr = ltr
        #TODO: split this into a render and play,
        #make render a public (for cases where you want to ship it out)
        self.audio_player.play(data)


    # def checkVolume(self, data, threshold=20):
    #     rms = audioop.rms(data)
    #     # syllabary = 20*log10(rms)
    #     if threshold > rms:
    #         return False
    #     else:
    #         return True

    # def _play(self, data):
    #     wav_file = wave.open("out.wav", 'wb')
    #     wav_file.setnchannels(1)
    #     wav_file.setsampwidth(2)  # 16 bits
    #     wav_file.setframerate(22050)
    #     wav_file.writeframes(data)
    #     wav_file.close()
    #
    #     Popen(self.audio_player, shell=True).wait()
