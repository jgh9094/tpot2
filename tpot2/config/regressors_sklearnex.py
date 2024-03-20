from sklearnex.linear_model import LinearRegression
from sklearnex.linear_model import Ridge
from sklearnex.linear_model import Lasso
from sklearnex.linear_model import ElasticNet

from sklearnex.svm import SVR
from sklearnex.svm import NuSVR

from sklearnex.ensemble import RandomForestRegressor
from sklearnex.neighbors import KNeighborsRegressor

import numpy as np

from functools import partial

from ConfigSpace import ConfigurationSpace
from ConfigSpace import ConfigurationSpace, Integer, Float, Categorical, Normal



def get_RandomForestRegressor_ConfigurationSpace(random_state=None):
    space = {
        'n_estimators': 100,
        'max_features': Float("max_features", bounds=(0.05, 1.0)),
        'bootstrap': Categorical("bootstrap", [True, False]),
        'min_samples_split': Integer("min_samples_split", bounds=(2, 21)),
        'min_samples_leaf': Integer("min_samples_leaf", bounds=(1, 21)),
    }
    
    if random_state is not None: #This is required because configspace doesn't allow None as a value
        space['random_state'] = random_state
    
    return ConfigurationSpace(
        space = space
    )


def get_KNeighborsRegressor_ConfigurationSpace(n_samples=100):
    return ConfigurationSpace(
        space = {
            'n_neighbors': Integer("n_neighbors", bounds=(1, max(n_samples, 100))),
            'weights': Categorical("weights", ['uniform', 'distance']),
        }
    )

LinearRegression_configspace = ConfigurationSpace()



def get_Ridge_ConfigurationSpace(random_state=None):
    space = {
        'alpha': Float("alpha", bounds=(0.0, 1.0)),
        'fit_intercept': Categorical("fit_intercept", [True]),
        'tol': Float("tol", bounds=(1e-5, 1e-1)),
    }

    if random_state is not None: #This is required because configspace doesn't allow None as a value
        space['random_state'] = random_state

    return ConfigurationSpace(
        space = space
    )

def get_Lasso_ConfigurationSpace(random_state=None):
    space = {
        'alpha': Float("alpha", bounds=(0.0, 1.0)),
        'fit_intercept': Categorical("fit_intercept", [True]),
        'precompute': Categorical("precompute", [True, False, 'auto']),
        'tol': 0.001,
        'positive': Categorical("positive", [True, False]),
        'selection': Categorical("selection", ['cyclic', 'random']),
    }

    if random_state is not None: #This is required because configspace doesn't allow None as a value
        space['random_state'] = random_state

    return ConfigurationSpace(
        space = space
    )

def get_ElasticNet_ConfigurationSpace(random_state=None):
    space = {
        'alpha': Float("alpha", bounds=(0.0, 1.0)),
        'l1_ratio': Float("l1_ratio", bounds=(0.0, 1.0)),
    }

    if random_state is not None: #This is required because configspace doesn't allow None as a value
        space['random_state'] = random_state

    return ConfigurationSpace(
        space = space
    )


def get_SVR_ConfigurationSpace(random_state=None):
    space = {
        'kernel': Categorical("kernel", ['poly', 'rbf', 'linear', 'sigmoid']),
        'C': Float("C", bounds=(1e-4, 25), log=True),
        'degree': Integer("degree", bounds=(1, 4)),
        'max_iter': 3000,
        'tol': 0.001,
    }

    if random_state is not None: #This is required because configspace doesn't allow None as a value
        space['random_state'] = random_state

    return ConfigurationSpace(
        space = space
    )

def params_NuSVR(trial, name=None):
    return {
        'nu': trial.suggest_float(f'subsample_{name}', 0.05, 1.0),
        'kernel': trial.suggest_categorical(name=f'kernel_{name}', choices=['poly', 'rbf', 'linear', 'sigmoid']),
        'C': trial.suggest_float(f'C_{name}', 1e-4, 25, log=True),
        'degree': trial.suggest_int(f'degree_{name}', 1, 4),
        'max_iter': 3000,
        'tol': 0.005,
    }

def get_NuSVR_ConfigurationSpace(random_state=None):
    space = {
        'nu': Float("nu", bounds=(0.05, 1.0)),
        'kernel': Categorical("kernel", ['poly', 'rbf', 'linear', 'sigmoid']),
        'C': Float("C", bounds=(1e-4, 25), log=True),
        'degree': Integer("degree", bounds=(1, 4)),
        'max_iter': 3000,
        'tol': 0.005,
    }

    if random_state is not None: #This is required because configspace doesn't allow None as a value
        space['random_state'] = random_state

    return ConfigurationSpace(
        space = space
    )