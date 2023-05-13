
'''
	ZARA ITEMS CLASSIFIER MODEL DASHBORD
'''

# -- Import module
import os
import pandas as pd
from pycaret.classification import load_experiment, load_model, dashboard

# -- Read data
df = pd.read_parquet(os.path.join('data', 'ml', 'zara_items.parquet'))

# -- Load experiment
exp = load_experiment(
	path_or_file=os.path.join('store', 'Binary_classification_experiment'),
	data=df,
	preprocess_data=True
	)

# -- Load MLA best model
model = load_model(os.path.join('store', 'models', 'Voting_Classifier_Model'))

# -- Create Model Explainer Dashboard
dashboard(model, display_format='dash')
