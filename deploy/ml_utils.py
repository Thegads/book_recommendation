import pandas as pd
import re
import joblib as jb
from scipy.sparse import hstack, csr_matrix
import numpy as np
import json

mdl_lr = jb.load("logistic_reg_19_10.pkl.z")
# mdl_lgbm = jb.load("lgbm_19_10.pkl.z")
title_vec = jb.load("title_vec_19_10.pkl.z")


def compute_features(data):

    reviews = data['reviews']
    classification = data['classification']
    title = data['title']

    features = np.array([reviews,classification], dtype = float)
    
    vectorized_title = title_vec.transform([title])

    feature_array = hstack([features, vectorized_title])

    return feature_array


def compute_prediction(data):
    feature_array = compute_features(data)

    p_lr = mdl_lr.predict_proba(feature_array)[0][1]
#     p_lgbm = mdl_lgbm.predict_proba(feature_array)[0][1]

    p = 1*p_lr #+ 0.3*p_lgbm
    
    return p
