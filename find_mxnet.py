try:
	import mxnet as mx
except ImportError:
	import os, sys
	curr_path = os.path.abspath(os.path.dirname(__file__))
	sys.path.append(os.path.join("/home/shhs/usr/detection/mxnet_msic/mxnet/python"))
	import mxnet as mx
