import numpy as np
import os
import matplotlib
import numpy.matlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import time
import math


# 定义文件夹路径
cur_path = os.path.abspath(os.path.curdir)
dataset_dir = os.path.join(cur_path, 'dataset')
train_dir = os.path.join(dataset_dir, 'training')
valid_dir = os.path.join(dataset_dir, 'validation')
test_dir = os.path.join(dataset_dir, 'testing')
input_dir = dataset_dir  # 定义输入文件夹

# self.tmp_dir = os.path.join(cur_path, 'tmp', self.input_name)
# self.out_dir = os.path.join(cur_path, 'out', self.input_name)
class prepare:

    def __init__(self, params):
        if not os.path.exists(dataset_dir):
            raise Exception('Could not find user-defined dataset directory ' + dataset_dir)

        # 如果文件夹路径不存在则新建文件夹
        #mkdir_if_nexist(self.tmp_dir)
        #mkdir_if_nexist(self.out_dir)

        # Read in pre-defined ADP taxonomy
        # 读入预定义的分类方法
        #self.atlas = Atlas()

    # 从输入文件夹目录中查找图像
    def find_img(self, input_dir):
        """Find images from input directory"""

        if self.verbosity == 'NORMAL':  # 调试消息的详细程度为‘NORMAL’
            print('Finding images', end='')
            start_time = time.time()  # 记录开始时间

        if self.input_mode == 'patch':
            # os.listdir() -- 返回指定的文件夹包含的文件或文件夹的名字的列表
            # os.path.isfile() -- 判断对象(需提供绝对路径)是否为文件
            # os.path.splitext() -- 分离文件名与拓展名
            # 检查文件路径合法性
            self.input_files_all = [x for x in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, x)) and
                                    os.path.splitext(x)[-1].lower() == '.png']
        elif self.input_mode == 'wsi':
            self.input_files_all = [x for x in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, x)) and
                                    os.path.splitext(x)[0].split('_f')[1] == '1']
        if self.verbosity == 'NORMAL':
            print(' (%s seconds)' % (time.time() - start_time))


cur_path = os.path.abspath(os.path.curdir)
dataset_dir = os.path.join(cur_path, 'dataset')
train_dir = os.path.join(dataset_dir, 'training')
valid_dir = os.path.join(dataset_dir, 'validation')
test_dir = os.path.join(dataset_dir, 'testing')
print(cur_path)
print(dataset_dir)
print(train_dir)
print(valid_dir)
print(test_dir)
