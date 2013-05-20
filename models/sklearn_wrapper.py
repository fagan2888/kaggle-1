""" Wraps a Scikit-learn class. 
It takes a an instance of a class as an init argument
and then assigns this class to its model attribute.

to_wrap = ExtraTreesRegressor()
model = SklearnWrapper(to_wrap)
model.fit(data, targets)
model.predict(data)
"""

class SklearnWrapper():

    def __init__(self, model):
        self.model = model

    def fit(self, data, targets):
        self.model.fit(data, targets)

    def predict(self, data, debug=False):
        pred = self.model.predict(data)
        if debug: print pred, ' for ', data
        return pred
