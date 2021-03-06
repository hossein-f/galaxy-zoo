from __future__ import division
from sklearn import ensemble
import classes
from models.Base import BaseModel, CascadeModel, KMeansModel


class GridSample75Mixin(object):
    @staticmethod
    def process_image(img):
        return img.grid_sample(20, 2).flatten().astype('float64') / 255


class RandomForestModel(GridSample75Mixin, BaseModel):
    train_predictors_file = 'data/data_random_forest_train_001.npy'
    test_predictors_file = 'data/data_random_forest_test_001.npy'
    n_features = 75
    estimator_defaults = {
        'n_estimators': 250,
        'random_state': 0,
        'verbose': 3,
        'oob_score': True,
    }
    estimator_class = ensemble.RandomForestRegressor


class RandomForestMoreFeatures(BaseModel):
    train_predictors_file = 'data/data_random_forest_train_002.npy'
    test_predictors_file = 'data/data_random_forest_test_002.npy'
    n_features = 675
    estimator_defaults = {
        'n_estimators': 50,
        'random_state': 0,
        'verbose': 3,
        'oob_score': True,
    }
    estimator_class = ensemble.RandomForestRegressor

    @staticmethod
    def process_image(img):
        data = img.crop(150).rescale(0.1).data.copy()
        return data.flatten().astype('float64') / 225


class RandomForestCascadeModel(GridSample75Mixin, CascadeModel):
    train_predictors_file = 'data/data_random_forest_train_001.npy'
    test_predictors_file = 'data/data_random_forest_test_001.npy'
    n_features = 75
    estimator_defaults = {
        'n_estimators': 10,
        'random_state': 0,
        'verbose': 1,
        'oob_score': True,
        }
    estimator_class = ensemble.RandomForestRegressor


class ExtraTreesModel(GridSample75Mixin, BaseModel):
    train_predictors_file = 'data/data_random_forest_train_001.npy'
    test_predictors_file = 'data/data_random_forest_test_001.npy'
    n_features = 75
    estimator_defaults = {
        'n_estimators': 15,
        'random_state': 0,
        'verbose': 3,
    }
    estimator_class = ensemble.ExtraTreesRegressor


class KMeansRandomForest(KMeansModel):
    train_predictors_file = 'data/data_kmeans_rf_train_002.npy'
    test_predictors_file = 'data/data_kmeans_rf_test_002.npy'
    estimator_defaults = {
        'n_estimators': 250,
        'random_state': 0,
        'verbose': 3,
        'oob_score': True,
    }
    estimator_class = ensemble.RandomForestRegressor
