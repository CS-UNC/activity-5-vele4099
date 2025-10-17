import pytest
from activity5 import *

def test_more_than_20(monkeypatch):
    result = more_than_20('CROSSWD.txt')
    test = ['counterdemonstrations', 'hyperaggressivenesses', 'microminiaturizations']
    assert result == test, f'Incorrect result for more_than_20 with the CROSSWD.txt file. Expected result: {test}, Actual: {result}'

def test_has_no_e():
    result1 = has_no_e('allegory')
    result2 = has_no_e('maximus')
    result3 = has_no_e('eaisousdesased')
    assert not result1, f'Incorrect result for has_no_e with the word "allegory". Expected result: False, Actual: {result1}'
    assert result2, f'Incorrect result for has_no_e with the word "maximus". Expected result: True, Actual: {result1}'
    assert not result3, f'Incorrect result for has_no_e with the word "eaisousdesased". Expected result: False, Actual: {result1}'

def test_uses_only():
    result1 = uses_only('abra','abr')
    result2 = uses_only('alakazam','alkzm')
    result3 = uses_only('maximus', 'maxiusb')
    result4 = uses_only('maximus', 'maxusb')

    assert result1, f'Incorrect result for uses_only with the word "abra" and letters "abr". Expected result: True, Actual: f{result1}'
    assert result2, f'Incorrect result for uses_only with the word "alakazam" and letters "alkzm". Expected result: True, Actual: {result2}'
    assert result3, f'Incorrect result for uses_only with the word "maximus" and letters "maxiusb". Expected result: True, Actual: {result3}'
    assert not result4, f'Incorrect result for uses_only with the word "maximus" and letters "maxusb". Expected result: False, Actual: {result4}'

def test_all_uses_only():
    result  = all_uses_only('CROSSWD.txt','abrz')
    intent = ['aa', 'aba', 'ar', 'ba', 'baa', 'baba', 'bar', 'barb', 'bazaar', 'bazar', 'bra', 'braza', 'razz']
    assert result == intent, f'Incorrect result for all_uses_only for the CROSSWD.txt file with the letters "abrz". Expected result = {intent}, actual: {result}.'
