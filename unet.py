import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Conv2DTranspose, MaxPooling2D, UpSampling2D, Dropout, Input, Concatenate, BatchNormalization
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import cv2
from google.colab.patches import cv2_imshow
import PIL

def down_conv(tensor, n_filters, size, pool = True, padding = 'same', initializer = 'he_normal'):
  x = Conv2D(n_filters, kernel_size = size, padding = padding, activation = 'relu', kernel_initializer = initializer)(tensor)
  x = Conv2D(n_filters, kernel_size = size, padding = padding, activation = 'relu', kernel_initializer = initializer)(x)
  return x

def unet(height, width, channels, n_class, n_filters=16):

  # Converging Block
  input_layer = Input(shape = (height, width, channels))
  conv1 = down_conv(input_layer, n_filters, size = (3,3))
  max1 = MaxPooling2D(pool_size = (2,2), strides = (2,2))(conv1)
  conv2 = down_conv(max1, n_filters*2, size = (3,3))
  max2 = MaxPooling2D(pool_size = (2,2), strides = (2,2))(conv2)
  conv3 = down_conv(max2, n_filters*3, size = (3,3))
  max3 = MaxPooling2D(pool_size = (2,2), strides = (2,2))(conv3)
  conv4 = down_conv(max3, n_filters*4, size = (3,3))
  max4 = MaxPooling2D(pool_size = (2,2), strides = (2,2))(conv4)
  
  conv5 = down_conv(max4, n_filters*8, size = (3,3))

  # Expansive Block
  exp_path1 = Conv2DTranspose(n_filters*8, kernel_size = (2,2), strides = (2,2), activation = 'relu')(conv5)
  exp_path1 = Concatenate()([exp_path1, conv4])
  exp_path1 = down_conv(exp_path1, n_filters*8, size = (3,3))

  exp_path2 = Conv2DTranspose(n_filters*4, kernel_size = (2,2), strides = (2,2), activation = 'relu')(exp_path1)
  exp_path2 = Concatenate()([exp_path2, conv3])
  exp_path2 = down_conv(exp_path2, n_filters*4, size = (3,3))

  exp_path3 = Conv2DTranspose(n_filters*2, kernel_size = (2,2), strides = (2,2), activation = 'relu')(exp_path2)
  exp_path3 = Concatenate()([exp_path3, conv2])
  exp_path3 = down_conv(exp_path3, n_filters*2, size = (3,3))

  exp_path4 = Conv2DTranspose(n_filters, kernel_size = (2,2), strides = (2,2), activation = 'relu')(exp_path3)
  exp_path4 = Concatenate()([exp_path4, conv1])
  exp_path4 = down_conv(exp_path4, n_filters, size = (3,3))

  print(exp_path4.shape)

  # Output
  """output = Conv2D(n_class, kernel_size = (1,1), activation = 'softmax')(exp_path4)
  model = Model(inputs = input_layer, outputs = output)

  return model"""

if __name__ == "__main__":
  unet(256, 256, 3, 10)
