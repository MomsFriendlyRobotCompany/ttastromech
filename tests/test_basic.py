import pytest
from ttastromech import TTAstromech

def test_dummy():
    assert True

def test_lowercase_letters_only():
   r2 = TTAstromech()
   r2.speak("hello world")
   assert True

