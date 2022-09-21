import os
import sys

class Base(object):
    factory = {}
    def __init__(self):
        pass

    def run(self):
        print('run base')


class Extend(Base):
    def __init__(self):
        super(Extend, self).__init__()
        self.factory[self.__class__.__name__] = self

    def run(self):
        print('run extend', self.factory)

class Poo(Base):
    def __init__(self):
        super(Poo, self).__init__()
        self.factory[self.__class__.__name__] = self

    def run(self):
        super(Poo, self).run()
        print('run poo', self.factory)


for c in Base.__subclasses__():
    ci = c()
    ci.run()

