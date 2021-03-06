import classes
import run
import numpy as np

a = run.RandomForestModel()
a.train_x = a.build_train_predictors()

params = {'max_features': 'auto',
          'min_samples_leaf': 1,
          'min_samples_split': 2,
          'n_estimators': 250}
est = a.get_estimator()
est.set_params(**params)
est.fit(a.train_x, a.train_y)

import classes
import run
import numpy as np
params = {
    'n_estimators': [10, 100, 250],
    'max_features': ['sqrt', 'log2', 'auto'],
    'min_samples_split': [2, 10, 50, 100],
    'min_samples_leaf': [1, 5, 10, 25, 50]
}
a = run.RandomForestModel(grid_search_parameters=params,
                          grid_search_sample=0.1)
a.train_x = a.build_train_predictors()
a.perform_grid_search_and_cv(njobs=8)

# Results in 540 jobs, finishes in 58 minutes on a GCE highcpu 8 instance

# noinspection PyStatementEffect
"""
In [9]: b.best_params_
Out[9]:
{'max_features': 'auto',
 'min_samples_leaf': 1,
 'min_samples_split': 2,
 'n_estimators': 250}

 [11]: b.best_score_
Out[11]: -0.13285532108270079

[mean: -0.14136, std: 0.00170, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 1},
 mean: -0.13413, std: 0.00173, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 1},
 mean: -0.13348, std: 0.00178, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 250, 'min_samples_leaf': 1},
 mean: -0.13854, std: 0.00176, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 10, 'min_samples_leaf': 1},
 mean: -0.13441, std: 0.00178, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 100, 'min_samples_leaf': 1},
 mean: -0.13414, std: 0.00178, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 250, 'min_samples_leaf': 1},
 mean: -0.14004, std: 0.00157, params: {'max_features': 'sqrt', 'min_samples_split': 50, 'n_estimators': 10, 'min_samples_leaf': 1},
 mean: -0.13812, std: 0.00175, params: {'max_features': 'sqrt', 'min_samples_split': 50, 'n_estimators': 100, 'min_samples_leaf': 1},
 mean: -0.13798, std: 0.00178, params: {'max_features': 'sqrt', 'min_samples_split': 50, 'n_estimators': 250, 'min_samples_leaf': 1},
 mean: -0.14167, std: 0.00144, params: {'max_features': 'sqrt', 'min_samples_split': 100, 'n_estimators': 10, 'min_samples_leaf': 1},
 mean: -0.14066, std: 0.00173, params: {'max_features': 'sqrt', 'min_samples_split': 100, 'n_estimators': 100, 'min_samples_leaf': 1},
 mean: -0.14064, std: 0.00174, params: {'max_features': 'sqrt', 'min_samples_split': 100, 'n_estimators': 250, 'min_samples_leaf': 1},
 mean: -0.13819, std: 0.00150, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 5},
 mean: -0.13532, std: 0.00206, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 5},
 mean: -0.13506, std: 0.00196, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 250, 'min_samples_leaf': 5},
 mean: -0.13819, std: 0.00150, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 10, 'min_samples_leaf': 5},
 mean: -0.13532, std: 0.00206, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 100, 'min_samples_leaf': 5},
 mean: -0.13506, std: 0.00196, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 250, 'min_samples_leaf': 5},
 mean: -0.14008, std: 0.00120, params: {'max_features': 'sqrt', 'min_samples_split': 50, 'n_estimators': 10, 'min_samples_leaf': 5},
 mean: -0.13834, std: 0.00186, params: {'max_features': 'sqrt', 'min_samples_split': 50, 'n_estimators': 100, 'min_samples_leaf': 5},
 mean: -0.13825, std: 0.00188, params: {'max_features': 'sqrt', 'min_samples_split': 50, 'n_estimators': 250, 'min_samples_leaf': 5},
 mean: -0.14179, std: 0.00139, params: {'max_features': 'sqrt', 'min_samples_split': 100, 'n_estimators': 10, 'min_samples_leaf': 5},
 mean: -0.14083, std: 0.00169, params: {'max_features': 'sqrt', 'min_samples_split': 100, 'n_estimators': 100, 'min_samples_leaf': 5},
 mean: -0.14078, std: 0.00179, params: {'max_features': 'sqrt', 'min_samples_split': 100, 'sudo apt-get install python-devn_estimators': 250, 'min_samples_leaf': 5},
 mean: -0.13918, std: 0.00162, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 10},
 mean: -0.13687, std: 0.00187, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 10},
 mean: -0.13675, std: 0.00186, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 250, 'min_samples_leaf': 10},
 mean: -0.13918, std: 0.00162, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 10, 'min_samples_leaf': 10},
 mean: -0.13687, std: 0.00187, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 100, 'min_samples_leaf': 10},
 mean: -0.13675, std: 0.00186, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 250, 'min_samples_leaf': 10},
 mean: -0.14004, std: 0.00163, params: {'max_features': 'sqrt', 'min_samples_split': 50, 'n_estimators': 10, 'min_samples_leaf': 10},
 mean: -0.13876, std: 0.00183, params: {'max_features': 'sqrt', 'min_samples_split': 50, 'n_estimators': 100, 'min_samples_leaf': 10},
 mean: -0.13866, std: 0.00179, params: {'max_features': 'sqrt', 'min_samples_split': 50, 'n_estimators': 250, 'min_samples_leaf': 10},
 mean: -0.14229, std: 0.00143, params: {'max_features': 'sqrt', 'min_samples_split': 100, 'n_estimators': 10, 'min_samples_leaf': 10},
 mean: -0.14111, std: 0.00175, params: {'max_features': 'sqrt', 'min_samples_split': 100, 'n_estimators': 100, 'min_samples_leaf': 10},
 mean: -0.14102, std: 0.00179, params: {'max_features': 'sqrt', 'min_samples_split': 100, 'n_estimators': 250, 'min_samples_leaf': 10},
 mean: -0.14120, std: 0.00141, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 25},
 mean: -0.13992, std: 0.00183, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 25},
 mean: -0.13990, std: 0.00175, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 250, 'min_samples_leaf': 25},
 mean: -0.14120, std: 0.00141, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 10, 'min_samples_leaf': 25},
 mean: -0.13992, std: 0.00183, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 100, 'min_samples_leaf': 25},
 mean: -0.13990, std: 0.00175, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 250, 'min_samples_leaf': 25},
 mean: -0.14120, std: 0.00141, params: {'max_features': 'sqrt', 'min_samples_split': 50, 'n_estimators': 10, 'min_samples_leaf': 25},
 mean: -0.13992, std: 0.00183, params: {'max_features': 'sqrt', 'min_samples_split': 50, 'n_estimators': 100, 'min_samples_leaf': 25},
 mean: -0.13990, std: 0.00175, params: {'max_features': 'sqrt', 'min_samples_split': 50, 'n_estimators': 250, 'min_samples_leaf': 25},
 mean: -0.14260, std: 0.00132, params: {'max_features': 'sqrt', 'min_samples_split': 100, 'n_estimators': 10, 'min_samples_leaf': 25},
 mean: -0.14169, std: 0.00170, params: {'max_features': 'sqrt', 'min_samples_split': 100, 'n_estimators': 100, 'min_samples_leaf': 25},
 mean: -0.14170, std: 0.00174, params: {'max_features': 'sqrt', 'min_samples_split': 100, 'n_estimators': 250, 'min_samples_leaf': 25},
 mean: -0.14376, std: 0.00151, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 50},
 mean: -0.14288, std: 0.00173, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 50},
 mean: -0.14283, std: 0.00169, params: {'max_features': 'sqrt', 'min_samples_split': 2, 'n_estimators': 250, 'min_samples_leaf': 50},
 mean: -0.14376, std: 0.00151, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 10, 'min_samples_leaf': 50},
 mean: -0.14288, std: 0.00173, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 100, 'min_samples_leaf': 50},
 mean: -0.14283, std: 0.00169, params: {'max_features': 'sqrt', 'min_samples_split': 10, 'n_estimators': 250, 'min_samples_leaf': 50},
 mean: -0.14376, std: 0.00151, params: {'max_features': 'sqrt', 'min_samples_split': 50, 'n_estimators': 10, 'min_samples_leaf': 50},
 mean: -0.14288, std: 0.00173, params: {'max_features': 'sqrt', 'min_samples_split': 50, 'n_estimators': 100, 'min_samples_leaf': 50},
 mean: -0.14283, std: 0.00169, params: {'max_features': 'sqrt', 'min_samples_split': 100, 'n_estimators': 250, 'min_samples_leaf': 50},
 mean: -0.14108, std: 0.00138, params: {'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 1},
 mean: -0.13419, std: 0.00174, params: {'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 1},
 mean: -0.13370, std: 0.00182, params: {'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 250, 'min_samples_leaf': 1},
 mean: -0.13870, std: 0.00138, params: {'max_features': 'log2', 'min_samples_split': 10, 'n_estimators': 10, 'min_samples_leaf': 1},
 mean: -0.13484, std: 0.00178, params: {'max_features': 'log2', 'min_samples_split': 10, 'n_estimators': 100, 'min_samples_leaf': 1},
 mean: -0.13462, std: 0.00177, params: {'max_features': 'log2', 'min_samples_split': 10, 'n_estimators': 250, 'min_samples_leaf': 1},
 mean: -0.14011, std: 0.00159, params: {'max_features': 'log2', 'min_samples_split': 50, 'n_estimators': 10, 'min_samples_leaf': 1},
 mean: -0.13855, std: 0.00171, params: {'max_features': 'log2', 'min_samples_split': 50, 'n_estimators': 100, 'min_samples_leaf': 1},
 mean: -0.13840, std: 0.00176, params: {'max_features': 'log2', 'min_samples_split': 50, 'n_estimators': 250, 'min_samples_leaf': 1},
 mean: -0.14209, std: 0.00177, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 10, 'min_samples_leaf': 1},
 mean: -0.14111, std: 0.00163, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 100, 'min_samples_leaf': 1},
 mean: -0.14105, std: 0.00169, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 250, 'min_samples_leaf': 1},
 mean: -0.13873, std: 0.00148, params: {'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 5},
 mean: -0.13569, std: 0.00185, params: {'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 5},
 mean: -0.13537, std: 0.00188, params: {'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 250, 'min_samples_leaf': 5},
 mean: -0.13873, std: 0.00148, params: {'max_features': 'log2', 'min_samples_split': 10, 'n_estimators': 10, 'min_samples_leaf': 5},
 mean: -0.13569, std: 0.00185, params: {'max_features': 'log2', 'min_samples_split': 10, 'n_estimators': 100, 'min_samples_leaf': 5},
 mean: -0.13537, std: 0.00188, params: {'max_features': 'log2', 'min_samples_split': 10, 'n_estimators': 250, 'min_samples_leaf': 5},
 mean: -0.14058, std: 0.00208, params: {'max_features': 'log2', 'min_samples_split': 50, 'n_estimators': 10, 'min_samples_leaf': 5},
 mean: -0.13886, std: 0.00185, params: {'max_features': 'log2', 'min_samples_split': 50, 'n_estimators': 100, 'min_samples_leaf': 5},
 mean: -0.13865, std: 0.00177, params: {'max_features': 'log2', 'min_samples_split': 50, 'n_estimators': 250, 'min_samples_leaf': 5},
 mean: -0.14221, std: 0.00143, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 10, 'min_samples_leaf': 5},
 mean: -0.14124, std: 0.00170, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 100, 'min_samples_leaf': 5},
 mean: -0.14124, std: 0.00175, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 250, 'min_samples_leaf': 5},
 mean: -0.13896, std: 0.00189, params: {'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 10},
 mean: -0.13740, std: 0.00179, params: {'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 10},
 mean: -0.13720, std: 0.00181, params: {'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 250, 'min_samples_leaf': 10},
 mean: -0.13896, std: 0.00189, params: {'max_features': 'log2', 'min_samples_split': 10, 'n_estimators': 10, 'min_samples_leaf': 10},
 mean: -0.13740, std: 0.00179, params: {'max_features': 'log2', 'min_samples_split': 10, 'n_estimators': 100, 'min_samples_leaf': 10},
 mean: -0.13720, std: 0.00181, params: {'max_features': 'log2', 'min_samples_split': 10, 'n_estimators': 250, 'min_samples_leaf': 10},
 mean: -0.14035, std: 0.00188, params: {'max_features': 'log2', 'min_samples_split': 50, 'n_estimators': 10, 'min_samples_leaf': 10},
 mean: -0.13922, std: 0.00184, params: {'max_features': 'log2', 'min_samples_split': 50, 'n_estimators': 100, 'min_samples_leaf': 10},
 mean: -0.13915, std: 0.00180, params: {'max_features': 'log2', 'min_samples_split': 50, 'n_estimators': 250, 'min_samples_leaf': 10},
 mean: -0.14229, std: 0.00140, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 10, 'min_samples_leaf': 10},
 mean: -0.14144, std: 0.00160, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 100, 'min_samples_leaf': 10},
 mean: -0.14146, std: 0.00168, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 250, 'min_samples_leaf': 10},
 mean: -0.14164, std: 0.00186, params: {'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 25},
 mean: -0.14039, std: 0.00179, params: {'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 25},
 mean: -0.14034, std: 0.00180, params: {'max_features': 'log2', 'min_samples_split': 50, 'n_estimators': 250, 'min_samples_leaf': 25},
 mean: -0.14283, std: 0.00185, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 10, 'min_samples_leaf': 25},
 mean: -0.14203, std: 0.00167, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 100, 'min_samples_leaf': 25},
 mean: -0.14205, std: 0.00169, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 250, 'min_samples_leaf': 25},
 mean: -0.14393, std: 0.00173, params: {'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 50},
 mean: -0.14314, std: 0.00170, params: {'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 50},
 mean: -0.14313, std: 0.00167, params: {'max_features': 'log2', 'min_samples_split': 2, 'n_estimators': 250, 'min_samples_leaf': 50},
 mean: -0.14393, std: 0.00173, params: {'max_features': 'log2', 'min_samples_split': 10, 'n_estimators': 10, 'min_samples_leaf': 50},
 mean: -0.14314, std: 0.00170, params: {'max_features': 'log2', 'min_samples_split': 10, 'n_estimators': 100, 'min_samples_leaf': 50},
 mean: -0.14313, std: 0.00167, params: {'max_features': 'log2', 'min_samples_split': 10, 'n_estimators': 250, 'min_samples_leaf': 50},
 mean: -0.14393, std: 0.00173, params: {'max_features': 'log2', 'min_samples_split': 50, 'n_estimators': 10, 'min_samples_leaf': 50},
 mean: -0.14314, std: 0.00170, params: {'max_features': 'log2', 'min_samples_split': 50, 'n_estimators': 100, 'min_samples_leaf': 50},
 mean: -0.14313, std: 0.00167, params: {'max_features': 'log2', 'min_samples_split': 50, 'n_estimators': 250, 'min_samples_leaf': 50},
 mean: -0.14393, std: 0.00173, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 10, 'min_samples_leaf': 50},
 mean: -0.14314, std: 0.00170, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 100, 'min_samples_leaf': 50},
 mean: -0.14313, std: 0.00167, params: {'max_features': 'log2', 'min_samples_split': 100, 'n_estimators': 250, 'min_samples_leaf': 50},
 mean: -0.13964, std: 0.00225, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 1},
 mean: -0.13331, std: 0.00214, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 1},
 mean: -0.13286, std: 0.00208, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 250, 'min_samples_leaf': 1},
 mean: -0.13756, std: 0.00210, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 10, 'min_samples_leaf': 1},
 mean: -0.13364, std: 0.00215, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 100, 'min_samples_leaf': 1},
 mean: -0.13342, std: 0.00211, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 250, 'min_samples_leaf': 1},
 mean: -0.13869, std: 0.00175, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 10, 'min_samples_leaf': 1},
 mean: -0.13724, std: 0.00216, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 100, 'min_samples_leaf': 1},
 mean: -0.13707, std: 0.00217, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 250, 'min_samples_leaf': 1},
 mean: -0.14110, std: 0.00165, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 10, 'min_samples_leaf': 1},
 mean: -0.14016, std: 0.00212, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 100, 'min_samples_leaf': 1},
 mean: -0.14005, std: 0.00212, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 250, 'min_samples_leaf': 1},
 mean: -0.13726, std: 0.00166, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 5},
 mean: -0.13403, std: 0.00212, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 5},
 mean: -0.13382, std: 0.00219, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 250, 'min_samples_leaf': 5},
 mean: -0.13726, std: 0.00166, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 10, 'min_samples_leaf': 5},
 mean: -0.13403, std: 0.00212, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 100, 'min_samples_leaf': 5},
 mean: -0.13382, std: 0.00219, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 250, 'min_samples_leaf': 5},
 mean: -0.13860, std: 0.00175, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 10, 'min_samples_leaf': 5},
 mean: -0.13735, std: 0.00218, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 100, 'min_samples_leaf': 5},
 mean: -0.13723, std: 0.00220, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 250, 'min_samples_leaf': 5},
 mean: -0.14110, std: 0.00164, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 10, 'min_samples_leaf': 5},
 mean: -0.14025, std: 0.00210, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 100, 'min_samples_leaf': 5},
 mean: -0.14014, std: 0.00213, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 250, 'min_samples_leaf': 5},
 mean: -0.13806, std: 0.00203, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 10},
 mean: -0.13560, std: 0.00219, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 10},
 mean: -0.13545, std: 0.00222, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 250, 'min_samples_leaf': 10},
 mean: -0.13806, std: 0.00203, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 10, 'min_samples_leaf': 10},
 mean: -0.13560, std: 0.00219, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 100, 'min_samples_leaf': 10},
 mean: -0.13545, std: 0.00222, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 250, 'min_samples_leaf': 10},
 mean: -0.13907, std: 0.00197, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 10, 'min_samples_leaf': 10},
 mean: -0.13771, std: 0.00217, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 100, 'min_samples_leaf': 10},
 mean: -0.13758, std: 0.00221, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 250, 'min_samples_leaf': 10},
 mean: -0.14131, std: 0.00171, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 10, 'min_samples_leaf': 10},
 mean: -0.14041, std: 0.00209, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 100, 'min_samples_leaf': 10},
 mean: -0.14033, std: 0.00214, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 250, 'min_samples_leaf': 10},
 mean: -0.13996, std: 0.00197, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 25},
 mean: -0.13881, std: 0.00213, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 25},
 mean: -0.13867, std: 0.00217, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 250, 'min_samples_leaf': 25},
 mean: -0.13996, std: 0.00197, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 10, 'min_samples_leaf': 25},
 mean: -0.13881, std: 0.00213, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 100, 'min_samples_leaf': 25},
 mean: -0.13867, std: 0.00217, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 250, 'min_samples_leaf': 25},
 mean: -0.13996, std: 0.00197, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 10, 'min_samples_leaf': 25},
 mean: -0.13881, std: 0.00213, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 100, 'min_samples_leaf': 25},
 mean: -0.13867, std: 0.00217, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 250, 'min_samples_leaf': 25},
 mean: -0.14168, std: 0.00189, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 10, 'min_samples_leaf': 25},
 mean: -0.14093, std: 0.00212, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 100, 'min_samples_leaf': 25},
 mean: -0.14086, std: 0.00215, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 250, 'min_samples_leaf': 25},
 mean: -0.14269, std: 0.00173, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 10, 'min_samples_leaf': 50},
 mean: -0.14195, std: 0.00201, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 100, 'min_samples_leaf': 50},
 mean: -0.14187, std: 0.00208, params: {'max_features': 'auto', 'min_samples_split': 2, 'n_estimators': 250, 'min_samples_leaf': 50},
 mean: -0.14269, std: 0.00173, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 10, 'min_samples_leaf': 50},
 mean: -0.14195, std: 0.00201, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 100, 'min_samples_leaf': 50},
 mean: -0.14187, std: 0.00208, params: {'max_features': 'auto', 'min_samples_split': 10, 'n_estimators': 250, 'min_samples_leaf': 50},
 mean: -0.14269, std: 0.00173, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 10, 'min_samples_leaf': 50},
 mean: -0.14195, std: 0.00201, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 100, 'min_samples_leaf': 50},
 mean: -0.14187, std: 0.00208, params: {'max_features': 'auto', 'min_samples_split': 50, 'n_estimators': 250, 'min_samples_leaf': 50},
 mean: -0.14269, std: 0.00173, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 10, 'min_samples_leaf': 50},
 mean: -0.14195, std: 0.00201, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 100, 'min_samples_leaf': 50},
 mean: -0.14187, std: 0.00208, params: {'max_features': 'auto', 'min_samples_split': 100, 'n_estimators': 250, 'min_samples_leaf': 50}]

 """

