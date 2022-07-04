import numpy as np


class MLDataset(object):

    def __init__(self, data_X, data_Y=None):
        # data shape be like (N_sample, *Feat_Size)
        self.data_X = np.array(data_X)
        self.data_Y = np.array(data_Y)

    def get_features(self):
        return self.data_X
    
    def get_labels(self):
        return self.data_Y

    def insert_data(self, X, Y):
        X = np.array(X)
        Y = np.array(Y)
        self.data_X = np.append(self.data_X, X)
        self.data_Y = np.append(self.data_Y, Y)

    def get_data_by_index(self, index):
        return self.data_X[index], self.data_Y[index]

    def __len__(self):
        return self.data_X.shape[0]
