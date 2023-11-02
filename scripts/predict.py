# -*- coding: utf-8 -*-

import keras_core as keras

from deepposekit.models import load_model
from deepposekit.io import VideoReader

model = load_model('data/saved_model.h5')
reader = VideoReader('data/video.avi')

predictions = model.predict(reader)