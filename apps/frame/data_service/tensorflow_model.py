import os
import sys
import json
from .base_data import BaseData
import tensroflow as tf


class TensorflowModel(BaseData):
    def __init__(self):
        super(TensorflowModel, self).__init__()
        self.factory[self.__class__.__name__] = self
        self.__graph = tf.Graph()
        self.__graph.as_default()
        self.__sess = tf.Session(graph=self.__graph)

    def load(self, path):
        tf.saved_model.loader.load(self.__sess, [tf.saved_model.tag_constants.SERVING], path)
        return True

    def query(self, key, value):
        feed_dict = {}
        for k in key:
            tensor_k = self.__graph.get_tensor_by_name(k + ':0')
            feed_dict[tensor_k] = key[k]
        output = []
        for v in value:
            tensor_v = self.__graph.get_tensor_by_name(v + ':0')
            output.append(tensor_v)
        y = self.__sess.run(output,feed_dict=feed_dict)
        return y

