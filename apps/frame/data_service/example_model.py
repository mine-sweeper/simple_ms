import os
import sys
import json
from .base_data import BaseData


class ExampleModel(BaseData):
    def __init__(self):
        super(ExampleModel, self).__init__()
        self.__weights = []
        self.factory[self.__class__.__name__] = self

    def load(self, path):
        super(ExampleModel, self).load(path)
        self.__weight = list(map(float, self._data[0].rstrip('\n').split(',')))

    def query(self, key, value):
        qf, df = key['q_vec'], key['d_vec']
        score = []
        for i in range(len(df)):
            s = sum([qq * dd for qq, dd in zip(qf, df[i])])
            score.append(s)
        return score

