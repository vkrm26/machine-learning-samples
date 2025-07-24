import tensorflow as tf
import numpy as np
from keras.layers import TFSMLayer


# Load model as a TFSMLayer
layer = TFSMLayer("my_model_y_3x", call_endpoint="serving_default")

# Predict
result = layer(np.array([[12.0]]))  # Input must be 2D
print(list(result.values())[0].numpy())