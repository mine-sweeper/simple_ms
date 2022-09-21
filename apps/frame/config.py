import os
import sys
import json


class Config(object):
    def  __init__(self, conf_dir):
        self.main_conf = json.load(open(os.path.join(conf_dir, 'main.json')))

        self.biz_conf = {}
        biz_path = os.path.join(conf_dir, 'biz')
        for filename in os.listdir(biz_path):
            biz_conf = json.load(open(os.path.join(biz_path, filename)))
            self.biz_conf[biz_conf['biz']] = biz_conf

        self.data_conf = json.load(open(os.path.join(conf_dir, 'data.json')))

