import os
import sys


if sys.version[0] == '2':
    import feature_processor
elif sys.version[0] == '3':
    from .handlers import query_feat_handler
    from .handlers import doc_feat_handler
