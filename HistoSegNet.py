from util import prepare
import os

cur_path = os.path.abspath(os.path.curdir)
dataset_dir = os.path.join(cur_path, 'dataset')
input_dir = dataset_dir
prepare.find_img(input_dir)