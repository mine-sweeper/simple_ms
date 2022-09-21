import os
import sys
import json
from .base_data import BaseData
from .example_model import ExampleModel


class DataService(dict):
    def __init__(self, work_dir, data_conf):
        self.__data = {}

        for d in BaseData.__subclasses__():
            d_instance = d()
            BaseData.factory[d.__name__] = d_instance

        for item in data_conf:
            data_name, data_type, data_dir, data_file = item['name'], item['type'], item['dir'], item['file']
            data_path = os.path.join(work_dir, 'data', data_dir, data_file)
            data_handler = BaseData.factory[data_type].kage_bunshin()
            data_handler.load(data_path)
            self.__data[data_name] = data_handler

    def __getitem__(self, key):
        return self.__data[key]

    def update(self, data_name):
        pass

