import numpy as np
from typing import Callable
from sklearn.metrics import mean_absolute_error, mean_squared_error

from models.AbstractModel import *
from utils.dataset import MLDataset
from utils.utils import from_text_to_number


class MLModel(AbstractMLModel):

    def __init__(
            self,
            model_constructor: Callable,
            train_data: MLDataset, 
            valid_data: MLDataset, 
            test_data: MLDataset,
            init_prop=None,
            init_stats=None,
        ):
        super(AbstractMLModel, self).__init__()
        
        # data
        self.train_data = train_data
        self.valid_data = valid_data
        self.test_data = test_data
        
        # props
        self.prop = {
            "level": 1,
            "power": 1,
            "allow": 0.1,
            "speed": 1,
        } if init_prop is None else init_prop

        self.stats = {
            "train_loss": [],
            "valid_metric": [],
            "test_metric": []
        } if init_stats is None else init_stats

        # model
        self.metric = mean_absolute_error
        self.model = model_constructor()
        self.ready2predict = 10


    def set_data(self, data, category="train"):
        if category == "train":
            self.train_data = data
        if category == "valid":
            self.valid_data = data
        if category == "test":
            self.test_data = data

    def reset(self, train_data=None, valid_data=None, test_data=None):
        
        # reset model, data(if necessary) and remaining step

        self.model = LinearRegression()
        if train_data is not None:
            self.set_data(train_data, "train")
        if valid_data is not None:
            self.set_data(valid_data, "valid")
        if test_data is not None:
            self.set_data(test_data, "test")

        self.ready2predict = 10


    def step(self):
        self.ready2predict -= self.prop["speed"]
        if self.ready2predict <= 0:
            self.train()
            self.stats["valid_metric"].append(from_text_to_number(self.fit()))


    def train(self):
        self.model.fit(X=self.train_data.get_features(), Y=self.train_data.get_labels())


    @log("game_process.log")
    def fit(self):
        pred_Y = self.model.predict(X=self.valid_data.get_features())
        metrics = self.metric(self.valid_data.get_labels(), pred_Y)
        return f"_info_Model's {self.metric.__str__} is %{metrics}%."

    def attack(self):
        pred_Y = self.model.predict(self.test_data.get_features())
        hits = np.zeros(len(self.test_data))
        for i, (pY, tY) in enumerate(zip(pred_Y, self.test_data.get_labels())):
            if abs(tY-pY) <= self.prop["allow"]:
                hits[i] = 1
        self.stats["test_metric"].append(self.metric(self.test_data.get_labels()), pred_Y)
        return hits

    def update(self, key, value):
        self.prop[key] += value