from sklearnex.ensemble import RandomForestClassifier
from sklearnex.neighbors import KNeighborsClassifier
from sklearnex.svm import SVC
from sklearnex.svm import NuSVC
from sklearnex.linear_model import LogisticRegression

import numpy as np
from ConfigSpace import ConfigurationSpace
from ConfigSpace import ConfigurationSpace, Integer, Float, Categorical, Normal
from functools import partial

def get_RandomForestClassifier_ConfigurationSpace(random_state=None):
    space = {
            'n_estimators': 100, #TODO make this a higher number? learned?
            'bootstrap': Categorical("bootstrap", [True, False]),
            'min_samples_split': Integer("min_samples_split", bounds=(2, 20)),
            'min_samples_leaf': Integer("min_samples_leaf", bounds=(1, 20)),
            'n_jobs': 1,
            
        }
    
    if random_state is not None: #This is required because configspace doesn't allow None as a value
        space['random_state'] = random_state
    
    return ConfigurationSpace(
        space = space
    )

def get_KNeighborsClassifier_ConfigurationSpace(n_samples=10):
    return ConfigurationSpace(
        space = {
            'n_neighbors': Integer("n_neighbors", bounds=(1, max(n_samples, 100)), log=True),
            'weights': Categorical("weights", ['uniform', 'distance']),
        }
    )


#TODO add conditionals
def get_LogisticRegression_ConfigurationSpace(random_state=None):
    space = {
        'solver': Categorical("solver", ['liblinear', 'sag', 'saga']),
        'penalty': Categorical("penalty", ['l1', 'l2']),
        'dual': Categorical("dual", [True, False]),
        'C': Float("C", bounds=(1e-4, 1e4), log=True),
        'max_iter': 1000,
    }

    if random_state is not None: #This is required because configspace doesn't allow None as a value
        space['random_state'] = random_state

    return ConfigurationSpace(
        space = space
    )

def get_SVC_ConfigurationSpace(random_state=None):
    space = {
        'kernel': Categorical("kernel", ['poly', 'rbf', 'linear', 'sigmoid']),
        'C': Float("C", bounds=(1e-4, 25), log=True),
        'degree': Integer("degree", bounds=(1, 4)),
        'max_iter': 3000,
        'tol': 0.001,
        'probability': Categorical("probability", [True]), # configspace doesn't allow bools as a default value? but does allow them as a value inside a Categorical
    }

    if random_state is not None: #This is required because configspace doesn't allow None as a value
        space['random_state'] = random_state

    return ConfigurationSpace(
        space = space
    )

def get_NuSVC_ConfigurationSpace(random_state=None):
    space = {
        'nu': Float("nu", bounds=(0.05, 1.0)),
        'kernel': Categorical("kernel", ['poly', 'rbf', 'linear', 'sigmoid']),
        'C': Float("C", bounds=(1e-4, 25), log=True),
        'degree': Integer("degree", bounds=(1, 4)),
        #TODO work around for None value?
        #'class_weight': Categorical("class_weight", [None, 'balanced']),
        'max_iter': 3000,
        'tol': 0.005,
        'probability': Categorical("probability", [True]), # configspace doesn't allow bools as a default value? but does allow them as a value inside a Categorical
    }

    if random_state is not None: #This is required because configspace doesn't allow None as a value
        space['random_state'] = random_state

    return ConfigurationSpace(
        space = space
    )