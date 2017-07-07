.. image:: https://raw.githubusercontent.com/MomsFriendlyRobotCompany/ttastromech/master/docs/pics/r2.gif
	:target: https://github.com/MomsFriendlyRobotCompany/ttastromech

Text to Astromech
========================

.. image:: https://img.shields.io/pypi/l/ttastromech.svg
	:target: https://github.com/MomsFriendlyRobotCompany/ttastromech
.. image:: https://img.shields.io/pypi/pyversions/ttastromech.svg
	:target: https://github.com/MomsFriendlyRobotCompany/ttastromech
.. image:: https://img.shields.io/pypi/wheel/ttastromech.svg
	:target: https://github.com/MomsFriendlyRobotCompany/ttastromech
.. image:: https://img.shields.io/pypi/v/ttastromech.svg
	:target: https://github.com/MomsFriendlyRobotCompany/ttastromech

This was originally created by `Hugo SCHOCH <https://github.com/hug33k/PyTalk-R2D2>`_.
I just packaged it on pypi and use it for an R2D2 project I am working on.

It works by assigning an R2-D2 sound to each letter of the alphabet, then, when you pass
it a string, it makes sounds like an astromech. Currently it only supports Linux and
macOS.

========= ================
OS        Audio Program
========= ================
macOS     ``afplay``
linux     ``play`` from libsox
linux     ``aplay`` from alsa
========= ================

Install
----------

The preferred method of installation is::

	pip install ttastromech

Usage
-------

.. code-block:: python

	from ttastromech import TTAstromech
	import time


	if __name__ == '__main__':
		r2 = TTAstromech()

		try:
			r2.run()  # make random astromech sounds by feeding it random strings of letters
			time.sleep(2)
		except KeyboardInterrupt:
			print('bye ...')

Or::

	astromech.py "my god, its full of stars ... oh wait, the wrong movie"

MIT License
============

**Copyright (c) 2015 SCHOCH Hugo**

**Copyright (c) 2017 Kevin J. Walchko**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
