# Utils
from utils.logger import log

# ML
import xgboost as xgb
import lightgbm as lgb
from sklearn.linear_model import LinearRegression

# DL
import torch
import torch.nn as nn



class AbstractMLModel(object):

    def __init__(self):
        pass

    def attack(self):
        # model attack behavior
        raise NotImplementedError

    def update(self):
        # model update behavior
        # different model have different update path
        # and path
        raise NotImplementedError


class AbstractDLModel(nn.Module):

    def __init__(self):
        """
        All DL Model are implemented by torch
        Need super() at __init__ 
        """
        super(AbstractDLModel, self).__init__()

    def train(self):
        # model train behavior
        # during training stage
        raise NotImplementedError

    def fit(self):
        # model valid behavior
        # during training stage
        raise NotImplementedError

    def attack(self):
        # model attack behavior
        # during testing stage
        raise NotImplementedError

    def update(self):
        # model update behavior
        # different model have different update path
        # and path
        raise NotImplementedError


class ModelProp(object):

    def __init__(self, prop_dict=None):
        if self.prop_dict is None:
            self.prop_dict = {}
        else:
            self.prop_dict = prop_dict

    @log("system.log")
    def add_level(self, level_index, level_prop):
        self.prop_dict[level_index] = level_prop
        if level_index in self.prop_dict.keys():
            return f"_warn_Changing Level {level_index} to {level_prop}"
        else:
            return f"_info_Setting Level {level_index} to {level_prop}"
    
    @log("system.log")
    def delete_devel(self, level_index):
        if level_index not in self.prop_dict.keys():
            return f"_error_Level {level_index} not found in prop dict"    
        else:
            self.prop_dict.pop(level_index)
            return f"_info_Deleted {level_index}"

    def info(self):
        for key, value in self.prop_dict.items():
            print(f"Level {key}: {value}")