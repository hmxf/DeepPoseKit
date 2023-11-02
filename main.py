# -*- coding: utf-8 -*-

import keras_core as keras
from deepposekit.io import DataGenerator, TrainingGenerator
from deepposekit.models import StackedDenseNet

data_generator = DataGenerator('data/annotation_data_release.h5')

train_generator = TrainingGenerator(data_generator)
model = StackedDenseNet(train_generator)

model.fit(batch_size=16, n_workers=16)

model.save('data/saved_model.h5')
