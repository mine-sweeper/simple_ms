import os
import sys


if sys.version[0] == '2':
    import model_processor
elif sys.version[0] == '3':
    from .handlers import encoder_handler
    from .handlers import classifier_handler
    from .handlers import tf_handler
