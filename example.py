#!/usr/bin/env python3

from ttastromech import TTAstromech
import time


if __name__ == '__main__':
    r2 = TTAstromech()

    try:
        r2.run()  # make random astromech sounds
        time.sleep(2)
    except KeyboardInterrupt:
        print('bye ...')
