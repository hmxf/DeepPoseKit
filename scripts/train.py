# -*- coding: utf-8 -*-

import keras_core as keras

from deepposekit.io import DataGenerator, TrainingGenerator
from deepposekit.models import StackedDenseNet

data_generator = DataGenerator('data/annotation_data_release.h5')

train_generator = TrainingGenerator(data_generator)
model = StackedDenseNet(train_generator)


model.fit(batch_size=16, n_workers=8)

# There are two methods can use for saving trained model. 
# Althouht model.save() is an alias for keras_core.saving.save_model(), 
# but the former works fine but the latter doesn't, weird.

# Just choose the format you like. 
# This statement can be output normally for models in both formats.
# model.train_model.save('data/saved_model.keras')
model.train_model.save('data/saved_model.h5')

# This cannot work. Maybe someone can try dig in and find why.
# keras.saving.save_model(model, filepath='saved_model.keras', overwrite=True)
