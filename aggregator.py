'''
Loads models from collected_model and aggregates them
and saves it as a global.h5 file.
'''

import tensorflow as tf
from tensorflow.keras.models import load_model
import os

local_models = []

dir = 'collected_model'
for f in os.listdir(dir):
    if f.endswith('.h5'):
        model = load_model(os.path.join(dir, f))
        if 'global' in f:
            global_model = model
        else:
            local_model = model
            local_models.append(local_model)

model_weights = []
for model in local_models:
    weights = model.get_weights()
    model_weights.append(weights)

    model.set_weights(weights)


def aggregate_weights(model_weights):
    avg_grad = list()
    for grad_list_tuple in zip(*model_weights):
        layer_mean = tf.math.reduce_sum(grad_list_tuple, axis=0)
        avg_grad.append(layer_mean)
    return avg_grad

average_weights = aggregate_weights(model_weights)
global_model.set_weights(average_weights)

print(global_model.summary())
