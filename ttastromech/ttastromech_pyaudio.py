from ttastromech import TTAstromech

try:
	import pyaudio

	class TTAstromechPyAudio(TTAstromech):
		def __init__(self, path="/sounds"):
			TTAstromech.__init__(self, path)

		def _play(self, data):
			p = pyaudio.PyAudio()
			stream = p.open(
				format=p.get_format_from_width(2),
				channels=1,
				rate=22050,
				output=True
			)

			stream.write(data)
			p.terminate()

except ImportError:

	class TTAstromechPyAudio(TTAstromech):
		def __init__(self, path="/sounds"):
			TTAstromech.__init__(self, path)
			print('<<< Need to install pyaudio >>>')

		def _play(self, data):
			print('Error: no pyaudio installed')
