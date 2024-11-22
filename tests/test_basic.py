import pytest
from ttastromech import TTAstromech

def test_dummy():
    assert True

def test_lowercase_letters_only():
   r2 = TTAstromech()
   r2.speak("hello world")
   assert True

def test_double_letters():
   r2 = TTAstromech()
   r2.speak("g a giggle")
   r2.speak("u o u o uu oo")
   assert True
