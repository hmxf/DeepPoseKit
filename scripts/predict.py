# -*- coding: utf-8 -*-

import keras_core as keras

#from deepposekit.models import load_model
#from keras.models import load_model
from deepposekit.io import VideoReader

# The `keras.saving.load_model` API won't work and will raise a 'ValueError: Unknown layer: 'ImageNormalization'.' error.
#model = keras.saving.load_model(filepath='data/saved_model.keras', custom_objects=None, compile=True, safe_mode=True)
#model = keras.saving.load_model(filepath='data/saved_model.h5', custom_objects=None, compile=True, safe_mode=True)

# Workaround: Use SavedModel format instead of '.keras' or '.h5' format.
model = keras.layers.TFSMLayer('data/saved_model', call_endpoint='serving_default')

reader = VideoReader('data/video.avi')

predictions = model.call(reader, training=False)