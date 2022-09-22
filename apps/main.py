import os
import sys
from frame.config import Config
from frame.context import Context
from frame.data_service.data_service import DataService
from frame.base_handler import BaseHandler
from parse.parse_processor import ParseProcessor
from feature.feature_processor import FeatureProcessor
from model.model_processor import ModelProcessor
from response.response_processor import ResponseProcessor
from frame.common import utils

from feature import handlers as feat_handlers
from model import handlers as model_handlers
import importlib

for m_name in dir(feat_handlers):
    if m_name.endswith('handler'):
        importlib.import_module('feature.handlers.' + m_name)
for m_name in dir(model_handlers):
    if m_name.endswith('handler'):
        importlib.import_module('model.handlers.' + m_name)


WORK_DIR = '/Users/porcodio/projects/simple_ms/'
class App(object):
    def __init__(self):
        pass

    def init(self):
        self.__config = Config(WORK_DIR + 'conf/')
        self.__data_service = DataService(WORK_DIR, self.__config.data_conf)
        self.__handlers = self.__init_handlers(self.__config.main_conf['handlers'])

    def process(self, req):
        self.__context = Context()
        self.__context.handler_factory = self.__handlers
        self.__context.data_service = self.__data_service
        self.__context.conf = self.__config

        self.__parse_processor = ParseProcessor()
        self.__feature_processor = FeatureProcessor()
        self.__model_processor = ModelProcessor()
        self.__response_processor = ResponseProcessor()

        self.__context.request.url = req
        self.__parse_processor.process(self.__context)
        self.__feature_processor.process(self.__context)
        self.__model_processor.process(self.__context)
        self.__response_processor.process(self.__context)
        ret = self.__context.response
        return ret

    def __init_handlers(self, handler_conf):
        for c in BaseHandler.__subclasses__():
            c_instance = c(None, self.__data_service)
        handler_factory = {}
        for handler_name in handler_conf:
            item = handler_conf[handler_name]
            handler_factory[handler_name] = BaseHandler.factory[item['class']]
        return handler_factory


if __name__ == '__main__':
    app = App()
    app.init()
    utils.debug(app._App__config.main_conf)
    utils.debug(app._App__config.biz_conf)
    utils.debug(app._App__config.data_conf)
    utils.debug(app._App__handlers)
    res = app.process('biz=example&feat=doc:d1,d2,d3,d4;query:q1')
    print(res)

