# -*- coding: utf-8 -*-

import keras_core as keras

from deepposekit.models import load_model
from deepposekit.io import VideoReader

model = keras.saving.load_model(filepath='data/saved_model.keras', custom_objects=None, compile=True, safe_mode=True)
reader = VideoReader('data/video.avi')

predictions = model.predict(reader)