from math import log, sin
from pyperclip import copy


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


def text_to_buffer(text):
    copy(text.split(': ')[-1])
