# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 02:57:27 2020

@author: philippe
"""

from argparse import ArgumentParser
import numpy as np
import tensorflow as tf
from sys import argv

from config import Config
from model import Model

# preprocessed android distribution
args_type="java-small-model"
args_dataset_name="java-small"
args_data_dir="C:/Users/philippe/python-projects/Code2Seq/data/baselines/preprocessed/java-small/"
args_data= args_data_dir + args_dataset_name
args_test_data= args_data_dir + args_dataset_name + ".val.c2s"
args_model_dir= "C:/Users/philippe/python-projects/Code2Seq/data/model/" + args_type
args_model = args_model_dir + "/model"

# train data
argv.append("--data")
argv.append( args_data )

# test data
argv.append("--test")
argv.append( args_test_data )

# model location
argv.append("--save_prefix")
argv.append( args_model )

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-d", "--data", dest="data_path",
                        help="path to preprocessed dataset", required=False)
    parser.add_argument("-te", "--test", dest="test_path",
                        help="path to test file", metavar="FILE", required=False)

    parser.add_argument("-s", "--save_prefix", dest="save_path_prefix",
                        help="path to save file", metavar="FILE", required=False)
    parser.add_argument("-l", "--load", dest="load_path",
                        help="path to saved file", metavar="FILE", required=False)
    parser.add_argument('--release', action='store_true',
                        help='if specified and loading a trained model, release the loaded model for a smaller model '
                             'size.')
    parser.add_argument('--predict', action='store_true')
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--seed', type=int, default=239)
    args = parser.parse_args()

    np.random.seed(args.seed)
    tf.set_random_seed(args.seed)

    if args.debug:
        conf = Config.get_debug_config(args)
    else:
        conf = Config.get_default_config(args)
    print( conf )
    model = Model(conf)
    print('Created model')
    model.train()
    model.close_session()