import classes
import models
classes.logstream.setLevel(classes.logging.DEBUG)
a = models.RandomForest.RandomForestCascadeModel(cv_sample=0.1)
a.run('cv')
a.run('train')
b = models.RandomForest.RandomForestModel(cv_sample=0.1)
b.estimator.set_params(n_estimators=10)
b.run('train')


import models
from models.Base import CropScaleImageTransformer
from models.KMeansFeatures import KMeansFeatureGenerator

train_x_crop_scale = CropScaleImageTransformer(training=True,
                                               # result_path='data/data_train_crop_150_scale_15.npy',
                                               crop_size=150,
                                               scaled_size=15,
                                               n_jobs=-1,
                                               memmap=True)

raw_images = train_x_crop_scale.transform()

patch_extractor = models.KMeansFeatures.PatchSampler(n_patches=1000,
                                                     patch_size=5,
                                                     n_jobs=-1)

reds = raw_images[0:100, :, :, 0]
a = patch_extractor.transform(reds)

kmeans_generator = KMeansFeatureGenerator(n_centroids=10,
                                          rf_size=5,
                                          result_path='foo.npy',
                                          n_iterations=20,
                                          n_jobs=1)

kmeans_generator.fit(a)
train_reds = kmeans_generator.transform(reds, stride_size=2)