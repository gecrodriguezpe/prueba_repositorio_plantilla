import numpy as np
import pandas as pd
from lark import Lark

file = "/src/config.py"


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


a = 10
b = 5
print(add(a, b))
print(substract(a, b))
print(multiply(a, b))
print(divide(a, b))

dummy_data = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5",
    "key6": "value6",
}
