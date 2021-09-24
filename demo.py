import multiprocessing
import os, glob
#import random
#from sklearn.model_selection import train_test_split
#import cv2
#import numpy as np
#import pandas as pd
#import multiprocessing
#from copy import deepcopy
#from sklearn.metrics import precision_recall_curve, auc
#import tensorflow.keras as keras
#from tensorflow.keras.models import load_model
#from tensorflow.keras.utils import Sequence
#from tensorflow.keras import backend as K
#import matplotlib.pyplot as plt
#from IPython.display import Image
#from tqdm import tqdm_notebook as tqdm
#from tensorflow.python.framework import ops
#from numpy.random import seed
#seed(10)
#from tensorflow import set_random_seed
#import tensorflow as tf
#set_random_seed(10)
#import gc

cur_dir = os.path.abspath(os.path.curdir)
#print(cur_dir)
train_imgs_dir = os.path.join(cur_dir, 'training')
#print(train_imgs_dir)
valid_imgs_dir =os.path.join(cur_dir, 'validation')
#print(valid_imgs_dir)
test_imgs_dir = os.path.join(cur_dir, 'testing')
#print(test_imgs_dir)
image_width, image_height = 224, 224
num_cores = multiprocessing.cpu_count()
batch_size = 64
model_class_name = ['Timor', 'Stroma', 'Normal']
