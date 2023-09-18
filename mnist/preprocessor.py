
import os
import numpy as np
import pandas as pd
import tempfile

from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from pickle import dump


# This is the location where the SageMaker Processing job
# will save the input dataset.
BASE_DIR = "/opt/ml/processing"
DATA_FILEPATH = Path(BASE_DIR) / "input" / "data.csv"


# david: this 
def preprocess(base_dir, date_filepath):
    """
    Preprocesses the supplied raw dataset and splits it into a train, validation,
    and test set.
    """
    
    
