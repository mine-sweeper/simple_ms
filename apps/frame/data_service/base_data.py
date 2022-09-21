import os
import sys
import json
from copy import copy


class BaseData(object):
    factory = {}
    def __init__(self):
        self._path = None
        self._data = None

    def load(self, path):
        self._path = path
        self._data = open(path).readlines()
        pass

    def query(self, key, value):
        return [1.0] * 4

    def kage_bunshin(self):
        return copy(self)

